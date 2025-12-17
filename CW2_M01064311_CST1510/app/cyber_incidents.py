import pandas as pd 
import sqlite3


def migrate_cyber_incidents(conn):
    path='DATA/cyber_incidents.csv'
    df = pd.read_csv(path)
    print(df.head())
    df.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print('Data Loaded Successfully')

def get_all_cyber_incidents(conn):
    sql='Select * from cyber_incidents'
    data=pd.read_sql(sql, conn)
    return data
