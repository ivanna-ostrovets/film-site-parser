from flask import Flask
from flask_restful import Resource, Api

import requests

app = Flask(__name__)
api = Api(app)

api_key = "b4cb68303a91f7b393e47305973fe19e"
query = "all"

url = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}".format(api_key, query)

class Movies(Resource):
    def get(self):
        result = requests.get(url)
        return result.json()

api.add_resource(Movies, '/movies')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
