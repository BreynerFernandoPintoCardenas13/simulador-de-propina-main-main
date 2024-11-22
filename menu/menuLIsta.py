import match
def menulistas():
    print("""
        =============================================
                    Listar Gastos
        =============================================
        Seleccione una opción para filtrar los gastos:

        1. Ver todos los gastos
        2. Filtrar por categoría
        3. Filtrar por rango de fechas
        4. Regresar al menú principal
        =============================================
    """)
    desicion=int(input("ingresa una opcion: "))
    match desicion:
        case 1:
            from menu.listaGastos import mostrarTodosMenu
            mostrarTodosMenu()
        case 2:
            from menu.listaGastos import mostrarCategoriaMenu
            mostrarCategoriaMenu()
        case 3:
            from menu.listaGastos import mostrarFechaMenu
            mostrarFechaMenu()
        case 4:
            from main import principal
            principal()