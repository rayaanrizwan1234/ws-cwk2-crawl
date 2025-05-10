# COMP3011: Web Search Tool
## Features

- Crawls [https://quotes.toscrape.com](https://quotes.toscrape.com)
- Builds an inverted index mapping words to the pages and their frequencies
- Skips stop words to improve index quality
- Normalizes all words (removes punctuation, lowercase)
- Saves and loads the index using JSON
- Provides ranked search results using **term frequency**
- Supports interactive command-line menu

---

## Project Structure

| File            | Description |
|------------------|-------------|
| `build.py`       | Crawls the website, builds and saves the inverted index |
| `load.py`        | Loads the `inverted_index.json` file into memory |
| `print.py`       | Prints the inverted index for one or more words |
| `find.py`        | Finds and ranks pages that contain all given search terms |
| `myclient.py`    | Main client interface for all commands |
| `inverted_index.json` | Output file storing the indexed word data |

---

## How to Run

### 1. Install Dependencies

```bash
pip install requests beautifulsoup4
```

### 2. Launch the Client

```bash
python myclient.py
```

### 3. Menu Options

```text
1. Build Inverted Index        → Crawl site and save index
2. Load Inverted Index         → Load from JSON file
3. Print Inverted Index        → Show pages and counts for a word
4. Find Inverted Index         → Rank pages that contain all input words
5. Exit                        → Quit the program
```

You can type either the number or the command name (e.g., `build`, `find good friends`).

---

## Search Ranking Method

The search results are ranked using **term frequency (TF)**:

```
Relevance Score = Sum of the frequency of each query word on that page
```

Pages are sorted in descending order of their score, ensuring that the most relevant results appear first.

---

## Stop Words

The crawler automatically ignores common stop words (like "the", "is", "in", etc.) when building the index. This reduces noise and improves relevance.

---

## Example Usage

```text
> build
Crawling https://quotes.toscrape.com ...
Inverted index saved to inverted_index.json

> load
Inverted index loaded from inverted_index.json

> print world
URL: https://quotes.toscrape.com/page/2/ — Count: 1
URL: https://quotes.toscrape.com/page/4/ — Count: 1

> find good world
Ranked pages:
  URL: https://quotes.toscrape.com/page/2/ — Total Count: 2
```

---

## Technologies Used

- Python 3
- `requests` — for fetching web pages
- `BeautifulSoup` — for HTML parsing
- `json`, `re`, `os`, `time`, `collections` — built-in Python libraries

---

## ✅ Author

**Rayaan**  
University of Leeds  
School of Computing  
COMP3011 – 2024/25
