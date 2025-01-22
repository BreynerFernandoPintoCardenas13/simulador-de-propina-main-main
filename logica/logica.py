import json
import tabulate
# Función para leer el archivo JSON
def read_file(path):
    try:
        with open(f"databases/{path}", "r") as file:
            data = file.read()
            return json.loads(data)
    except FileNotFoundError:
        return {}

# Función para escribir en el archivo JSON
def write_file(data, path):
    with open(f"databases/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
def addRegistrar(Nombre, Correo, Rol, formato, NombreKey):
    data = read_file("base.json")
    formato[NombreKey]= {
        'Nombre del usuario:':Nombre,
        'Correo electronico':Correo,
        'Rol':Rol
    }
    write_file(data, "base.json")
    return formato
def mostrarTodos(formato):
    if formato:
        for date, client in formato.items():
            (f"\ndate: {date}")
            (f"Monto: {client['monto']}")
            (f"categoria: {client['categoria']}")
            (f"Descripcion: {client['descripcion']}")
    tablaBonita=[]
    headers=["FECHA", "MONTO", "CATEGORIA", "TELEFONO"]
    for date, client in formato.items():
        todo=[date, client['monto'], client['categoria'], client['descripcion']]
        tablaBonita.append(todo)
    print(tabulate(tablaBonita, headers=headers, tablefmt="grid" ))

    write_file(formato, "base.json")


def mostrarCategoria(formato, Nombre):
    filtrarCategoria= {NombreKey: client for Nombre, client in formato.items() if client['nombre']==nombre}

    if filtrarCategoria:
        for NombreKey, client in filtrarCategoria.items():
            print(f"Nombre de usuario: {client['Nombre']}")
            print(f"Correo: {client['Correo']}")
            print(f"Rol: {client['Rol']}")
    else:
        print("NO REGISTRADA")
    tablaBonita=[]
    headers=["Nombre", "Correo", "Rol"]
    print(tabulate(tablaBonita, headers=headers, tablefmt="grid" ))

    write_file(formato, "base.json")

def mostrarFecha(formato, categoria):
   filtrarFecha={date: client for date, client in formato.items() if date==categoria}

   if filtrarFecha:
        for date, client in filtrarFecha.items():
                print(f"\ndate: {date}")
                print(f"Monto: {client['monto']}")
                print(f"categoria: {client['categoria']}")
                print(f"Descripcion: {client['descripcion']}")
        tablaBonita=[]
        headers=["FECHA", "MONTO", "CATEGORIA", "TELEFONO"]
        for date, client in filtrarFecha.items():
         todo=[date, client['monto'], client['categoria'], client['descripcion']]
        tablaBonita.append(todo)
        print(tabulate(tablaBonita, headers=headers, tablefmt="grid" ))

   write_file(formato, "base.json")
