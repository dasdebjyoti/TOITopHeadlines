# This program scrapes a web page from Times of India to extract
# top headlines and write it to a JSON file in Google Drive.
# Author: Debjyoti Das

import requests
import datetime
import json
from bs4 import BeautifulSoup

# Prepare file location
import os
from google.colab import drive
strDriveMountLoc = '/content/drive'
strDriveTargetLoc = "/content/drive/My Drive/WebScrape/DataNewsScrapeTOI"
# Mount Google Drive
drive.mount(strDriveMountLoc)
# Create a folder in the root directory
!mkdir -p "/content/drive/My Drive/WebScrape/DataNewsScrapeTOI"

def toi_topheadlines():
  # Generate output filename based on the date and time
  dt = datetime.datetime.now()
  filename = "toi_topheadlines" + dt.strftime("%Y%m%d%H%M%S") + ".json"

  url = "https://timesofindia.indiatimes.com/home/headlines"
  page_request = requests.get(url)
  page_content = page_request.content
  soup = BeautifulSoup(page_content,"html.parser")

  count = 1
  txtscraped = ""
  headlines = []

  for divtag_c02 in soup.find_all('div', {'id': 'c_02'}):
    for divtag_0201 in divtag_c02.find_all('div', {'id': 'c_0201'}):
      divtag_hwdt1 = divtag_0201.find('div', {'id': 'c_headlines_wdt_1'})
      for divtag_topnl in divtag_hwdt1.find_all('div',
       {'class': 'top-newslist'}):
        for ultag in divtag_topnl.find_all('ul',{'class': 'clearfix'}):
          for litag in ultag.find_all('li'):
            for spantitle in litag.find_all('span', {'class': 'w_tle'}):
              href = spantitle.find('a')['href']
              if href.find("/", 0) == 0:
                href = "https://timesofindia.indiatimes.com" + href
                print(str(count) + ". " + spantitle.find('a')['title'] +
                      " - " + href)
                thisheadline = {
                    "sn": count,
                    "title": spantitle.find('a')['title'],
                    "href": href
                }
                headlines.append(thisheadline)

                count = count + 1

  with open(strDriveTargetLoc + '/' + filename, "a") as f:
    f.write(json.dumps(headlines, indent=2))

if __name__ == "__main__":
  toi_topheadlines()

print("\n" + "end")
