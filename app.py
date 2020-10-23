from flask import Flask, request, jsonify
import pymongo
import urllib

app = Flask(__name__)


MONGO_URI = "mongodb+srv://Dhrupa:"+ urllib.parse.quote("Dhrupa@337")+ "@cluster0.qfy6s.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_URI)
db = client.test


@app.route('/create_cart')
def create_cart():
    count = len(db.collection_names())
    db["cart_"+str(count)]
    return "Cart successfully created"


@app.route('/get_item/<id>', methods=['GET'])
def get_item(id):
    col = db['cart_'+str(id)]
    output = []
    for s in col.find():
        output.append({'Name': s['Name'], 'Price': s['Price'], 'Ingredients':s['Ingredients']})
    return jsonify({'result': output})


@app.route('/add_item/<id>', methods=['GET','POST'])
def add_item(id):
    name = request.json['Name']
    price = request.json['Price']
    igd = request.json['Ingredients']
    x = db['cart_' + str(id)].insert({'Name': name, 'Price': price, 'Ingredients': igd})
    return "item got successfully added to cart"


@app.route('/delete_item/<id>', methods=['GET','POST'])
def delete_item(id):
    name = request.json['Name']
    col = db['cart_' + str(id)]
    col.delete_one({'Name':name})
    return "Item got deleted successfully from the cart"

if __name__ == '__main__':
    app.run(debug=True)
