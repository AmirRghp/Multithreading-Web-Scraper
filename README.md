
# Multithreading Web Scraper
This project is a Simple Python-based web scraper that demonstrates the use of object-oriented programming (OOP) principles and inheritance to build a modular and efficient web scraping tool.

## Features

- **Extract Links**: Scrapes all links from a given base URL.
- **HTML Saving**: Fetches and saves the HTML content of each link as `.html` files in an output folder.
- **Concurrent Fetching**: Utilizes multithreading to process multiple links simultaneously for better performance.

## Classes

### BaseScraper
- The parent class that initializes common attributes such as the base URL and output folder.

### LinkFinder (inherits from BaseScraper)
- Extracts all valid links from the base URL using `BeautifulSoup`.

### LinkFetcher (inherits from BaseScraper)
- Fetches and saves the HTML content of each link to the output folder.

### LinkScraper (inherits from LinkFinder and LinkFetcher)
- Combines the functionalities of `LinkFinder` and `LinkFetcher`.
- Manages the scraping process using multithreading.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AmirRghp/multithreading-web-scraper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd multithreading-web-scraper
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Update the `base_url` and `output_folder` variables in the `if __name__ == '__main__':` section of the script.

2. Run the script:
   ```bash
   python scraper.py
   ```

3. The scraped HTML files will be saved in the specified output folder.

## Dependencies

- `requests`: For sending HTTP requests.
- `beautifulsoup4`: For parsing and extracting links from HTML content.
- `concurrent.futures`: For multithreaded link processing.

## Notes

- Ensure you have appropriate permissions to scrape the website's content.
- Be mindful of the website's `robots.txt` and terms of service.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests to contribute to this project.

---

Happy Scraping!
