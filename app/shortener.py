class URL_Shortener:
    # Dictionary database for mapping of long and short link
    url_map = {
        "www.google.com": "99"
    }
    # assuming initial ID is 1
    id = 1

    def shorten_url(self, original_url):
        print("[DEBUG]", self.url_map)
        # if url is already present
        if original_url in self.url_map:
            old_id = self.url_map[original_url]
            shorten_url = old_id
        else:
            self.url_map[original_url] = str(self.id)
            shorten_url = self.id
            self.id += 1

        return str(shorten_url)
