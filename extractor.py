import requests
from bs4 import BeautifulSoup
from newspaper import Article

def get_article_urls(base_url):
    """
    Extract article URLs using general patterns.
    """
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # General patterns for extracting links
    possible_article_links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        text = a_tag.get_text().strip().lower()

        # Heuristics to identify article links
        if 'article' in href or 'news' in href or 'story' in href or '202' in href:  # Common keywords in news URLs
            if not href.startswith('http'):
                href = base_url + href  # Handle relative URLs
            possible_article_links.append(href)

    return list(set(possible_article_links))

def extract_article_content(url):
    """
    Extract the main content from a news article using Newspaper3k.
    """
    article = Article(url)
    try:
        article.download()
        article.parse()
    except Exception as e:
        print(f"Newspaper3k failed for {url}, falling back to manual extraction: {e}")
        return fallback_content_extraction(url)

    return article.title, article.text

def fallback_content_extraction(url):
    """
    Use BeautifulSoup to extract content if Newspaper3k fails.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Attempt to find the largest content block
    paragraphs = soup.find_all('p')
    content = ' '.join([p.get_text() for p in paragraphs if len(p.get_text()) > 20])
    title = soup.title.string if soup.title else "No Title Found"

    return title, content
