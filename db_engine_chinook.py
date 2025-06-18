#Create an engine to connect to SQLite database
from sqlalchemy import create_engine, inspect, text
import os
import urllib.request
import pandas as pd

#Note: replace blob with raw while pasting the link
url = 'https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite'
filename = 'Chinook_Sqlite.sqlite'

print('Downloading Chinook Database...')
urllib.request.urlretrieve(url, filename)
print(f'Download to: {os.path.abspath(filename)}')

#Create engine
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

#Get table names
inspector = inspect(engine)
table_names = inspector.get_table_names()
print(f"The tables are: \n{table_names}")

#Connection
conn = engine.connect()
rs = conn.execute(text("SELECT * FROM Album"))
df = pd.DataFrame(rs.fetchall())
conn.close()

print(df.head())