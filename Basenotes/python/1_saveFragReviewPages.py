import requests 
from bs4 import BeautifulSoup 
import datetime as dt
import time as tm
from random import randint

session = requests.Session() 

for i in range(1):
    d = dt.datetime.now()
    page = 'http://www.basenotes.net/fragrancereviews/page/' + str(i)
    r = session.get(page, timeout=20)
    o = open("Page"
            + str(i)
            + "_"
            + d.strftime("%m") 
            + d.strftime("%d") 
            + d.strftime("%y")
            + "_"
            + d.strftime("%H")
            + d.strftime("%M")
            + d.strftime("%S")
            + '.html', 'w')
    o.write(r.content)
    o.close()
