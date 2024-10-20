import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://camo.githubusercontent.com/5b5c039e0e17338e87aa9eaf0026a06f8b9774c8d752415a92e7ba581157abb8/68747470733a2f2f71756f7465732d6769746875622d726561646d652e76657263656c2e6170702f6170693f747970653d686f72697a6f6e74616c267468656d653d7261646963616c"

data = rq.get(url=url)


content = bs(data,'html.parser')

print(content)