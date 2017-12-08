from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from FacebookScraper import FacebookScraper

mongoClient = MongoClient()
db = mongoClient.fbscrape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/scrape/<page>/<folder>')
def scrape(page, folder):
    fbUrl = "https://www.facebook.com/pg/" + page
    myScraper = FacebookScraper(fbUrl, folder)
    myScraper.scrape()

    return "Les photos de la page " + fbUrl + " ont été téléchargées dans le dossier " + folder


@app.route('/results')
def results():
    dbResults = dumps(db.fb_images.find())

    return dbResults