# ContentGen

A simple and modular scraper that extracts articles from specified websites, summarizes the content, and optionally publishes it to a blog.

## Features

- Extracts article URLs using general patterns.
- Extracts article content using Newspaper3k and BeautifulSoup.
- Summarizes content using the T5 model from Hugging Face.
- Optionally translates content to a specified language.
- Publishes summarized articles to a blog via an API.

## Requirements

- Python 3.7+
- Libraries: `requests`, `beautifulsoup4`, `newspaper3k`, `transformers`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ShawnAlisson/content_gen.git
   cd content_gen
   ```

2. Install the required packages:
   ```bash
   pip install requests beautifulsoup4 newspaper3k transformers
   ```

## Configuration

Edit the `config.json` file to specify:

- The list of websites to scrape.
- Whether to publish (`publish` option).
- The blog API endpoint (`post_url`).
- Your API token for authentication (`api_token`).
- Target language for translation (`target_language`).

## Usage

Run the scraper using the command:

```bash
python scraper.py
```
