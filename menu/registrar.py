from logica.logica import addRegistrar, read_file, write_file
import requests
import os

def option1():
    formato=read_file("base.json")
    while True:
        print(f"""
            =============================================
            Registrar Nuevo Usuario
            =============================================
            Ingrese la información del gasto:
""")
        NombreKey=str(input(f" \t   Nombre del usuario: "))
        Nombre=NombreKey
        Correo=str(input(" \t   Correo Elcetronico: "))
        Rol=input(" \t   Selecciona rol(Administrador/Usuario):")
        formato=addRegistrar(NombreKey, Nombre, Correo, Rol, formato)
        
        decision=input("""Ingrese 'S' para guardar o 'N' para cancelar: 
                            =============================================        
                               """)
        decision.lower()
        if decision=="s":
            write_file(formato, "base.json")
        elif decision=="n":
            print("se ha cancelado todo")    
            break
