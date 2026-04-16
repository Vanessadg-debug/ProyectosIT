
"""sqlite3 es la libreria de Python para conectar con DB
En la siguiente linea se establece conexion with my previous DB created"""
conexion = sqlite3.connect('db_data.db')
cursor = conexion.cursor()

#Creando Tabla de colores contaste
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
               id integer primary key autoincrement,
               nombre text,
               puesto text)
''')
