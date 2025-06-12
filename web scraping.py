import requests
from bs4 import BeautifulSoup
url= input("Enter the URL to scrape:")
response=requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))