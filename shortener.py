import string
import random

class Shortener:
    def __init__(self):
        self.url_map = {}
    
    def shorten(self, url):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        while True:
            short_url = ''.join(random.choice(chars) for _ in range(6))
            if short_url not in self.url_map:
                self.url_map[short_url] = url
                return short_url
    
    def expand(self, short_url):
        if short_url in self.url_map:
            return self.url_map[short_url]
        else:
            return None
