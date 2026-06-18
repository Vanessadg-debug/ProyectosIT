
import pandas as pd
import os
import sys

#Declaracion de Variables
data_list: list[str]=['date','campaign','channel','impressions','total_click','spend','video_views','conversion']
current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir,"assets","hojatest.xlsx")

try:
    data=pd.read_excel(file_path, sheet_name='TC12C')
    
    if set(data_list).issubset(data.columns):
        if data.columns.str.contains(r'\.\d+$').any():
         duplicated= set(data.columns)-set(data_list)
         dup_list=[]
         for item in duplicated:
            dup_list.append(item.split('.')[0])
         print(f"Los siguientes datos se encuentran duplicados {dup_list}")
         sys.exit(0) 
        else:
         print("Tus datos estan compeltos")
         data.info()

    elif len(set(data_list).intersection(data.columns)) / len(data_list) > 0:
       missing_data= set(data_list)-set(data.columns)
       print(f"Error critico: faltan los siguientes datos {missing_data}")
       data.info()
       sys.exit(1)

    elif data.columns.str.startswith('Unnamed').all():
     
        found=False
        header=0 
        print("elif starts")  
        for index,row in data.iterrows():
             
            if len(set(data_list).intersection(row.values)) / len(data_list) > 0.5:
             header = index+1
             found=True
             break   
        if found:                      
            data=pd.read_excel(file_path, sheet_name='TC12C',header=header) 
            if set(data_list).issubset(data.columns):
                if data.columns.str.contains(r'\.\d+$').any():
                    duplicated= set(data.columns)-set(data_list)
                    dup_list=[]
                    for item in duplicated:
                        dup_list.append(item.split('.')[0])
                    print(f"Los siguientes datos se encuentran duplicados {dup_list}")
                    sys.exit(0) 
                else:
                    print("Tus datos estan compeltos")
                    data.info()
            else:
                missing_data= set(data_list)-set(data.columns)
                print(f"Error critico: faltan los siguientes datos {missing_data}")
                sys.exit(1)
        else:
            print(f"Error critico:no se encontró ninguna fila con suficientes encabezados. Revisa tu archivo.")
            sys.exit(1)
    else:
        if len(set(data_list).intersection(data.columns)) / len(data_list) == 0:
            missing_data= set(data_list)-set(data.columns)
            print(f"Error critico: faltan los siguientes datos {missing_data}")
            sys.exit(1)
         
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


