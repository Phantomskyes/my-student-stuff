import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = "https://www.mathsisfun.com/numbers/fibonacci-sequence.html"

# Send a GET request to the URL
response = requests.get(url)
print(response.content)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find and extract the desired data from the HTML
    # Here's an example of extracting all the links on the page
    links = soup.find_all("a")
    print(links)
    for link in links:
        print(link.get("href"))

else:
    print("Failed to retrieve data from the website.")