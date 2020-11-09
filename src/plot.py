import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

def df_plot(data):
 data = pd.read_csv('./data/data.csv)

  sns_plot = sns.countplot(y=data.pegi, hue=data.Year, palette="Blues")

  sns_plot.figure.savefig("./image/year_and_pegi.jpg", dpi=1000)



  
  
  p = sns.countplot(y=data.Genre, hue=data.pegi, palette="Blues")
  p.figure.savefig("./image/genre_and_pegi.jpg", dpi=1000)
  
  


 # pair = sns.pairplot(data=data, plot_kws={"size": 1})
  #pair.figure.savefig("./image/pair.jpg", dpi=1000)