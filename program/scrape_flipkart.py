import requests
from bs4 import BeautifulSoup

class FlipkartScraper:
    def __init__(self):
        self.base_url = "https://www.flipkart.com/search?q="

    def get_product_data(self, search_query, page_num=1):
        formatted_query = search_query.replace(" ", "+")
        url = f"{self.base_url}{formatted_query}&page={page_num}"

        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return None

    def extract_product_details(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        products = []

        results = soup.find_all("div", class_='_13oc-S')
        for result in results:
            product = {}
            product["name"] = result.find("div", class_='_4rR01T').text
            product["price"] = result.find("div", class_='_30jeq3').text
            product["link"] = "https://www.flipkart.com" + result.find("a", class_='_1fQZEK')['href']
            products.append(product)

        return products

    def scrape_multiple_pages(self, search_query, num_pages):
        for page_num in range(1, num_pages + 1):
            html_content = self.get_product_data(search_query, page_num)

            if html_content:
                products = self.extract_product_details(html_content)
                for idx, product in enumerate(products, start=(page_num - 1) * 24 + 1):
                    print(f"Product {idx}:")
                    print(f"Name: {product['name']}")
                    print(f"Price: {product['price']}")
                    print(f"Link: {product['link']}")
                    print("-" * 50)
            else:
                print(f"Failed to retrieve HTML content for page {page_num}.")

if __name__ == "__main__":
    scraper = FlipkartScraper()
    search_query = input("Enter search query: ")
    num_pages = int(input("Enter number of pages to scrape: "))
    scraper.scrape_multiple_pages(search_query, num_pages)
