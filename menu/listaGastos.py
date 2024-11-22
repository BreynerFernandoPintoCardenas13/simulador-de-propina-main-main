from logica.logica import mostrarTodos, read_file, write_file, mostrarCategoria, mostrarFecha
from tabulate import tabulate
def mostrarTodosMenu():
    while True:
        formato=read_file("base.json")
        mostrarTodos(formato)
        desicion=int(input("quieres volver al menu principal? S/1 N/0 "))
        if desicion==1:
            break
def mostrarCategoriaMenu():
    while True:
        formato=read_file("base.json")
        peticion=input("que categoria quieres ver?")
        categoria=peticion.lower()
        mostrarCategoria(formato, categoria)
        desicion=int(input("quieres volver al menu principal? S/1 N/0 "))
        if desicion==1:
            break
def mostrarFechaMenu():
    while True:
        formato=read_file("base.json")
        peticion=input("ingresa la fecha a la cual deseas acceder")
        categoria=peticion.lower()
        mostrarFecha(formato, categoria)
        desicion=int(input("quieres volver al menu principal? S/1 N/0 "))
        if desicion==1:
            break
 