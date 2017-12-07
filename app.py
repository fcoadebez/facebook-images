from flask import Flask
from FacebookScraper import FacebookScraper

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/scrape/<page>/<folder>')
def scrape(page, folder):
    fbUrl = 'https://www.facebook.com/pg/' + page
    myScraper = FacebookScraper(fbUrl, folder)
    myScraper.scrape()

    return 'Les photos de la page ' + fbUrl + ' ont été téléchargées dans le dossier ' + folder