import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_images(url):
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create a directory to store the downloaded images
    directory = 'downloaded_images'
    os.makedirs(directory, exist_ok=True)

    # Find the slide container element
    slide_container = soup.find('div', {'class': 'slide-container'})

    if slide_container:
        # Find all the image tags within the slide container
        image_tags = slide_container.find_all('img')

        for img in image_tags:
            img_url = img.get('src')
            if img_url.endswith('.png'):
                # Download the image
                image_url = urljoin(url, img_url)
                response = requests.get(image_url)
                response.raise_for_status()

                # Extract the filename from the URL
                filename = os.path.basename(urlparse(image_url).path)

                # Save the image to the directory
                with open(os.path.join(directory, filename), 'wb') as file:
                    file.write(response.content)
                    print(f"Downloaded: {filename}")

        print("All images downloaded successfully!")
    else:
        print("No slide container found on the webpage.")


website_link = "https://agent.valvespace.com/map?office=2916"
download_images(website_link)