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
        monto=float(input(f" \t   -Monto del gasto: "))
        categoria=str(input(" \t   -Categoría (ej. comida, transporte, entretenimiento, otros: )"))
        descripcion=input(" \t   -Descripción (opcional): ")
        date = input(" \t   -cual es la fecha? (05/05/2000)")
        formato=addRegistrar(monto, categoria, descripcion, date, formato)
        write_file(formato, "base.json")
        decision=int(input("""Ingrese 'S' para guardar o 'N' para cancelar: 
                            =============================================        
                               """))
            
        
