from bs4 import BeautifulSoup
import requests
import os


url = f"URL"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")

heading = soup.find(name="h1", id="chapter-heading").getText()

image_urls = []
reading_content = soup.select("div div img")
for url in reading_content:
    image_urls.append(url.get("data-src").strip("\t\n"))

# Creates Folder
image_path = f"./{heading}"
os.mkdir(image_path)

# Saves images to the folder
n = 1
for url in image_urls:
    response = requests.get(url)
    with open(f"{image_path}/page-{n}.jpg", "wb") as file:
        file.write(response.content)
        n += 1
