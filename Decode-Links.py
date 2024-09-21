import requests
import hashlib
import os
from bs4 import BeautifulSoup

CACHE_DIR = './decoded/'
cache = {}

def get_md5(url):
    return hashlib.md5(url.encode()).hexdigest()

def load_cache():
    if os.path.exists(CACHE_DIR):
        return {filename[:-4]: open(os.path.join(CACHE_DIR, filename)).read().strip() 
                for filename in os.listdir(CACHE_DIR) if filename.endswith('.txt')}
    return {}

def create_cache_dir():
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        return True
    except Exception as e:
        print(f"Warning: Unable to create cache directory. {e}")
        return False

def save_to_cache(url, final_url):
    md5 = get_md5(url)
    with open(os.path.join(CACHE_DIR, f"{md5}.txt"), 'w') as f:
        f.write(final_url)

def get_linkedin_url(short_link):
    response = requests.get(short_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.find('a', {'data-tracking-control-name': 'external_url_click'})
    return link['href'] if link else None

def decode_short_link(url):
    global cache
    create_cache_dir()  # Attempt to create cache directory, but continue regardless

    cache = load_cache()
    md5 = get_md5(url)
    
    if md5 in cache:
        return cache[md5]

    final_url = get_linkedin_url(url) if 'lnkd.in' in url else requests.get(url, allow_redirects=True).url

    if final_url:
        cache[md5] = final_url
        save_to_cache(url, final_url)
    
    return final_url

'''
# Example usage
short_link = "https://lnkd.in/gsP_####"
destination = decode_short_link(short_link)
print(destination)
'''
