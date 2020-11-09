import pandas as  pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from src.get_pegi import get_pegi 
from src.cleaning import *
from src.plot import *

#create_data()


df = pd.read_csv('./data/data.csv')
print(df)


df_plot(df)

