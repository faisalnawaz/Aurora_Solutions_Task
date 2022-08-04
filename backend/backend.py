
from flask import Flask

from flask_restful import Api, Resource

app = Flask (__name__) 
api = Api(app)
import os
os.environ['NAME'] = 'Faisal'

class NameAppApi(Resource):
    def get(self):
#       return {"name": name, "test": test}
        prsnl_name = os.environ['NAME']
        return{"name": prsnl_name}
     
#api.add_resource (HelloWorld, "/helloworld/<string:name>/<int:test>");
api.add_resource (NameAppApi, "/");

if __name__ == "__main__":
    app.run()


