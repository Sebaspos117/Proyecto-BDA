from multiprocessing import connection
from tkinter import EXCEPTION
import psycopg2

try:
    connection=psycopg2.connect(
       host='localhost',
       user='postgres',
       password='mandril77',
       database='Proyecto'
    )

    connection.autocommit= True

    def insertarDatos(nombreestudiante,segundonombre,correo):
        cursor=connection.cursor()
        query= f"""INSERT INTO bda.student (nombreestudiante,segundonombre,correo) VALUES ('{nombreestudiante}','{segundonombre}','{correo}')"""
        cursor.execute(query)
        cursor.close()

    def crearTabla():
        cursor=connection.cursor()
        query= "CREATE TABLE student(nombreestudiante varchar(30))"
        try:
            cursor.execute(query)
        except:
            print("La tabla student ya existe")
        cursor.close()

    def eliminarTabla():
        cursor=connection.cursor()
        query= "DROP TABLE student"
        cursor.execute(query)
        cursor.close()

    def actualizarDatos():
        cursor=connection.cursor()
        query= """ UPDATE student SET nombreestudiante='Chele' where nombreestudiante='Jonathan' """
        cursor.execute(query)
        cursor.close()

    insertarDatos('Josue','Ruiz','jRuiz@invenio.com')
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")