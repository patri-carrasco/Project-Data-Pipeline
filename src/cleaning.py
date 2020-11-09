
import pandas as  pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from src.get_pegi import get_pegi 


def cleaning(list_string):

  name_list = []
  for elem in list_string:
      elem = elem.replace(':','')
      elem = elem.replace('(', '')
      elem = elem.replace(')', '')
      
      name_list.append(elem)
  return name_list




def create_data():

  #Creamos la base datos de juegos

  data = pd.read_csv('./data/vgsales.csv')

  #Vemos información del data

  print(data.value_counts())

  print(data.Platform.value_counts())

  data_xbox = data[data['Platform'] == 'XOne' ]

  data_xbox = data_xbox[['Name','Platform','Year','Genre','Publisher']]

  data_xbox = data_xbox.reset_index(drop = True) 

  #limpiamos el listado de los nombres del dataset
  name_list = []
  name_list = cleaning(data_xbox.Name)

  #obtenemos los pegi

  
  pegi = []
  for name in name_list:
      try:
          pegi.append(int(get_pegi(name)))
      except Exception:
          pegi.append(0)
  print(pegi)
  data_xbox['pegi'] = pegi
  

 

  data_xbox= data_xbox.drop(data_xbox.loc[data_xbox.pegi==0].index)
  data_xbox = data_xbox.reset_index(drop = True) 



  data_xbox.to_csv('./data/data.csv')

  return(data_xbox)
