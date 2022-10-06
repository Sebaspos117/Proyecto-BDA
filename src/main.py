from cgitb import text
from distutils.cmd import Command
from email.policy import default
from os import close
from tkinter import *
from tkinter import ttk

import customtkinter

master = customtkinter.CTk() 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue") 
master.geometry("400x400")
  
  
def openAlumnos(): 

    alumnos = customtkinter.CTkToplevel(master) 
  
    
    alumnos.title("ALUMNOS") 
  
    
    alumnos.geometry("400x400") 

    customtkinter.CTkLabel(alumnos,  
          text ="ALUMNOS").pack()

    btnAlumnos = customtkinter.CTkButton(alumnos,  
             text ="AGREGAR ALUMNO",
             command = handleAddAlumno) 
    btnAlumnos.pack(pady = 10) 

    btnAlumnos = customtkinter.CTkButton(alumnos,  
             text ="BUSCAR ALUMNO",
             command = handleSearchAlumno) 
    btnAlumnos.pack(pady = 10) 
        
def handleAddAlumno(): 
    alumnosAgregados = customtkinter.CTkToplevel()

    alumnosAgregados.title("AGREGAR ALUMNO")

    alumnosAgregados.geometry("400x400")
    
    customtkinter.CTkLabel(alumnosAgregados,  
        text ="Nombre").pack() 

    entry = customtkinter.CTkEntry(alumnosAgregados)
    entry.pack()

    customtkinter.CTkLabel(alumnosAgregados,  
          text ="Carrera").pack() 

    entry = customtkinter.CTkEntry(alumnosAgregados)
    entry.pack()

    customtkinter.CTkLabel(alumnosAgregados,  
          text ="Cursos").pack() 

    entry = customtkinter.CTkEntry(alumnosAgregados)
    entry.pack()

    btnAgregarAlumno = customtkinter.CTkButton(alumnosAgregados,  
             text ="AGREGAR ALUMNO",
             fg_color	= "green",
             command = handleSearchAlumno) 
    btnAgregarAlumno.pack(pady = 10) 

def handleSearchAlumno(): 

    alumnosBuscados = customtkinter.CTkToplevel()

    alumnosBuscados.title("BUSCAR ALUMNO")

    alumnosBuscados.geometry("400x400")

    
def openProfesores(): 
      
    
        profesores = customtkinter.CTkToplevel(master) 
  
    
        profesores.title("PROFESORES") 
  
    
        profesores.geometry("400x400") 
  
        customtkinter.CTkLabel(profesores,  
          text ="PROFESORES").pack() 

        btnProfesores = customtkinter.CTkButton(profesores,  
             text ="AGREGAR PROFESOR",
             command = handleAddProfesores) 
        btnProfesores.pack(pady = 10) 

        btnProfesores = customtkinter.CTkButton(profesores,  
             text ="BUSCAR PROFESOR",
             command = handleSearchProfesores) 
        btnProfesores.pack(pady = 10)

def handleAddProfesores(): 

    profesoresAgregados = customtkinter.CTkToplevel()

    profesoresAgregados.title("AGREGAR PROFESOR")

    profesoresAgregados.geometry("400x400")

    customtkinter.CTkLabel(profesoresAgregados,  
        text ="Nombre").pack() 

    entry = customtkinter.CTkEntry(profesoresAgregados)
    entry.pack()

    customtkinter.CTkLabel(profesoresAgregados,  
        text ="Cursos Impartidos").pack() 

    entry = customtkinter.CTkEntry(profesoresAgregados)
    entry.pack()

    btnAgregarProfesor = customtkinter.CTkButton(profesoresAgregados,  
             text ="AGREGAR PROFESOR",
             fg_color	= "green",
             command = handleSearchProfesores) 
    btnAgregarProfesor.pack(pady = 10) 

def handleSearchProfesores(): 

    profesoresBuscados = customtkinter.CTkToplevel()

    profesoresBuscados.title("BUSCAR PROFESOR")

    profesoresBuscados.geometry("400x400")
        
def openCarreras(): 

    carreras = customtkinter.CTkToplevel(master) 
    carreras.title("CARRERAS") 
  
    
    carreras.geometry("400x400") 

    customtkinter.CTkLabel(carreras,  
        text ="CARRERAS").pack() 

    btnCarreras = customtkinter.CTkButton(carreras,  
        text ="AGREGAR CARRERA",
        command = handleAddCarreras) 
    btnCarreras.pack(pady = 10) 

    btnCarreras = customtkinter.CTkButton(carreras,  
        text ="BUSCAR CARRERA",
        command = handleSearchCarreras) 
    btnCarreras.pack(pady = 10) 

def handleAddCarreras(): 

    carrerasAgregadas = customtkinter.CTkToplevel()

    carrerasAgregadas.title("AGREGAR CARRERA")

    carrerasAgregadas.geometry("400x400")

    customtkinter.CTkLabel(carrerasAgregadas,  
        text ="Nombre").pack()
    entry = customtkinter.CTkEntry(carrerasAgregadas)
    entry.pack()

    customtkinter.CTkLabel(carrerasAgregadas,  
        text ="Cursos").pack()
    entry = customtkinter.CTkEntry(carrerasAgregadas)
    entry.pack()

    btnAgregarCarrera = customtkinter.CTkButton(carrerasAgregadas,  
             text ="AGREGAR PROFESOR",
             fg_color	= "green",
             command = handleSearchCarreras) 
    btnAgregarCarrera.pack(pady = 10) 

def handleSearchCarreras(): 

    carrerasBuscadas = customtkinter.CTkToplevel()

    carrerasBuscadas.title("BUSCAR CARRERA")

    carrerasBuscadas.geometry("400x400")

def openCursos(): 
        cursos = customtkinter.CTkToplevel(master) 
        cursos.title("CURSOS") 
        cursos.geometry("400x400") 

        customtkinter.CTkLabel(cursos,  
          text ="CURSOS").pack() 

        btnCarreras = customtkinter.CTkButton(cursos,  
             text ="AGREGAR CURSOS",
             command = handleAddCursos) 
        btnCarreras.pack(pady = 10) 

        btnCarreras = customtkinter.CTkButton(cursos,  
             text ="BUSCAR CURSOS",
             command = handleSearchCursos) 
        btnCarreras.pack(pady = 10) 
def handleAddCursos(): 

    cursosAgregadas = customtkinter.CTkToplevel()

    cursosAgregadas.title("AGREGAR CURSOS")

    cursosAgregadas.geometry("400x400")

    customtkinter.CTkLabel(cursosAgregadas,  
        text ="Nombre").pack() 
    entry = customtkinter.CTkEntry(cursosAgregadas)
    entry.pack()

    trimestres = customtkinter.CTkComboBox(cursosAgregadas, text_color= "black" , state= "readonly", values=["Trimrestre 1", "Trimrestre 2", "Trimrestre 3", "Trimrestre 4" , "Trimrestre 5" , "Trimrestre 6" , "Trimrestre 7" , "Trimrestre 3", "Trimrestre 8", "Trimrestre 9" , "Trimrestre 10", "Trimrestre 11", "Trimrestre 12" , "Trimrestre 13", "Trimrestre 14", "Trimrestre 15" , "Trimrestre 16"])
    trimestres.place(x=130, y=70)

    horarios = customtkinter.CTkComboBox(cursosAgregadas,text_color= "black" , state= "readonly",  values=["Mañana", "Tarde", "Noche", "Sabatinos"] )
    horarios.place(x=130, y=110)

    horarios = customtkinter.CTkComboBox(cursosAgregadas,text_color= "black" , state= "readonly", values=["Presencial", "Virtual", "Híbrida"] )
 
    horarios.place(x=130, y=150)

    btnAgregarCursos = customtkinter.CTkButton(cursosAgregadas,  
             text ="AGREGAR CURSO",
             fg_color	= "green",
             command = handleSearchCarreras) 
    btnAgregarCursos.pack(pady = 10)

    btnAgregarCursos.place(relx=0.5, rely=0.5, anchor=CENTER)

def handleSearchCursos(): 

    cursosBuscadas = customtkinter.CTkToplevel()

    cursosBuscadas.title("BUSCAR CURSOS")

    cursosBuscadas.geometry("400x400")

label = customtkinter.CTkLabel(master,  
              text ="INVENIO") 
  
label.pack(pady = 10) 
  
btnAlumnos = customtkinter.CTkButton(master,  
             text ="ALUMNOS",  
             command = openAlumnos) 
btnAlumnos.pack(pady = 10) 

btnProfesores = customtkinter.CTkButton(master,  
             text ="PROFESORES",  
             command = openProfesores) 
btnProfesores.pack(pady = 10) 

btnCarreras = customtkinter.CTkButton(master,  
             text ="CARRERAS",  
             command = openCarreras) 
btnCarreras.pack(pady = 10) 

btnCursos = customtkinter.CTkButton(master,  
             text ="CURSOS",  
             command = openCursos) 
btnCursos.pack(pady = 10) 

master.mainloop()
