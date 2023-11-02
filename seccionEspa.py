import pandas as pd
import random
from openpyxl import load_workbook
from funcImprimir import imprimir    

def juegoEspa(listaDatosUsuario):
    #Lectura de datos del usuario
    idUsuario=listaDatosUsuario[0]
    nombreUsuario=listaDatosUsuario[1]
    scoreEspa=listaDatosUsuario[3]
    #Apertura de archivos y construcción de string para guardar el Score
    archivoUsuarios=load_workbook(filename="usuarios.xlsx")
    hoja = archivoUsuarios.active
    
    construirCelda="F"+str(idUsuario+1)
    
    archivoExcel = "preguntasEspa.xlsx"
    esp = pd.read_excel(archivoExcel)
    #Lectura de preguntas y asignación al nivel correcto
    listaMaestra=esp.values.tolist()
    niv1, niv2, niv3, niv4, niv5, niv6, niv7 = [], [], [], [], [], [], []
    for i in listaMaestra:
        nivel=i[1]
        match nivel:
            case 1:
                niv1.append(i)
            case 2:
                niv2.append(i)
            case 3:
                niv3.append(i)
            case 4:
                niv4.append(i)
            case 5:
                niv5.append(i)
            case 6:
                niv6.append(i)
            case 7:
                niv7.append(i)    

    #Inicialización de la variable para el control del ciclo while
    respuestaUsuario=1
    preguntasMostradas=[]

    while respuestaUsuario!=0: 
        nivelMostrar=niv1
        #Asignación del nivel del usuario
        if scoreEspa<200:
            nivelMostrar=niv1 
        if scoreEspa>=200 and scoreEspa<400:
            nivelMostrar=niv2
        elif scoreEspa>=400 and scoreEspa<600:
            nivelMostrar=niv3
        elif scoreEspa>=600 and scoreEspa<800:
            nivelMostrar=niv4
        elif scoreEspa>=800 and scoreEspa<1000:
            nivelMostrar=niv5
        elif scoreEspa>=1000 and scoreEspa<1200:
            nivelMostrar=niv6
        elif scoreEspa>=1200:
            nivelMostrar=niv7
        
        numeroPreguntasNivel=len(nivelMostrar)
        #Elección Random de la pregunta
        preguntaRandom=random.randint(0,numeroPreguntasNivel-1)
        #Si ya se le preguntó eso al usuario, se busca otra pregunta
        if preguntaRandom not in preguntasMostradas:
            #Función para randomizar la impresión de las respuestas
            listaMostrada=[3,4,5,6]
            listaRandom = random.sample(listaMostrada, len(listaMostrada))
            #listaRandom=[6,5,3,4]
            #La siguiente parte toma los índices de la listaRando y hace el print aleatorio de opciones
            textoPreguntas=f"""
        {nivelMostrar[preguntaRandom][2]}
        1){nivelMostrar[preguntaRandom][listaRandom[0]]}
        2){nivelMostrar[preguntaRandom][listaRandom[1]]}
        3){nivelMostrar[preguntaRandom][listaRandom[2]]}
        4){nivelMostrar[preguntaRandom][listaRandom[3]]}
        """
            imprimir(textoPreguntas)
            respuestaUsuario=input("""
        Respuesta elegida (Puedes teclear 0 para regresar al menú anterior): """)
            if respuestaUsuario=="0":
                pass          
            else:
                #Regresa la respuesta del usuario al índice original
                respuestaUsuario=int(respuestaUsuario)
                respuestaUsuario-=1
                indiceTemporal=int(listaRandom[respuestaUsuario])
                
                respuestaUsuario=listaMostrada.index(listaRandom[respuestaUsuario])
                respuestaUsuario+=3
                #Comprobación de respuesta correcta y cálculo de puntaje.
                if respuestaUsuario==nivelMostrar[preguntaRandom][7]:
                    respCorrecta=f"""
        ¡Respuesta correcta!
            
        Siguiente pregunta:
        """
                    imprimir(respCorrecta)
                    
                    scoreEspa+=10
                else:
                    indiceRespCorrecta=nivelMostrar[preguntaRandom][7]
                    respCorrecta=nivelMostrar[preguntaRandom][indiceRespCorrecta]
                    respIncorrecta=f"""
        ¡Respuesta incorrecta!
            
        La respuesta correcta es: {respCorrecta}
            
        Siguiente pregunta:
        """
                    imprimir(respIncorrecta)
                    
                    scoreEspa-=5
                #Actualizar puntos en archivo y guardar pregunta en las ya vistas     
                hoja[construirCelda] = scoreEspa
                archivoUsuarios.save(filename="usuarios.xlsx")
                preguntasMostradas.append(preguntaRandom)
                
        
        if len(preguntasMostradas)==len(nivelMostrar):
            preguntasMostradas=[]    