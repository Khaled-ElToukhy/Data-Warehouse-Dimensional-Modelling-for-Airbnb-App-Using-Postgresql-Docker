import pandas as pd



def read_calender(file):
    df = pd.read_csv(file)
    df.dropna(inplace= True)
    df.reset_index(inplace= True)
    df.drop(columns = "index", inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['price']  = df['price'].str.replace("$","")
    df['price']  = df['price'].str.replace(",","")
    df['price'] = df['price'].astype('float')
    return df


def read_reviews(file):
    df = pd.read_csv(file)
    df.dropna(inplace= True)
    df['date'] = pd.to_datetime(df['date'])
    return df



def read_listings(file):
    df = pd.read_csv(file)
    df.drop(columns='neighbourhood_group',inplace=True)
    df.dropna(inplace=True)
    df['room_type'] = df['room_type'].astype('category')
    return df