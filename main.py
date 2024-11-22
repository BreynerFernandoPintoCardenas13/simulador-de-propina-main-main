import requests
def principal():
    while True:  
        from menu.mainMenu import design1 as menuPrincipal

        try:
            respuesta = menuPrincipal()  # Suponiendo que esta función retorna un número
            if not isinstance(respuesta, int):  # Verificamos si la respuesta no es un número entero
                raise ValueError("La entrada debe ser un número entero")
        except ValueError as e:
            print(f"Error: {e}")
            continue
        match respuesta:
            case 1:
                from menu.registrar import option1
                option1()
            case 2:
                from menu.menuLIsta import menulistas
                menulistas()
principal()
