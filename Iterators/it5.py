# Web Scraping
# When scraping data from websites, iterators can be used to handle multiple pages or elements. Instead of loading all data at once, you can load and process one page at a time.


import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        yield link.get('href')

# Usage
for link in scrape_links('https://example.com'):
    print(link)