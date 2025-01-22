from logica.logica import addRegistrar, read_file, write_file
import requests
import os

def option1():
    formato=read_file("base.json")
    while True:
        print(f"""
            =============================================
            Registrar Nuevo Gasto
            =============================================
            Ingrese la información del gasto:
""")
        monto=str(input(f" \t   Nombre del usuario: "))
        categoria=str(input(" \t   Correo Elcetronico: "))
        descripcion=input(" \t   Selecciona rol(Administrador/Usuario):")
        #formato=addRegistrar(monto, categoria, descripcion, formato)
        
        decision=input("""Ingrese 'S' para guardar o 'N' para cancelar: 
                            =============================================        
                               """)
        decision.lower()
        if decision=="s":
            write_file(formato, "base.json")
        elif decision=="n":
            print("se ha cancelado todo")    
        
