from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import os
from selenium.webdriver.common.keys import Keys

a = 3
x = 1
start_time = time.time()
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)

webdriver_service = Service("..\ChromeWebDriver\chromedriver")  # Your chromedriver path
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
output_filename = "output_1.csv"
count = 1
while os.path.exists(output_filename):
    output_filename = f"output_{count}.csv"
    count += 1

with open(output_filename, 'w', newline='') as csvfile:
    fieldnames = ['Property Address', 'City', 'State', 'Zip']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()

    with open("propertyByCity.csv", 'r') as file:
        csvreaders = csv.reader(file, delimiter=':')
        data1 = list(csvreaders)
    for row in data1:
        try:
            search = data1[x][0].split(',')
            address = search[0]
            city = search[1]
            url = 'https://www.google.com/'
            driver.get(url)
            driver.maximize_window()
            time.sleep(a)
            search_text = f"{address}, {city}"
            search_box = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
            search_box.send_keys(search_text, Keys.RETURN)
            time.sleep(a)

            soup = BeautifulSoup(driver.page_source, 'lxml')
            try:
                try:
                    data = soup.find('span', class_="fMYBhe").string.split(',')
                    zip_c = data[1].split(' ')
                    state = zip_c[1]
                    zip_code = zip_c[2]
                    print(state, zip_code)
                except:
                    data = soup.find('span', class_="fMYBhe").string.split(',')
                    zip_c = data[2].split(' ')
                    state = zip_c[1]
                    zip_code = zip_c[2]
                    print(state, zip_code)

            except:
                data = soup.find('h3', class_="LC20lb MBeuO DKV0Md").string.split(',')
                zip_c = data[2].split(' ')
                state = zip_c[1]
                zip_code = zip_c[2]
                print(state, zip_code)

            csvwriter.writerow({'Property Address': address, 'City': city, 'State': state, 'Zip': zip_code})

            x = x + 1
            a = 0.5
        except:
            break
end_time = time.time()  # Record the end time
elapsed_time = end_time - start_time
print(f"Total time taken: {elapsed_time:.2f} seconds")
driver.quit()