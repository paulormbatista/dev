import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://atos.net/en/solutions/advanced-computing'
 
r = requests.get(url)

print(r.text)
 
