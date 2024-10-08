import json
import time
from extractor import get_article_urls, extract_article_content
from summarizer import summarize_content, translate_content
from publisher import post_to_blog

def process_article(url, publish, post_url, api_token, target_language):
    """
    Extract, summarize, and post the article.
    """
    title, content = extract_article_content(url)
    if not content:
        print(f"No content found for {url}")
        return

    print(f"Summarizing content for: {title}")
    summarized_content = summarize_content(content)

    print(f"Summarized content: {summarized_content}")

    # Translate content if necessary
    translated_content = translate_content(summarized_content, target_language=target_language)

    # Post the translated and summarized content to a blog if publish is true
    if publish:
        post_to_blog(title, translated_content, post_url, api_token)
    time.sleep(2)  # Avoid hitting rate limits

def main():
    # Load configuration from JSON file
    with open('config.json') as config_file:
        config = json.load(config_file)

    websites = config['websites']
    publish = config['publish']
    post_url = config['post_url']
    api_token = config['api_token']
    target_language = config['target_language']

    for base_url in websites:
        print(f"Fetching articles from: {base_url}")
        article_urls = get_article_urls(base_url)
        print(f"Found {len(article_urls)} articles to process from {base_url}.")

        for url in article_urls[:5]:  # Process only the first 5 articles to limit load
            print(f"Processing URL: {url}")
            process_article(url, publish, post_url, api_token, target_language)

# Run the script
if __name__ == "__main__":
    main()
