import requests

from bs4 import BeautifulSoup

 

# URL of the website to scrape

url = "https://quotes.toscrape.com/"

 

# Send a GET request to the website

response = requests.get(url)

 

# Parse the HTML content using Beautiful Soup

soup = BeautifulSoup(response.content, "html.parser")

 

# Find all quote elements

quote_elements = soup.find_all("span", class_="text")

author_elements = soup.find_all("small", class_="author")

 

# Iterate through the quotes and authors and display them

for quote, author in zip(quote_elements, author_elements):

    quote_text = quote.get_text()

    author_name = author.get_text()

    print(f"Quote: {quote_text}")

    print(f"Author: {author_name}")

    print("-" * 40)
