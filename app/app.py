from config import app, api
from api import URLS

# Endpoints and resources
api.add_resource(URLS, '/api/test', endpoint='urls')

# Provide run environment
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
