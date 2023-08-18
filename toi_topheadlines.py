import requests
from bs4 import BeautifulSoup

def toi_topheadlines():
  url = "https://timesofindia.indiatimes.com/home/headlines"
  page_request = requests.get(url)
  page_content = page_request.content
  soup = BeautifulSoup(page_content,"html.parser")

  count = 1

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
                count = count + 1

if __name__ == "__main__":
  toi_topheadlines()

print("\n" + "end")
