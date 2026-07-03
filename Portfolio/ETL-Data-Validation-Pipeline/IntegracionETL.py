
import pandas as pd
import os
import sys
from collections import Counter
file_name="hojatest.xlsx"
sheet_name="TC09"
rows=50
current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir,"assets",file_name)
data=pd.read_excel(file_path, sheet_name=sheet_name,header=None, nrows=rows)

def read_header(data):
    data_list: list[str]=['date','campaign','channel','impressions','total_click','spend','video_views','conversion']

    header_found=False
    coincidencia=0
    max_coincidencia=0
    header=0

    for index,row in data.iterrows():
        coincidencia = (len(set(data_list).intersection(row.values)) / len(data_list))*100
        if coincidencia>0:
            if coincidencia==100:
                header_found=True
                header=index
                max_coincidencia=coincidencia
                break
            else:
                if coincidencia > max_coincidencia:
                 max_coincidencia=coincidencia
                 header_found=True
                 header=index   
        else:
            print("No se encontro ninguna coincidencia de header") 
            sys.exit(1)
        
    return header, header_found,max_coincidencia
header,header_found,max_coincidencia=read_header(data)
print(f" valor de Header found {header_found}")
print(f"posicion de header {header}")
print(f"Valor de max coincidencia {max_coincidencia}")

data= pd.read_excel(file_path, header=None, skiprows=header, nrows=1).iloc[0].tolist()
#data=pd.read_excel(file_path, sheet_name=sheet_name,header=header)
#print(header)
#data.info()
print (f"El valor de data transformado a lista es {data}")
def header_filter(data):
    is_clean=True
    trash_data=[]
    clean_data=[]
    for value in data:
        if  value in data_list:
            clean_data.append(value)
        else:
            trash_data.append(value)
    
    if trash_data:
        is_clean=False

    return is_clean,trash_data,clean_data
is_clean,trash_data,clean_data=header_filter(data)
print(f"Valor de is clean {is_clean}")
print(f"Valor de trash data {trash_data}")
print(f"Valor de clean data lista {clean_data}")

print(f"Valor de clean data lista entrando a validacion de duplicados{clean_data}")
def duplicated(clean_data):
    is_duplicated=False
    conteo=Counter(clean_data)
    dup_list=[]
    
    for elemento,cantidad in conteo.items():
        if cantidad >1:
            dup_list.append(elemento)
            is_duplicated=True
    return is_duplicated, dup_list

is_duplicated,dup_list=duplicated(clean_data)
print(f"Valor de si es duplicados boleano es {is_duplicated}")
print(f"Valor de cuantos hay duplicados en la lista es {dup_list}")

""""
try:
    
    
    if set(data_list).issubset(data.columns):
        #if data.columns.str.contains(r'\.\d+$').any():
            duplicated= set(data.columns)-set(data_list)
            dup_list=[]
            for item in duplicated:
                dup_list.append(item.split('.')[0])
            print(f"Los siguientes datos se encuentran duplicados {dup_list}")
            sys.exit(0)

        else:
            trash_columns = set(data.columns) - set(data_list)
            lista_basura = list(trash_columns)
            if trash_columns:
             print(f"Se encontraron columas adicionales {trash_columns}, estas seran eliminadas")
             data = data[data_list]
            print("Tus datos estan compeltos")
            data.info()

    elif len(set(data_list).intersection(data.columns)) / len(data_list) > 0:added
       missing_data= set(data_list)-set(data.columns)
       print(f"Error critico: faltan los siguientes datos {missing_data}")
       data.info()
       sys.exit(0)

   # elif data.columns.str.startswith('Unnamed').all():
     
        found=False
        header=0 
         
        for index,row in data.iterrows():
             
            if len(set(data_list).intersection(row.values)) / len(data_list) > 0.5:
             header = index+1
             found=True
             break   
        if found:                      
            data=pd.read_excel(file_path, sheet_name=sheet_name,header=header)

            if set(data_list).issubset(data.columns):
             #   if data.columns.str.contains(r'\.\d+$').any():
                    duplicated= set(data.columns)-set(data_list)
                    dup_list=[]
                    for item in duplicated:
                        dup_list.append(item.split('.')[0])
                    print(f"Los siguientes datos se encuentran duplicados {dup_list}")
                    sys.exit(0) 
                else:
                    trash_columns = set(data.columns) - set(data_list)
                    lista_basura = list(trash_columns)
                    if trash_columns:
                     print(f"Se encontraron columas adicionales {trash_columns}, estas seran eliminadas")
                     data = data[data_list]
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
print(data) imprime los datos de la hoja de la hoja que se subio
data.info() imprime que tipo de valores subi por cada columna es decir int64, channel str,date tipo datetime ect



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


