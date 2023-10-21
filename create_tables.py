import psycopg2
from sqlalchemy import create_engine , text
from sql_queries import create_table_queries, drop_table_queries

url = 'postgresql://user:user@pgdatabase:5432/airbnb'
con = create_engine('postgresql://user:user@pgdatabase:5432/airbnb')



def create_database(url):
    """
    - Creates and connects to the airbnb
    - Returns the connection and cursor to airbnb
    """
    url = 'postgresql://user:user@pgdatabase:5432/airbnb'
    con = create_engine('postgresql://user:user@pgdatabase:5432/airbnb')
    con.connect()
    return con.create_all()


def drop_tables(con):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    with con.connect() as connection:
        for query in drop_table_queries:
            connection.execute(text(query))
        
        
def create_tables(con):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    with con.connect() as connection:
        for query in create_table_queries:
            connection.execute(text(query))
        

def main():
    """
    - Drops (if exists) and Creates the airbnb database. 
    
    - Establishes connection with the airbnb database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database(url)
    
    drop_tables(con)
    create_tables(con)

    con.close()


if __name__ == "__main__":
    main()