import string


class URL_Shortener:
    # Dictionary database for mapping of long and short link
    url_map = {}
    # taking ID from larger number to get 5-6 digit code
    id = 999999999

    def shorten_url(self, original_url):
        print("[DEBUG]", self.url_map)
        # if url is already present
        if original_url in self.url_map:
            old_id = self.url_map[original_url]
            shorten_url = self.encode(old_id)
        else:
            self.url_map[original_url] = str(self.id)
            shorten_url = self.encode(self.id)
            self.id += 1
        return str(shorten_url)

    def encode(self, hash_id):
        # using more char pool to offer more codes
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

        # encoding plane ID to base 62 number
        base = len(chars)

        result = []
        while hash_id > 0:
            val = hash_id % base
            result.append(chars[val])
            hash_id = hash_id // base

        return "".join(result[::-1])
