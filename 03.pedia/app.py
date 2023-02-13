from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# library
import requests
from bs4 import BeautifulSoup

# DB
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:test@cluster0.dmaafdb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.test

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give'] 
    comment_receive = request.form['comment_give'] 
    star_receive = request.form['star_give'] 

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']
    ogdesc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title' : ogtitle,
        'desc' : ogdesc,
        'image' : ogimage,
        'star' : star_receive,
        'comment' : comment_receive
    }

    db.movies.insert_one(doc)
    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    all_movies = list(db.movies.find({}, {'_id':False}))
    return jsonify({'result' : all_movies})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)