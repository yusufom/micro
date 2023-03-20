from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate, MigrateCommand
from dataclasses import dataclass
import requests
from producer import publish


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS()

db = SQLAlchemy(app)



migrate = Migrate(app, db)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)


    UniqueConstraint('user_id', 'product_id', name='user_product_unique')




@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://127.0.0.1:8000/users/')
    json = req.json()
    

    try:
        product_user = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(product_user)
        db.session.commit()
        publish('product_liked', id)
    except:
        abort(400, 'You already liked this product')


    return jsonify({
            'message':'success'
        })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8001')