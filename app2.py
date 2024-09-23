from src.constants import ROW_DATA_PATH,PROCESSED_DATA_PATH,PROCESSED_FILE_PREFIX,MAIN_DATA_SET_NAME
from src.utils.generate_dataset import DataIngest
import os,ast
import pandas as pd

def create_data_set():
     dataingest_obj = DataIngest(ROW_DATA_PATH , PROCESSED_DATA_PATH ,PROCESSED_FILE_PREFIX,MAIN_DATA_SET_NAME)
    
     xlsx_files = [f for f in os.listdir(ROW_DATA_PATH) if f.endswith('.xlsx')]
     print(xlsx_files)
     for file in xlsx_files:
        dataingest_obj.restructure_data(file)     
     dataingest_obj.create_main_dataset()               

if __name__ =="__main__":
     print("main")
     create_data_set()
    