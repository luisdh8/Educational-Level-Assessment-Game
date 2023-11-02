#Importamoossssss pandas para excel y os para verificar el excel
import pandas as pd
import os

# Comprobamos si el archivo Excel ya existe, si no es asi entonces va a crear uno nuevo
archivo_excel = "usuarios.xlsx"
if os.path.isfile(archivo_excel):
    daf = pd.read_excel(archivo_excel)
else:
    dat = {'ID':[], 'Usuario': [], 'Contraseña': [], 'Grado que cursa': [], 'Subgrado que cursa': [], 'Score_mat': [], 'Score_Es': []}
    daf = pd.DataFrame(dat)

#(FUNCION)Aqui entran los datos que el usuario pone con el input KAKAKAUUUU
def agregar_datos(ID, usuario, contr, subgrado, score_mat, score_es):
    global daf
    #Aqui es donde los valores que el usuario puso se van para ser guardados posteriormente en el excel
    nueva_fila = {'ID': ID,'Usuario': usuario, 'Contrasena': contr, "NivelEducativo": subgrado, "ScoreMate": score_mat, "ScoreEspa": score_es}
    nueva_data = pd.DataFrame([nueva_fila])
    daf = pd.concat([daf, nueva_data], ignore_index=True)
    #Justo en esta linea de codigo es donde la variable que contiene la lista guarda las variables
    daf.to_excel(archivo_excel, index=False)
    

#Pide al usuario sus datos, estos datos son necesarios para el LOGIN
ultimoID = daf["ID"].values[-1] #Le el utlimo valor de la columna ID para saber que numero es y posteriormente agregarle +1 a un nuevo usuario
usuario = input("""
    Ingrese su usuario: """)
contra = input("""
    Ingrese su contraseña: """)
grado = int(input("""
    ¿En qué nivel de estudios estás?
        1) Primaria
        2) Secundaria
    
    Respuesta: """))
if grado == 1:
    subgrado = int(input("""
    ¿En qué grado estás? 
        3) Tercero
        4) Cuarto
        5) Quinto
        6) Sexto
    
    Respuesta: """))
    subgrado-=2
    
elif grado == 2:
    subgrado = int(input("""
    ¿En qué grado estás?
        1) Primero
        2) Segundo
        3) Tercero
    
    Respuesta: """))
    subgrado+=4
    
score_mat = (subgrado-1)*200
score_es = (subgrado-1)*200


#Manda a llamar la funcion con todos los valores pedidos al usuario
agregar_datos(ultimoID + 1, usuario, contra, subgrado, score_mat, score_es)

listaDatosUsuario=[ultimoID + 1,usuario,score_mat,score_es]