from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

class Hello(Resource):
    def get(self,name):
        
        # COD3 here LIKE db QUERIES
        
        return {"hello":" kala kuta"}
    
api.add_resource(Hello,'/hello/')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)