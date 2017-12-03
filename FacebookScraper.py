from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import os

class FacebookScraper:

    def __init__(self, url, folder):
        self.url = url + '/photos/'
        self.folder = folder + '/'

    def scrape(self):
        browser = webdriver.PhantomJS()
        browser.get(self.url)

        html_doc = browser.page_source

        soup = BeautifulSoup(html_doc, "html.parser")

        allImages = soup.find('div', {'id': 'content_container'}).find_all('img')

        for i, img in enumerate(allImages):
            if img.parent.name == 'a':
                imageSource = img['src']
                print(imageSource)
                if not os.path.exists(self.folder):
                    os.makedirs(self.folder)
                urllib.request.urlretrieve(imageSource, self.folder + str(i) + '.jpg')


        browser.close()






