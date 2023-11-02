import pandas as pd

def funcionLogin():
    abrirexcelUsuario= pd.read_excel("usuarios.xlsx") #Abre el excel, lo lee y lo establece a un valor    print(abrirexcelUsuario) #Enseña la base de datos (Esta linea se tiene que quitar, es solo para revision)
    listaUsuarios = abrirexcelUsuario["Usuario"].tolist() #establece a ListaUsuarios solo la linea de Usarios(que esta en la lista) donde estan todos los nombres registrados

    controlWhilelogin=False
    #Ciclo
    while controlWhilelogin==False:
        usuarioLogin=input("""
    Nombre de usuario (O escribe "Salir" para regresar al menú anterior): """)

        #USUARIO
        if usuarioLogin in listaUsuarios: #Confirma si lo que puso el usuario esta en la base de datos

            rowUsuario = abrirexcelUsuario[abrirexcelUsuario["Usuario"] == usuarioLogin]
            

            controlWhileContra = False
            while controlWhileContra == False:
                contrasenaLogin=input("""
    Contraseña: """)
                #CONTRASEÑA
                if contrasenaLogin == rowUsuario["Contrasena"].values[0]: #Confirma si la contraseña es correcta, dependiendo de el usuario que puso
                    print(f"""
    Bienvenido {usuarioLogin} """) #Linea de prueba (se quita y se pone la entrada de las preguntas ya que se confirmo el usuario y la contraseña)
                    idUsuario = rowUsuario.loc[rowUsuario["Usuario"]==usuarioLogin,"ID"].values[0]
                    ScoreMate= rowUsuario.loc[rowUsuario["Usuario"]==usuarioLogin,"ScoreMate"].values[0]
                    ScoreEspa = rowUsuario.loc[rowUsuario["Usuario"]==usuarioLogin,"ScoreEspa"].values[0]
                    listaDatosUsuario=[idUsuario,usuarioLogin,ScoreMate,ScoreEspa]
                    return listaDatosUsuario
                    #Aqui puede que se mande a llamar el archivo del codigo de las preguntas
                    controlWhileContra = True
                    controlWhilelogin=True
                    controlWhileMenuInicial=True
                elif contrasenaLogin == "Salir":
                    controlWhileContra = True
                else:
                    print("""
    Contraseña incorrecta, intente de nuevo o escriba Salir para volver al usuario""")

        elif usuarioLogin=="Salir":
            return False
            controlWhilelogin=True

        else:
            print("""
    Usuario no encontrado. Intente de nuevo""")

