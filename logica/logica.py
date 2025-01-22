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
def addRegistrar(Nombre, Correo, Rol, formato):
    data = read_file("base.json")
    formato= {
        'Nobre del usuario:':Nombre,
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


def mostrarCategoria(formato, categoria):
    filtrarCategoria= {date: client for date, client in formato.items() if client['categoria']==categoria}

    if filtrarCategoria:
        for date, client in filtrarCategoria.items():
            print(f"\ndate: {date}")
            print(f"Monto: {client['monto']}")
            print(f"categoria: {client['categoria']}")
            print(f"Descripcion: {client['descripcion']}")
    else:
        print("NO REGISTRADA")
    tablaBonita=[]
    headers=["FECHA", "MONTO", "CATEGORIA", "TELEFONO"]

    for date, client in filtrarCategoria.items():
        todo=[date, client['monto'], client['categoria'], client['descripcion']]
        tablaBonita.append(todo)
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
