from bs4 import BeautifulSoup
import urllib3
from urllib3.contrib.appengine import AppEngineManager

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = AppEngineManager()
pagina = http.request('GET','http://www.iaexpert.com.br')
pagina2 = http.request('GET','https://www.iaexpert.com.br')

pagina.status

pagina.data

