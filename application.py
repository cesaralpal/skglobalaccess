from flask import Flask
import time
from datetime import datetime
from flask_restful import Resource, Api, reqparse,request
import gc
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

temperaturas = []


def lee_temperaturas(lista):
    return lista


class HelloWorld(Resource):
    def get(self):
        return {'mensaje': 'Bienveido a Global Data Access'}

class sigFoxPost(Resource):
    def post(self):
            parser.add_argument('clave', type=str)
            args = parser.parse_args()
            return { 'echo':args['clave']}

class sigFoxGet(Resource):
    def get(self):
        parser.add_argument('id', type=str)
        parser.add_argument('time', type=int)
        parser.add_argument('data', type=str)
        args = parser.parse_args()
        fecha = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(args['time']))
        temperatura = bytes.fromhex(args['data']).decode('utf-8')
        device = args['id']
        global temperaturas
        temperatura_actual = {
            'id':device,
            'temperatura':temperatura,
            'fecha':fecha
        }
        temperaturas.append(temperatura_actual)

        print("La temperatura es"+ temperatura)
        print("La fecha es" + fecha)
        print("Dispositivo" + device)
        
        return { 'echo':temperaturas}

class Temperatura(Resource):
    def get(self):
        global temperaturas
        return temperaturas





api.add_resource(HelloWorld, '/')
api.add_resource(sigFoxPost,'/sigFoxPost')
api.add_resource(sigFoxGet,'/sigFoxGet')
api.add_resource(Temperatura,'/temp')

if __name__ == '__main__':
    app.run(debug=True)

