from config import app, api
from api import URLS, URL

# Endpoints and resources
api.add_resource(URLS, '/api/shortener/<short_url>', endpoint='urls')
api.add_resource(URL, '/api/shortener', endpoint='url')

# Provide run environment
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
