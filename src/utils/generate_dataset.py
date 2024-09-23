
import os,ast
import pandas as pd
class DataIngest:

    def __init__(self,row_data_path,processed_data_path,processed_file_prefix,main_data_set_name):
          self.row_data_path =  row_data_path 
          self.processed_data_path = processed_data_path
          self.processed_file_prefix=processed_file_prefix
          self.main_data_set_name=main_data_set_name

     
    def restructure_data(self,file_name):
          
            dataset_path = f"{self.row_data_path}\\{file_name}"
            processed_file_name = f"{self.processed_file_prefix}_{file_name}"
            df=pd.read_excel(dataset_path,engine='openpyxl')
            print(df.columns)
            data_list=[]
            df_list=[]
            new_dict_list=[]
            for column in df.columns:
                    if column in ['car_links']:
                        continue
                    content_list=list(df[column])
                    dict_list=[ast.literal_eval(item) for item in  content_list]
                    if column in ['new_car_detail']:
                        data_list.extend(dict_list)
                        data_list=[{k:v for k,v in item.items() if k != 'trendingText'} for item in data_list]
                        result_df=pd.DataFrame(data_list)
                        df_list.append(result_df) 
                    if column in ['new_car_overview','new_car_specs']:
                        overview_dict_list=[item.get('top','') for item in dict_list]
                        #print(overview_dict_list)
                        new_dict_list=[{list_item['key']:list_item['value'] for list_item in item} for item in overview_dict_list]
                        result_df=pd.DataFrame(new_dict_list)
                        df_list.append(result_df) 
                    if column in ['new_car_feature']:
                        feature_dict_list=[item.get('top','') for item in dict_list]
                        content_list =[[item.get('value','') for item in list_item]  for list_item in feature_dict_list]
                        new_dict_list=[{'top_features':item} for item in content_list]   
                        result_df=pd.DataFrame(new_dict_list)
                        df_list.append(result_df) 
            if df_list:
                #print(len(df_list))        
                combined_df = pd.concat(df_list, axis=1)
                combined_df.to_excel(f"{self.processed_data_path}\\{processed_file_name}")
    
    def create_main_dataset(self):
        df_list=[]
        processed_files = [f for f in os.listdir(self.processed_data_path) if f.endswith('.xlsx')]
        for file in processed_files:
             df=pd.read_excel(f"{self.processed_data_path}\\{file}")
             df_list.append(df)
        if df_list:
             new_df=pd.concat(df_list,ignore_index=True)
             new_df.to_excel(f"{self.processed_data_path}\\{self.main_data_set_name}",index=False)
             
                         
