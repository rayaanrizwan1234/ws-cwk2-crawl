import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import time
import json
import re

DELAY = 6  # seconds

STOP_WORDS = set([
    "a", "an", "and", "are", "as", "at", "be", "but", "by",
    "for", "if", "in", "into", "is", "it", "no", "not", "of",
    "on", "or", "such", "that", "the", "their", "then", "there",
    "these", "they", "this", "to", "was", "will", "with"
])

# Function to normalize the word by removing punctuation and converting it to lowercase
def normalize_word(word):
    return re.sub(r'\W+', '', word).lower()

# Function to find next page
def next_page(soup, BASE_URL):
    next_page = soup.find('li', class_='next')
    return BASE_URL + next_page.a['href'] if next_page else None

# Function to crawl the website and build the inverted index
def crawl_and_build_index(base_url, index_file):
    page_url = base_url
    '''
    Nested Dictionary
    e.g., {
        "word": {
            "url1": count1,
            "url2": count2,
            ...
        },
        ...
    }
    '''
    inverted_index = defaultdict(lambda: defaultdict(int))
    # Ensure each page is only visited once
    visited_urls = set()

    while page_url:
        print(f"Crawling {page_url}")
        if page_url not in visited_urls:
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract quotes from the page
            quotes = soup.find_all('div', class_='quote')
            for quote in quotes:
                text = quote.find('span', class_='text').get_text()
                words = text.split()
                for word in words:
                    normalized_word = normalize_word(word)
                    if normalized_word and normalized_word not in STOP_WORDS:
                        inverted_index[normalized_word][page_url] += 1
            visited_urls.add(page_url)

        # Find the next page link
        page_url = next_page(soup, base_url)

        # politness window
        time.sleep(DELAY)

    # Save the inverted index to a file
    with open(index_file, 'w') as f:
        json.dump(inverted_index, f, indent=4)
    print(f"Inverted index saved to {index_file}")

    return len(visited_urls)
