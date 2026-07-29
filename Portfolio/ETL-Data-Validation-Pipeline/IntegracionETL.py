
import pandas as pd
import os
import sys
from collections import Counter

data_list: list[str]=['date','campaign','channel','impressions','total_click','spend','video_views','conversion']

def load_sheet_data(file_name,sheet_name,rows):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir,"assets",file_name)
    data=pd.read_excel(file_path, sheet_name=sheet_name,header=None, nrows=rows)

    return data
#data=load_sheet_data("hojatest.xlsx", "TC25", 50)

def read_header(data):
    header_found=False
    coincidencia=0
    max_coincidencia=0
    header=0

    for index,row in data.iterrows():
        dato = [str(elemento).lower().strip() for elemento in row.values]
        coincidencia = (len(set(data_list).intersection(dato)) / len(data_list))*100
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
    if not header_found:
        pass
        
    return header, header_found,max_coincidencia
#header,header_found,max_coincidencia=read_header(data)
#print(f" valor de Header found {header_found}")
#print(f"posicion de header {header}")
#print(f"Valor de max coincidencia {max_coincidencia}")
#header_list= data.iloc[header].tolist()

#data.info()
#print (f"El valor de data transformado a lista es {header_list}")

def header_filter(data):
    is_clean=True
    trash_data=[]
    clean_data=[]
    for value in data:

        if pd.isna(value):
            pass
        else:
            dato=str(value).lower().strip() 
            if  dato in data_list:
               clean_data.append(dato)
            else:
                trash_data.append(dato)
                
    if trash_data:
        is_clean=False

    return is_clean,trash_data,clean_data
#is_clean,trash_data,clean_data=header_filter(header_list)
#print(f"Valor de is clean {is_clean}")
#print(f"Valor de trash data {trash_data}")
#print(f"Valor de clean data lista {clean_data}")

#print(f"Valor de clean data lista entrando a validacion de duplicados{clean_data}")

def missing_header(clean_data):
    missing_data=False
    missing=set(data_list) - set(clean_data)
    if missing:
        missing_data=True
        
    return  missing_data,missing
#missing_data,missing=missing_header(clean_data)
#print(f"Faltan los siguientes datos {missing}")

def duplicated(clean_data):
    is_duplicated=False
    conteo=Counter(clean_data)
    dup_list=[]
    
    for elemento,cantidad in conteo.items():
        if cantidad >1:
            dup_list.append(elemento)
            is_duplicated=True
    return is_duplicated, dup_list

#is_duplicated,dup_list=duplicated(clean_data)
#print(f"Valor de si es duplicados boleano es {is_duplicated}")
#print(f"Valor de cuantos hay duplicados en la lista es {dup_list}")


def orquestador(file_name,sheet_name,rows):
    data_sheet=load_sheet_data(file_name,sheet_name,rows)
    header, header_found,max_coincidencia=read_header(data_sheet)

    if header_found:
        header_list= data_sheet.iloc[header].tolist()
        is_clean,trash_data,clean_data=header_filter(header_list)
        missing_data,missing=missing_header(clean_data)
        is_duplicated,dup_list=duplicated(clean_data)
        return header_list,is_clean,trash_data,clean_data,missing_data,missing,is_duplicated,dup_list
    else:
        missing_data,missing=missing_header([])
        return missing_data,missing
    
final_data06=orquestador("hojatest.xlsx", "TC06", 50)    
final_data07=orquestador("hojatest.xlsx", "TC07", 50)    

print(f"Datos finales de TC06 {final_data06}")
print(f"Datos finales DE TC07 {final_data07}")

""""
try:         
except FileNotFoundError:
    print(f" Oops! The file dos not exist in {file_path}")
    sys.exit(1)
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
data['conversion'] = file_path['conversion'].astype('int64') if date =! AAAA-MM-DD

"""
