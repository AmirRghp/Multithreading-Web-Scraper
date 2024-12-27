import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time
from concurrent.futures import ThreadPoolExecutor

class BaseScraper:
    def __init__(self, base_url, output_folder):
        self.base_url = base_url
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)

class LinkFinder(BaseScraper):
    def find_links(self):
        """Fetches and extracts all links from the base URL."""
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)

            urls = []
            for link in links:
                href = link['href']
                full_url = urljoin(self.base_url, href)
                urls.append(full_url)

            return urls
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {self.base_url}: {e}")
            return []

class LinkFetcher(BaseScraper):
    def fetch_and_save(self, link):
        """Fetches a link and saves its HTML content as a file."""
        try:
            response = requests.get(link)
            response.raise_for_status()

            # Generate a safe file name from the URL
            file_name = link.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
            file_path = os.path.join(self.output_folder, file_name)

            # Save the HTML content to a file
            with open(file_path, mode="w", encoding="utf-8") as file:
                file.write(response.text)

            print(f"Saved: {file_name}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {link}: {e}")

class LinkScraper(LinkFinder, LinkFetcher):
    def __init__(self, base_url, output_folder, max_workers=10):
        super().__init__(base_url, output_folder)
        self.max_workers = max_workers

    def scrape_links(self):
        """Finds links and fetches them concurrently."""
        links = self.find_links()
        print(f"Total pages: {len(links)}")

        start_time = time.time()
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.fetch_and_save, links)

        duration = time.time() - start_time
        print('\n')
        print(f"Saved {len(links)} pages in {duration:.2f} seconds")

if __name__ == '__main__':
    base_url = 'your-url'
    output_folder = 'output'

    scraper = LinkScraper(base_url, output_folder, max_workers=100)
    scraper.scrape_links()
