import sqlite3
import os

APP_PATH = os.getcwd()
DB_PATH = APP_PATH+'/my_slangs3.db'
con = sqlite3.connect(DB_PATH)
c = con.cursor()

def creartabla():
    c.execute("""
    CREATE TABLE SLANGS(
    ID          INTEGER   PRIMARY KEY AUTOINCREMENT NOT NULL,
    SLANG        TEXT                 NOT NULL,
    SIGNIFICADO  TEXT                 NOT NULL
    )""")
def rellenartabla():
    c.execute("""
         INSERT INTO SLANGS(ID,SLANG,SIGNIFICADO)
         VALUES(1,'Que xopa','saludo')
         """)

    c.execute("""
         INSERT INTO SLANGS(ID,SLANG,SIGNIFICADO)
         VALUES(2,'Mopri','Amigo cercano')
         """)

    c.execute("""
         INSERT INTO SLANGS(ID,SLANG,SIGNIFICADO)
         VALUES(3,'Rantan','Bastante')
         """)
    con.commit()
    
#creartabla()
#rellenartabla()

def nuevos_registros():
    SLANG=input("\nIngrese nuevo slang: ")
    SIGNIFICADO=input("Ingrese significado: ")
    c.execute("INSERT INTO SLANGS(ID,SLANG,SIGNIFICADO) VALUES(?,?,?)",
              (None,SLANG,SIGNIFICADO)
              )
    print("Palabra guardada correctamente, vaya a la opcion de ver listado de palabras para observar los cambios ")
    con.commit()
    
def listar_registros():
    print("\nListar Registros.")
    for row in c.execute("SELECT*FROM SLANGS"):
        print(f"ID: {row[0]}| SLANG: {row[1]}| SIGNIFICADO: {row[2]}")

def listar_slangs():
    print("\nLista de palabras")
    for row in c.execute("SELECT SLANG FROM SLANGS"):
        print(f"SLANG: {row[0]}")
 

def actualizar_registros():
    listar_registros()
    print("\nActualizar registro")
    ID= input("ID de palabra a editar: ")
    ID= int(ID)
    SLANG=input("Ingrese nuevo slang: ")
    SIGNIFICADO=input("Ingrese significado: ")
    c.execute('UPDATE SLANGS SET SLANG=?, SIGNIFICADO=? WHERE ID=?',
              (SLANG,SIGNIFICADO,ID))
    con.commit()
   
    
def eliminar_registro():
    listar_registros()
    print("\nELIMINAR REGISTRO.")
    ID= input("ID de palabra: ")
    ID= int(ID)
    c.execute('DELETE FROM SLANGS WHERE ID=?',(ID,))
    con.commit()
    listar_registros()

    
print("--------------------------Diccionario de Slang Panameño-------------------------")
menuprincipal = int(input("--Menú Principal: \n 1- agregar nueva palabra \n 2- Editar palabra existente\n 3- Eliminar palabra existente \n 4- Ver listado de palabras \n 5- Buscar significado de palabra \n 6- Salir \n Elija una opción: "))


while menuprincipal !=6:
    if menuprincipal == 1:
        nuevos_registros()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 2:
        actualizar_registros()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 3:
        eliminar_registro()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==4:
        listar_slangs()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==5:
        listar_registros()
        menuprincipal==input("preciones Enter para seguir: ")
    else:
        print("Por favor digite una opción válida")
        
    menuprincipal = int(input("\n\n\nMenú Principal: \n 1- agregar nueva palabra \n 2- Editar palabra existente \n 3- Eliminar palabra existente \n 4- Ver listado de palabras \n 5- Buscar significado de palabra \n 6- Salir \n"))


con.close()

    
    

    

