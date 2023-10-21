import os
import sys
sys.path.insert(1,"D:\\End to end project\\ML Project\\src\\ML Project")
import logger as lo
import exception as ex
import utils as ut
import pandas as pd
from sklearn.model_selection import train_test_split


from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df=ut.read_sql_data()
            ### Reading data
            lo.logging.info("Reading completed mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            lo.logging.info("Data Ingestion is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path


            )


        except Exception as e:
            raise ex.CustomException(e,sys)
