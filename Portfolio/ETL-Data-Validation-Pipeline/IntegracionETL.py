
import pandas as pd
import  os
import sys

#Declaracion de Variables
data_list: list[str]=['date','campaign','channel','impressions','total_click','spend','video_views','conversion']
current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir,"assets","hojatest.xlsx")

try:
    data=pd.read_excel(file_path, sheet_name='TC02')
    
    for index,row in data.iterrows():
        if set (data_list).issubset(row):
            header=index+1
            break
    print(header)

    data=pd.read_excel(file_path, sheet_name='TC02',header=header)
       
    if set(data_list).issubset(data.columns):
    
            if data.duplicated().any():
              print("Tus datos estan compeltos pero tienes duplicados revisalos")
              sys.exit(1)
            else:
                print("Tus datos estan compeltos")
                data.info()

    else:
        missing_data= set(data_list)-set(data.columns)
        print(f"Error critico, faltan los siguientes datos {missing_data}")

except FileNotFoundError:
    print(f" Oops! The file dos not exist in {file_path}")
    sys.exit(1)

#data=data.loc[:,~data.columns.str.startswith('Unnamed')]
#data.drop(columns=data.columns[data.columns.str.startswith('Unnamed')])
#print(data) imprime los datos de la hoja de la hoja que se subio
#data.info() imprime que tipo de valores subi por cada columna es decir int64, channel str,date tipo datetime ect


"""
 transformando los datos de lectura al valor que debe corresponder de cada uno
data['date'] = pd.to_datetime(file_path['date'])
data['campaign'] = file_path['campaign'].astype('string')
data['channel'] = file_path['channel'].astype('string')
data['impressions'] = file_path['impressions'].astype('int64')
data['total_click'] = file_path['total_click'].astype('int64')
data['spend'] = file_path['spend'].astype('float64')
data['video_views'] = file_path['video_views'].astype('int64')
data['conversion'] = file_path['conversion'].astype('int64')

try:
 if date =! AAAA-MM-DD"""


