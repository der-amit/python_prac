import pandas as pd
from urllib.request import urlretrieve

url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

#urlretrieve is basically a get request
urlretrieve(url,'latitude.xls')

df = pd.read_excel('latitude.xls', sheet_name = None)

#Print sheet names
print(df.keys())

#Access first 5 rows of the first sheet
print(df['1700'].head())