from src.constants import DATASET
import os,ast
import pandas as pd
dataset_path = os.path.join("src","repository","row_data","bangalore_cars.xlsx")
df=pd.read_excel(dataset_path,engine='openpyxl')
print(df.columns)
data_list=[]
new_dict_list=[]
for column in df.columns:
    if column in ['new_car_overview']:
        dict_list=[ast.literal_eval(item) for item in  list(df[column])]
        dict_list=[item.get('top','') for item in dict_list]
        #print(dict_list)
        
        if dict_list:

            if column in ['new_car_feature']:
                pass

               # content_list =[item.get('value','') for item in dict_list]
                #new_dict_list=[{'top_features':content_list}]
            else:    
                new_dict_list=[{item[0]['key']:item[0]['value']} for item in dict_list]
        if new_dict_list:
            data_list.append(new_dict_list)
    else:
        data_list.append(df[column])
print("data",data_list)
new_df=pd.DataFrame(data_list)
print(new_df)
df.to_excel("./new_banglore_Cars.xlsx")
