import pandas as  pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def get_pegi(name):
    response = requests.get(f'https://pegi.info/search-pegi?q={name}')
    response.status_code 
    soup = BeautifulSoup(response.content,'html.parser')
    result = soup.find_all("div", class_="page-content")
    
    r = result[0].find("div",class_= "age-rating")
    pegi_img = r.find("img").get("src")
    num = pegi_img.split('/')
    
    pegi = num[len(num)-1].split('.')[0]
    return  pegi
