from FacebookScraper import FacebookScraper
import argparse

parser = argparse.ArgumentParser('Facebook Images')
parser.add_argument('-u', '--url')
parser.add_argument('-f', '--folder')

args = parser.parse_args()

fbUrl = str(args.url)
destFolder = str(args.folder)

myScraper = FacebookScraper(fbUrl, destFolder)
myScraper.scrape()