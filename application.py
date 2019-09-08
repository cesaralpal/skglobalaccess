from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

temperatura = "null"
parser = reqparse.RequestParser()

class HelloWorld(Resource):
    def get(self):
        return {'mensaje': 'la cagas morro'}

class sigFoxPost(Resource):
    def post(self):
            parser.add_argument('clave', type=str)
            args = parser.parse_args()
            return { 'echo':args['clave']}

class sigFoxGet(Resource):
    def get(self):
        parser.add_argument('id', type=str)
        parser.add_argument('time', type=str)
        parser.add_argument('data', type=str)
        args = parser.parse_args()
        temperatura = bytes.fromhex(args['data']).decode('utf-8')
        return { 'echo':args['data']}

class Temperatura(Resource):
    def get(self):
        return {"la temperatura es"+temperatura}

class sigFoxPostGet(Resource):
    def post(self):
        parser.add_argument('clave', type=str)
        args = parser.parse_args()
        return { 'echoPost':args['clave']}

    def get(self):
        parser.add_argument('clave', type=str)
        args = parser.parse_args()
        return { 'echoGet':args['clave']}


api.add_resource(HelloWorld, '/')
api.add_resource(sigFoxPost,'/sigFoxPost')
api.add_resource(sigFoxGet,'/sigFoxGet')
api.add_resource(sigFoxPostGet,'/sigFoxPostGet')
api.add_resource(Temperatura,'/temp')

if __name__ == '__application__':
    app.run(debug=True)

