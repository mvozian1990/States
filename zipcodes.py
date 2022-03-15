import pandas
from sqlalchemy import create_engine

hostname = "localhost:8889"
uname = "root"
pwd = "root"
dbname = "zipcodes"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=uname, pw=pwd))

tables = pandas.read_csv("/Users/mariana/zip_code_database.csv")

connection = engine.connect()

tables.to_sql('zipcodes', con=engine, if_exists='replace')
connection.close()
print(tables)
