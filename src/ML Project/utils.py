import os
import sys
sys.path.insert(1,"D:\\End to end project\\ML Project\\src\\ML Project")
import logger as lo
import exception as ex
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')


def read_sql_data():
    lo.logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        lo.logging.info("Connection Established", mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df
    

    except Exception as ex:
        raise ex.CustomException(e,sys)
