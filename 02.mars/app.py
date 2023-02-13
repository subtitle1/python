from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:test@cluster0.dmaafdb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.test

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    doc = {
        'name' : name_receive,
        'address' : address_receive,
        'size' : size_receive,
    }
    
    db.mars.insert_one(doc)
    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    mars_data = list(db.mars.find({}, {'_id':False}))
    return jsonify({'result' : mars_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)