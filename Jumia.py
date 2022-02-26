#from bs4 import BeautifulSoup
#import requests
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

#jumia_page = requests.get("https://www.jumia.com.gh/laptops/")
#print(jumia_page)
#soup = BeautifulSoup(jumia_page.content, "html.parser")
#laptop = soup.find_all("div", attrs={"class":"info"})
#print(laptop)
#price = laptop.find("div", class_ ="prc")
#print(price)

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

req = Request('https://www.jumia.com.gh/laptops/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")
laptop = soup.find_all("div", class_ ='info')
csvFile = open('jumialaptops.csv', 'w',encoding='utf-8')
csvWriter = csv.writer(csvFile)
for prce in laptop:
    item_list = list()
    title = prce.find('div', class_ = "name").text
    item_list.append(title)
    price = prce.find('div', class_ = "prc").text
    item_list.append(price)
    csvWriter.writerow(item_list)
