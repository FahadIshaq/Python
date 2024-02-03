import os, zipfile, string, random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def get_background_js_str(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS):
    manifest_json = """
                        {
                            "version": "1.0.0",
                            "manifest_version": 2,
                            "name": "Chrome Proxy",
                            "permissions": [
                                "proxy",
                                "tabs",
                                "unlimitedStorage",
                                "storage",
                                "<all_urls>",
                                "webRequest",
                                "webRequestBlocking"
                            ],
                            "background": {
                                "scripts": ["background.js"]
                            },
                            "minimum_chrome_version":"22.0.0"
                        }
                        """
    background_js = """
                    var config = {
                            mode: "fixed_servers",
                            rules: {
                            singleProxy: {
                                scheme: "http",
                                host: "%s",
                                port: parseInt(%s)
                            },
                            bypassList: ["localhost"]
                            }
                        };

                    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

                    function callbackFn(details) {
                        return {
                            authCredentials: {
                                username: "%s",
                                password: "%s"
                            }
                        };
                    }

                    chrome.webRequest.onAuthRequired.addListener(
                                callbackFn,
                                {urls: ["<all_urls>"]},
                                ['blocking']
                    );
                    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
    return manifest_json,background_js

def get_driver_path():
    driver_path = ChromeDriverManager().install()
    return driver_path

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits  # You can also add more characters if needed
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def get_driver(user_profile_path,proxy=None):
    print("** Launching driver..")

    options = Options()
    options.add_argument("–lang= en")

    if proxy:
        print("** Using proxies -> ", proxy)

        if len(proxy.split(":"))>2: # proxy = "HOST:PORT:USERNAME:PASSWORD"
            arr = proxy.split(":")
            proxiesZipFolder = os.path.join(os.getcwd(),'proxies_zip')
            if not os.path.exists(proxiesZipFolder):
                os.mkdir(proxiesZipFolder)
            random_name = generate_random_string() + '.zip'
            pluginfile = os.path.join(proxiesZipFolder,random_name)
            manifest_json,background_js = get_background_js_str(arr[0],arr[1],arr[2],arr[3])
            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)
            options.add_extension(pluginfile)
        else:  # proxy = "HOST:PORT"
            options.add_argument('--proxy-server=%s' % proxy)
    else:
        print("** Continue with rotating ip...")


    if not os.path.exists(user_profile_path): os.mkdir(user_profile_path)

    options.add_argument("user-data-dir={}".format(user_profile_path))
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    driverPath = get_driver_path()
    
    dr =  webdriver.Chrome(options=options)
    
    return dr



if __name__ == "__main__":
    
    profilePath = os.path.join(os.getcwd(),'my-profile')
    
    driver = get_driver(profilePath)

    x = 0
    time_delay = 10
    c = ""  # Define c outside the loop
    output_filename = "output.csv"
    count = 1
    while os.path.exists(output_filename):
        output_filename = f"output_{count}.csv"
        count += 1

    # Start processing data
    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = ['Company Name', 'First Name', 'Last Name']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()

        with open("test.csv", 'r') as file:
            csvreaders = csv.reader(file, delimiter=':')
            data1 = list(csvreaders)


    
        for row in data1:
            search = data1[x][0].split(',')
            company = search[0]
            state = search[1]
            
            # Navigate to the website and perform searches
            #url = 'https://plainproxies.com/resources/free-web-proxy'
            url = 'https://opencorporates.com/'
            driver.get(url)
            driver.maximize_window()
            time.sleep(time_delay)
            
            # Perform company search
            company_input = driver.find_element(By.XPATH, '//input[@name="q"]')
            company_input.send_keys(company)
            time.sleep(time_delay)
            search_button = driver.find_element(By.XPATH, '//button[@class="oc-home-search_button"]')
            search_button.click()
            time_delay = 5
            time.sleep(time_delay)
            
            try:
                # Handle different scenarios based on company status
                status_classes = [
                    "company_search_result current_active",
                    "current_active",
                    "branch current_active",
                    "company_search_result",
                    "company_search_result in_existence",
                    "company_search_result active",
                    "company_search_result good_standing",
                    "company_search_result branch current_active",
                    "company_search_result branch active",
                    "company_search_result exists",
                    "company_search_result goodstanding",
                    "company_search_result registered",
                    "company_search_result branch registered",
                    "company_search_result reservation",
                ]
                
                for status_class in status_classes:
                    try:
                        soup = BeautifulSoup(driver.page_source, 'lxml')
                        infos = soup.find(class_=status_class).next_sibling
                        a = infos.string
                        b = a.split('(')
                        c = b[1]
                        print(c,'checking')
                        
                        if c == state:
                            driver.find_element(By.XPATH, f'//a[@class="{status_class}"]').click()
                            time.sleep(3)
                            print(state,'matched')
                            break  # Exit the loop if correct status is found
                        
                    except:
                        continue
                
                # Extract name information
                soup = BeautifulSoup(driver.page_source, 'lxml')
                infos = soup.find(class_='agent_name')
                name = infos.string.split(',')
                fullname = infos.string
                
                try:
                    first_name = name[1]
                    last_name = name[0]
                except:
                    first_name = fullname
                    last_name = ''
                
                # Write data to CSV
                csvwriter.writerow({'Company Name': company, 'First Name': first_name, 'Last Name': last_name})
                x += 1
                time_delay = 3
                print('Agent Name Saved')
                
            except:
                if c == state:
                    f = 'Agent Not Found'
                    l = 'Agent Not Found'
                    csvwriter.writerow({'Company Name': company, 'First Name': f, 'Last Name': l})
                    x += 1
                    print('Agent Not Found')
                    continue
                else:
                    f = 'Company Not Found'
                    l = 'Company Not Found'
                    csvwriter.writerow({'Company Name': company, 'First Name': f, 'Last Name': l})
                    x += 1
                    print('Company Not Found')
                    continue

# Close the browser
    driver.quit()


    while 1: pass