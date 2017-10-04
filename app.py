from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import  Store, StoreList
from security import authenticate, identity

# flask_restful uses jsonify for dicts automatically

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    # Busca en todos los imports, si hay clases definidas como db.Model

jwt = JWT(app,authenticate,identity) # /auth

#/student/<name>
api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')

api.add_resource(UserRegister,'/register')


# Protects this code to execute if app.py is imported elsewhere
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=80, debug=True)


