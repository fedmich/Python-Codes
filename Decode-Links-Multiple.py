import requests
import hashlib
import os
from bs4 import BeautifulSoup

class ShortLinkDecoder:
    def __init__(self, cache_dir='./decoded/'):
        self.CACHE_DIR = cache_dir
        self.cache = {}
        self.create_cache_dir()
        self.load_cache()

    def get_md5(self, url):
        return hashlib.md5(url.encode()).hexdigest()

    def load_cache(self):
        if os.path.exists(self.CACHE_DIR):
            self.cache = {
                filename[:-4]: open(os.path.join(self.CACHE_DIR, filename)).read().strip()
                for filename in os.listdir(self.CACHE_DIR) if filename.endswith('.txt')
            }

    def create_cache_dir(self):
        try:
            os.makedirs(self.CACHE_DIR, exist_ok=True)
        except Exception as e:
            print(f"Warning: Unable to create cache directory. {e}")

    def save_to_cache(self, url, final_url):
        md5 = self.get_md5(url)
        with open(os.path.join(self.CACHE_DIR, f"{md5}.txt"), 'w') as f:
            f.write(final_url)

    def get_linkedin_url(self, short_link):
        response = requests.get(short_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        link = soup.find('a', {'data-tracking-control-name': 'external_url_click'})
        return link['href'] if link else None

    def decode_short_link(self, url):
        md5 = self.get_md5(url)
        
        if md5 in self.cache:
            return self.cache[md5]

        final_url = self.get_linkedin_url(url) if 'lnkd.in' in url else requests.get(url, allow_redirects=True).url

        if final_url:
            self.cache[md5] = final_url
            self.save_to_cache(url, final_url)
        
        return final_url

    def decode_multiple_links(self, urls):
        return {url: self.decode_short_link(url) for url in urls}

# Example usage
if __name__ == "__main__":
    decoder = ShortLinkDecoder()
    links = [
        "https://lnkd.in/gqTsN8VD",
        "https://lnkd.in/gsP_s6hh",
        "https://lnkd.in/gWn7BKuq",
        "https://lnkd.in/gW67mJD4"
    ]
    decoded_links = decoder.decode_multiple_links(links)
    for short_link, final_url in decoded_links.items():
        print(f"{short_link} -> {final_url}")
