import pandas as pd

from sqlalchemy import create_engine
from time import time


engine = create_engine('postgresql://user:user@pgdatabase:5432/airbnb')

engine.connect()


df_lookup = pd.read_csv('reviews.csv')
df_lookup.dropna(inplace= True)
df_lookup['date'] = pd.to_datetime(df_lookup['date'])
df_lookup.head(0).to_sql(name= 'reviews', con= engine, if_exists= 'fail')
df_lookup.to_sql(name = 'reviews',con = engine,if_exists = 'replace')



df_lookup = pd.read_csv('reviews_details.csv')
df_lookup.dropna(inplace= True)
df_lookup['date'] = pd.to_datetime(df_lookup['date'])
df_lookup.head(0).to_sql(name= 'reviews_details', con= engine, if_exists= 'fail')
df_lookup.to_sql(name = 'reviews_details',con = engine,if_exists = 'replace')



df_lookup = pd.read_csv('listings.csv')
df_lookup.drop(columns='neighbourhood_group',inplace=True)
df_lookup.dropna(inplace=True)
df_lookup['room_type'] = df_lookup['room_type'].astype('category')
df_lookup.head(0).to_sql(name= 'listings', con= engine, if_exists= 'fail')
df_lookup.to_sql(name = 'listings',con = engine,if_exists = 'replace')





df_iter = pd.read_csv("calendar.csv" ,iterator=True,chunksize=200000)
df=next(df_iter)
df.dropna(inplace= True)
df.reset_index(inplace= True)
df.drop(columns = "index", inplace=True)
df['date'] = pd.to_datetime(df['date'])
df['price']  = df['price'].str.replace("$","")
df['price']  = df['price'].str.replace(",","")
df['price'] = df['price'].astype('float')


df.head(0).to_sql(name = 'calender',con = engine,if_exists = 'fail')


df.to_sql(name = 'calender',con = engine,if_exists = 'append')
count = 2
while True:
    tstart = time()
    df=next(df_iter)
    df.dropna(inplace= True)
    df.reset_index(inplace= True)
    df.drop(columns = "index", inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['price']  = df['price'].str.replace("$","")
    df['price']  = df['price'].str.replace(",","")
    df['price'] = df['price'].astype('float')
    
    df.to_sql(name = 'calender',con = engine,if_exists = 'append')
    tend = time()
    print(f'inserted chunk ({count}).. time spent:{tend-tstart:.3f}')
    count = count + 1

