import csv
import sqlite3

base = input("\nIngrese el nombre de la base de datos SQLite: ")
tabla = input("\nIngrese el nombre de la Tabla: ")
salida = base+".csv"

conn = sqlite3.connect(base)
cursor = conn.cursor()
cursor.execute("select * from "+tabla+";")
with open(salida, 'w',newline='', encoding="utf-8") as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)
conn.close()