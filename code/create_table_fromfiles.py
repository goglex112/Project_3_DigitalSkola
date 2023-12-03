import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import URL


url_object = URL.create(
    "postgresql",
    username="postgres",
    password="password",  # plain (unescaped) text
    host="localhost",
    database="test",
)

engine = create_engine(url_object)

df = pd.read_csv(r'D:\OneDrive - Bina Nusantara University\Desktop\Self Learning\Data Engineer\Week V\Project 3\source\region.csv')

df.to_sql(name='region', con=engine, if_exists='replace')