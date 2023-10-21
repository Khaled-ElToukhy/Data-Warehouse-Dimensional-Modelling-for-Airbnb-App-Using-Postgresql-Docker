import os
import glob
import psycopg2
import pandas as pd
from sqlalchemy import create_engine , text
from sql_queries import *


engine = create_engine('postgresql://user:user@pgdatabase:5432/airbnb')

engine.connect()


def process_calender():
    df = pd.read_csv("calendar.csv")
    df.dropna(inplace= True)
    df.reset_index(inplace= True)
    df.drop(columns = "index", inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['price']  = df['price'].str.replace("$","")
    df['price']  = df['price'].str.replace(",","")
    df['price'] = df['price'].astype('float')
    return df.to_sql(name = 'calender', con= engine,if_exists="replace")



def process_reviews_details():
    df = pd.read_csv("reviews_details.csv")
    df.dropna(inplace= True)
    df['date'] = pd.to_datetime(df['date'])
    return df.to_sql('reviews_details', con= engine,if_exists="replace")

def process_reviews():
    df = pd.read_csv("reviews.csv")
    df.dropna(inplace= True)
    df['date'] = pd.to_datetime(df['date'])
    return df.to_sql('reviews', con= engine,if_exists="replace")


def process_listings():
    df = pd.read_csv("listings.csv")
    df.drop(columns='neighbourhood_group',inplace=True)
    df.dropna(inplace=True)
    df['room_type'] = df['room_type'].astype('category')
    return df.to_sql('listings', con= engine,if_exists="replace")


