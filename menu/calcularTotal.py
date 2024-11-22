from formula.logic import calcular_propina, total_propina, dividir_total
import requests
import tabulate
import os

def option2():
    while True:
        print(f"""
        =============================================
        Calculate tip divide
        =============================================""")
        
        try:
            monto = float(input("        Enter the amount total: $"))
        except ValueError:
            print("Error: Please enter a valid number for the amount.")
            continue  # Solicitar la entrada nuevamente si es inválida

        try:
            porcentaje = int(input("        Enter the percentage of tip (for example: 15): %"))
        except ValueError:
            print("Error: Please enter a valid number for the percentage.")
            continue  # Solicitar la entrada nuevamente si es inválida

        # Calcular propina
        propina = calcular_propina(monto, porcentaje)
        
        try:
            personas = int(input("        Enter the number of people: "))
        except ValueError:
            print("Error: Please enter a valid integer for the number of people.")
            continue  # Solicitar la entrada nuevamente si es inválida
        
        # Dividir el monto
        montoDividido = dividir_total(monto, personas)
        
        # Calcular el total
        total = total_propina(monto, propina)
        
        # Mostrar los resultados
        print(f"""
        =============================================
        The tip calculated is: ${propina}
        The total to pay is: ${total}
        Money for each person: ${montoDividido}
        =============================================""")
        
        # Preparar los datos para la solicitud POST
        headers = {'content-type': 'application/json'}
        data = {'monto': monto, 'porcentaje': porcentaje, 'propina': propina, 'total': total, 'personas': personas, 'dividido': montoDividido}
        
        try:
            response = requests.post('https://6734eba25995834c8a915cad.mockapi.io/dividida', headers=headers, json=data)
            response.raise_for_status()  # Verificar si la solicitud fue exitosa
        except requests.exceptions.RequestException as e:
            print(f"Error with the request: {e}")
            continue  # Si hay un error en la solicitud, se vuelve a intentar
        
        # Preguntar si el usuario quiere calcular nuevamente o salir
        try:
            option = int(input("        Do you want to calculate again? Y=1 BACK=2 EXIT=0:\n"))
        except ValueError:
            print("Error: Please enter a valid option (0, 1, or 2).")
            continue  # Si la opción no es válida, se vuelve a preguntar
        
        if option == 0:
            from menu.thankyou import goodbye as bye
            bye()
            break
        elif option == 2:
            from main import principal as back
            back()
        os.system("clear")  # Limpiar la pantalla para la próxima iteración
