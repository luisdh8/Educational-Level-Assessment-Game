import pandas as pd
import funcionLogin
import seccionEspa
import seccionMate
from funcImprimir import imprimir



#Menu inicial de registro y login
saludo=f"""
    Hola, bienvenido al Himalaya
    Este juego es una serie de preguntas de regularización de Español y Matemáticas
    Está destinado para niños de tercero de primaria a tercero de secundaria
    Elige una de las siguientes opciones:
"""

imprimir(saludo)

controlWhileMenuInicial=False

#ciclo para correr el menu y controlarlo
while controlWhileMenuInicial==False:
    loginRegistrarInput=input("""
    1.- Iniciar sesión
    2.- Registrarse

    Ingresa tu opción: """)


    if loginRegistrarInput=="1": #Iniciar sesion
        listaDatosUsuario= funcionLogin.funcionLogin()
        if listaDatosUsuario != False:
            break

    elif loginRegistrarInput=="2":
        exec(open("funcionRegistro.py").read())
        break

#Variables para control de seleccionar una u otra opció de juego.
controlWhileOpcionJuego=False
opcionJuegoElegir="0"

#Ciclo para controlar la sección que queremos jugar. Cada función puede regresar aquí.
while controlWhileOpcionJuego==False:
    opcionJuegoElegir=input("""
    ¿Qué sección deseas jugar? (Escribe Salir para terminar la sesión)
    1.- Matemáticas
    2.- Español
    
    Opción elegida: """)
    if opcionJuegoElegir=="Salir" or opcionJuegoElegir=="salir":
        break
    elif opcionJuegoElegir=="1":
        seccionMate.juegoMate(listaDatosUsuario)
    elif opcionJuegoElegir=="2":
        seccionEspa.juegoEspa(listaDatosUsuario)