from flask_restful import Resource, Api

api = Api(app)


class Movies(Resource):
    def get(self):
        return

api.add_resource(Movies, '/movies')
