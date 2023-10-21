import sys
sys.path.insert(1,"D:\\End to end project\\ML Project\\src\\ML Project")
sys.path.insert(1,"D:\\End to end project\\ML Project\\src\\ML Project\\components")
import logger as lo
import exception as ex
import data_ingestion as dt




if __name__=="__main__":
    lo.logging.info("The execution has started")

    try:
        data_ingestion=dt.DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        lo.logging.info("Custom Exception")
        raise ex.CustomException(e,sys)