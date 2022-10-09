from cgitb import text
from distutils.cmd import Command
from email.policy import default
from multiprocessing import connection
from os import close
from tkinter import *
from tkinter import EXCEPTION, ttk

import customtkinter
import psycopg2


master = customtkinter.CTk() 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue") 
master.geometry("600x600")


def conexion(sele,query):
    conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='mandril77',
            database='Proyecto',
            port='5432'
    )

    if sele == '1':
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        cursor.close()
        return row
        
    elif sele == '2':
        cursor = conn.cursor()
        cursor.execute(query)
        print(query)
   
  
def openAlumnos(): 
    
    
    alumnos = customtkinter.CTkToplevel(master) 
  
    
    alumnos.title("ALUMNOS") 
  
    
    alumnos.geometry("600x600") 

    customtkinter.CTkLabel(alumnos,  
          text ="ALUMNOS").grid(row=0, column=0, sticky=W, pady=2)
    customtkinter.CTkLabel(alumnos,  
          text ="Buscar").grid(row=1, column=0, sticky=W, pady=2)

    entry = customtkinter.CTkEntry(alumnos, textvariable = "Buscar")
    entry.grid(row=1, column=1, sticky=W, pady=2)
    entry.focus_set()


    btnAlumnos = customtkinter.CTkButton(alumnos,  
             text ="BUSCAR ALUMNO",
             command = handleSearchAlumno) 
    btnAlumnos.grid(row=1, column=2, sticky=W, pady=2)

    btnAgregarAlumno1 = customtkinter.CTkButton(alumnos,
                text ="AGREGAR",
                fg_color = "green",
                command = handleAddAlumno)
    btnAgregarAlumno1.grid(row=1, column=3, sticky=W, pady=2)

    vistaTable = ttk.Treeview(alumnos, columns = (1,2,3), show = "headings", height = "5")
    vistaTable.grid(row=2, column=0, columnspan=4)

    vistaTable.heading(3, text = "Cédula")
    vistaTable.heading(1, text = "Nombre")
    vistaTable.heading(2, text = "Apellidos") 
    vistaTable.heading(3, text = "Correo")
    
    for x in conexion('1',f""" SELECT * FROM bda.student """):
        vistaTable.insert("", "end", values = (x[1], x[2], x[3]))
        
    # style = ttk.Style()
    # style.theme_use("clam")
    # style.map("Treeview")
    # style.configure("Treeview", rowheight = 25)
    # style.configure("Treeview.Heading", font = ("Helvetica", 10, "bold"))
    # style.configure("Treeview", font = ("Helvetica", 10))

    
def handleAddAlumno(): 
    alumnosAgregados = customtkinter.CTkToplevel()

    alumnosAgregados.title("AGREGAR ALUMNO")

    alumnosAgregados.geometry("600x600")

    customtkinter.CTkLabel(alumnosAgregados,  
        text ="Cédula").grid(row=0, column=0, sticky=W, pady=2)

    cedula = customtkinter.CTkEntry(alumnosAgregados,)
    cedula.grid(row=0, column=1, sticky=W, pady=2)
    
    customtkinter.CTkLabel(alumnosAgregados,  
        text ="Nombre").grid(row=1, column=0, sticky=W, pady=2) 

    nombre = customtkinter.CTkEntry(alumnosAgregados)
    nombre.grid(row=1, column=1, sticky=W, pady=2)

    customtkinter.CTkLabel(alumnosAgregados,  
          text ="Apellidos").grid(row=2, column=0, sticky=W, pady=2)

    apellidos = customtkinter.CTkEntry(alumnosAgregados)
    apellidos.grid(row=2, column=1, sticky=W, pady=2)
    customtkinter.CTkLabel(alumnosAgregados,  
          text ="Correo").grid(row=3, column=0, sticky=W, pady=2)

    email = customtkinter.CTkEntry(alumnosAgregados)
    email.grid(row=3, column=1, sticky=W, pady=2)


    btnAgregarAlumno = customtkinter.CTkButton(alumnosAgregados,  
             text ="AGREGAR ALUMNO",
             fg_color= "green",
             command = conexion('2',(f""" INSERT INTO bda.student (nombreestudiante,apellidos,email,cedula) VALUES ('{nombre}','{apellidos}','{email}','{cedula}')""")))
    btnAgregarAlumno.grid(row=4, column=1, sticky=W, pady=2)

def handleSearchAlumno(): 
    print("ADD Alumno")


def openProfesores(): 
      
        profesores = customtkinter.CTkToplevel(master) 
  
    
        profesores.title("PROFESORES") 
  
    
        profesores.geometry("600x600") 
  
        customtkinter.CTkLabel(profesores,  
          text ="PROFESORES").grid(row=0, column=0, sticky=W, pady=2)

        customtkinter.CTkLabel(profesores,  
            text ="Buscar").grid(row=1, column=0, sticky=W, pady=2)

        entry = customtkinter.CTkEntry(profesores, textvariable = "Buscar")
        entry.grid(row=1, column=1, sticky=W, pady=2)
        entry.focus_set()

        btnProfesores = customtkinter.CTkButton(profesores,  
             text ="AGREGAR PROFESOR",
             command = handleAddProfesores) 
        btnProfesores.grid(row=1, column=1, sticky=W, pady=2)

        btnProfesores = customtkinter.CTkButton(profesores,  
             text ="BUSCAR PROFESOR",
             command = handleSearchProfesores) 
        btnProfesores.grid(row=1, column=2, sticky=W, pady=2)
            
        vistaTable = ttk.Treeview(profesores, columns = (1,2,3,4), show = "headings", height = "5")
        vistaTable.grid(row=2, column=0, columnspan=4)

        vistaTable.heading(4, text = "Cédula")
        vistaTable.heading(1, text = "Nombre")
        vistaTable.heading(2, text = "Apellidos")
        vistaTable.heading(3, text = "Correo")

        for x in conexion('bda.profesor'):
            vistaTable.insert("", "end", values = (x[1]+' '+x[3], x[2], x[4]))

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        style.configure("Treeview", rowheight = 25)
        style.configure("Treeview.Heading", font = ("Helvetica", 10, "bold"))

def handleAddProfesores(): 

    profesoresAgregados = customtkinter.CTkToplevel()

    profesoresAgregados.title("AGREGAR PROFESOR")

    profesoresAgregados.geometry("600x600")

    customtkinter.CTkLabel(profesoresAgregados,  
        text ="Cédula").grid(row=0, column=0, sticky=W, pady=2)

    entry = customtkinter.CTkEntry(profesoresAgregados)
    entry.grid(row=0, column=1, sticky=W, pady=2)

    customtkinter.CTkLabel(profesoresAgregados,  
        text ="Nombre").grid(row=1, column=0, sticky=W, pady=2)

    entry = customtkinter.CTkEntry(profesoresAgregados)
    entry.grid(row=1, column=1, sticky=W, pady=2)

    customtkinter.CTkLabel(profesoresAgregados,  
        text ="Apellidos").grid(row=2, column=0, sticky=W, pady=2) 

    entry = customtkinter.CTkEntry(profesoresAgregados)
    entry.grid(row=2, column=1, sticky=W, pady=2)

    customtkinter.CTkLabel(profesoresAgregados,  
    text ="Email").grid(row=3, column=0, sticky=W, pady=2)
    entry = customtkinter.CTkEntry(profesoresAgregados)
    entry.grid(row=3, column=1, sticky=W, pady=2)
    btnAgregarProfesor = customtkinter.CTkButton(profesoresAgregados,  
             text ="AGREGAR PROFESOR",
             fg_color	= "green",
             command = handleSearchProfesores) 
    btnAgregarProfesor.grid(row=4, column=1, sticky=W, pady=2)

def handleSearchProfesores(): 

    profesoresBuscados = customtkinter.CTkToplevel()

    profesoresBuscados.title("BUSCAR PROFESOR")

    profesoresBuscados.geometry("600x600")

        
def openCarreras(): 

    carreras = customtkinter.CTkToplevel(master) 
    carreras.title("CARRERAS") 
  
    
    carreras.geometry("600x600") 

    customtkinter.CTkLabel(carreras,  
        text ="CARRERAS").grid(row=0, column=0, sticky=W, pady=2)

    customtkinter.CTkLabel(carreras,
        text ="Buscar").grid(row=1, column=0, sticky=W, pady=2)

    entry = customtkinter.CTkEntry(carreras, textvariable = "Buscar")
    entry.grid(row=1, column=1, sticky=W, pady=2)
    entry.focus_set()

    btnCarreras = customtkinter.CTkButton(carreras,  
        text ="AGREGAR CARRERA",
        command = handleAddCarreras) 
    btnCarreras.grid(row=1, column=1, sticky=W, pady=2) 

    btnCarreras = customtkinter.CTkButton(carreras,  
        text ="BUSCAR CARRERA",
        command = handleSearchCarreras) 
    btnCarreras.grid(row=1, column=2, sticky=W, pady=2, padx=10)

    vistaTable = ttk.Treeview(carreras, columns = (1), show = "headings", height = "5", selectmode = "browse", style = "Treeview", padding = 10)
    vistaTable.grid(row=2, column=0, columnspan=4)

    vistaTable.heading(1, text = "Nombre")

    for x in conexion('bda.carreras'):
            vistaTable.insert("", "end", values = (x[1]))
    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    style.configure("Treeview", rowheight = 25)
    style.configure("Treeview.Heading", font = ("Helvetica", 10, "bold"))

def handleAddCarreras(): 

    carrerasAgregadas = customtkinter.CTkToplevel()

    carrerasAgregadas.title("AGREGAR CARRERA")

    carrerasAgregadas.geometry("600x600")

    customtkinter.CTkLabel(carrerasAgregadas,  
        text ="Nombre").grid(row=0, column=0, sticky=W, pady=2)
    entry = customtkinter.CTkEntry(carrerasAgregadas)
    entry.grid(row=0, column=1, sticky=W, pady=2)

    btnAgregarCarrera = customtkinter.CTkButton(carrerasAgregadas,  
             text ="AGREGAR CARERA",
             fg_color	= "green",
             command = handleSearchCarreras) 
    btnAgregarCarrera.grid(row=1, column=1, sticky=W, pady=2)

def handleSearchCarreras(): 

    carrerasBuscadas = customtkinter.CTkToplevel()

    carrerasBuscadas.title("BUSCAR CARRERA")

    carrerasBuscadas.geometry("600x600")

def openCursos(): 
        cursos = customtkinter.CTkToplevel(master) 
        cursos.title("CURSOS") 
        cursos.geometry("600x600") 

        customtkinter.CTkLabel(cursos,  
          text ="CURSOS").grid(row=0, column=0, sticky=W, pady=2)

        customtkinter.CTkLabel(cursos,  
          text ="Buscar").grid(row=1, column=0, sticky=W, pady=2)

        entry = customtkinter.CTkEntry(cursos, textvariable = "Buscar")
        entry.grid(row=1, column=1, sticky=W, pady=2)
        entry.focus_set() 

        btnCursos = customtkinter.CTkButton(cursos,
            text ="BUSCAR CURSO",
            command = handleSearchCursos)
        btnCursos.grid(row=1, column=1, sticky=W, pady=2)
        btnCursos = customtkinter.CTkButton(cursos,
            text ="AGREGAR CURSO",
            command = handleAddCursos)
        btnCursos.grid(row=1, column=2, sticky=W, pady=2)



        vistaTable = ttk.Treeview(cursos, columns = (1,2,3,4), show = "headings", height = "5")
        vistaTable.grid(row=2, column=0, columnspan=4)

        vistaTable.heading(1, text = "Nombre")
        vistaTable.heading(2, text = "Periodo")
        vistaTable.heading(4, text = "Horario")
        vistaTable.heading(3, text = "Modalidad")

        for x in conexion('bda.cursos'):
            vistaTable.insert("", "end", values = (x[1], x[2], x[3],x[4]))

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        style.configure("Treeview", rowheight = 25)
        style.configure("Treeview.Heading", font = ("Helvetica", 10, "bold"))

        btnCarreras = customtkinter.CTkButton(cursos,  
             text ="AGREGAR CURSOS",
             command = handleAddCursos) 
        btnCarreras.grid(row=3, column=1, sticky=W, pady=2)
def handleAddCursos(): 

    cursosAgregadas = customtkinter.CTkToplevel()

    cursosAgregadas.title("AGREGAR CURSOS")

    cursosAgregadas.geometry("600x600")

    customtkinter.CTkLabel(cursosAgregadas,  
        text ="Nombre").grid(row=0, column=0, sticky=W, pady=2)
    entry = customtkinter.CTkEntry(cursosAgregadas)
    entry.grid(row=0, column=1, sticky=W, pady=2)

    customtkinter.CTkLabel(cursosAgregadas,
        text ="Periodo").grid(row=1, column=0, sticky=W, pady=2)
    trimestres = customtkinter.CTkComboBox(cursosAgregadas, text_color= "black" , state= "readonly", values=["Trimrestre 1", "Trimrestre 2", "Trimrestre 3", "Trimrestre 4" , "Trimrestre 5" , "Trimrestre 6" , "Trimrestre 7" , "Trimrestre 3", "Trimrestre 8", "Trimrestre 9" , "Trimrestre 10", "Trimrestre 11", "Trimrestre 12" , "Trimrestre 13", "Trimrestre 14", "Trimrestre 15" , "Trimrestre 16"])
    trimestres.grid(row=1, column=1, sticky=W, pady=2)

    customtkinter.CTkLabel(cursosAgregadas,
        text ="Horario").grid(row=2, column=0, sticky=W, pady=2)

    horarios = customtkinter.CTkComboBox(cursosAgregadas,text_color= "black" , state= "readonly",  values=["Mañana", "Tarde", "Noche", "Sabatinos"] )
    horarios.grid(row=2, column=1, sticky=W, pady=2)

    customtkinter.CTkLabel(cursosAgregadas,
        text ="Modalidad").grid(row=3, column=0, sticky=W, pady=2)
    horarios = customtkinter.CTkComboBox(cursosAgregadas,text_color= "black" , state= "readonly", values=["Presencial", "Virtual", "Híbrida"] )
 
    horarios.grid(row=3, column=1, sticky=W, pady=2)

    btnAgregarCursos = customtkinter.CTkButton(cursosAgregadas,  
             text ="AGREGAR CURSO",
             fg_color	= "green",
             command = handleSearchCarreras) 
    btnAgregarCursos.grid(row=4, column=1, sticky=W, pady=2)

def handleSearchCursos(): 

    cursosBuscadas = customtkinter.CTkToplevel()

    cursosBuscadas.title("BUSCAR CURSOS")

    cursosBuscadas.geometry("600x600")

label = customtkinter.CTkLabel(master,  
              text ="INVENIO") 
  
label.grid(row=0, column=1, sticky=W, pady=2, padx=200)
  
btnAlumnos = customtkinter.CTkButton(master,  
             text ="ALUMNOS",  
             command = openAlumnos) 
btnAlumnos.grid(row=1, column=1,  pady=2, padx=200)

btnProfesores = customtkinter.CTkButton(master,  
             text ="PROFESORES",  
             command = openProfesores) 
btnProfesores.grid(row=2, column=1, sticky=W, pady=10, padx=200)

btnCarreras = customtkinter.CTkButton(master,  
             text ="CARRERAS",  
             command = openCarreras) 
btnCarreras.grid(row=3, column=1, sticky=W, pady=10, padx=200)

btnCursos = customtkinter.CTkButton(master,  
             text ="CURSOS",  
             command = openCursos) 
btnCursos.grid(row=4, column=0, pady=2)

master.mainloop()
