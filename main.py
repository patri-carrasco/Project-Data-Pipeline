from src.get_reference import get_reference
from src.price_string_to_price_euro import price_string_to_price_euro
from src.update_price_nan import update_price_nan
from src.pounds_euro import pounds_euro
import pandas as pd


reference = []

#leemos el data

data = pd.read_csv('./data/amazon_co-ecommerce_sample.csv')

#Creamos un data nuevo donde solo el manufacturer sea LEGO
n_data = data[data['manufacturer'] == 'LEGO']

#Le añadimos el resto de columnas que vamos a necesitar

lego_data = n_data[['product_name','manufacturer','price','product_description']]

#reiniciamos los indices
lego_data = lego_data.reset_index(drop = True) 


total_null= lego_data['price'].isnull().sum()



#creamos una función donde obtenemos las referencias de los sets de los LEGOS

for string in lego_data.product_name:
  reference.append(get_reference(string))

#añadimos una columna nueva con las referencias nuevas
lego_data['reference'] = reference

#borramos las referencias nulas
lego_data = lego_data[lego_data.reference != '----']



#creamos una función donde pasamos de las libras a euros en decimales

euro = []
for  elem in lego_data.price:
    price =price_string_to_price_euro(elem)
    euro.append(pounds_euro(price))

    
lego_data['euro'] = euro

lego_data = lego_data.reset_index(drop = True) 

indices_nulos =((lego_data.loc[lego_data['euro'] == 0]).index)


print(indices_nulos)


#print(lego_data.loc[lego_data['euro'] == 0])
print(lego_data.iloc[indices_nulos[0]])

#añadimos los datos
lego_data.at[indices_nulos[0], 'euro'] = 10

print(lego_data)
print(lego_data.iloc[indices_nulos[0]])