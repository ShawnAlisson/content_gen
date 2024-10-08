import requests
import json

def post_to_blog(title, content, post_url, api_token):
    """
    Post the summarized content to a blog.
    """
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'title': title,
        'content': content,
        'status': 'publish'
    }

    response = requests.post(post_url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Successfully posted: {title}")
    else:
        print(f"Failed to post: {response.status_code} - {response.text}")
