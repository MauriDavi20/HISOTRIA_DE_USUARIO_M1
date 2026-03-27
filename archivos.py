import csv

opcion = None
inventario = []
valor_total = 0
cantidad_total = 0

def guardar_csv(inventario,ruta):
    try:
        archivo = open(ruta, "w" ,newline="", encoding="utf-8")
       
        writer = csv.writer(archivo)

        writer.writerow(["nombre", "precio", "cantidad"])
        for producto in inventario:
            writer.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])

        archivo.close()
        print("archivo guardado")

    except:
        print("Error al guardar el archivo")

def cargar_csv(ruta):
    try:
        inventario_local = [] 
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader) 

            for fila in reader:
                producto = {
                    "nombre": fila[0], 
                    "precio": float(fila[1]), 
                    "cantidad": int(fila[2])
                }
                inventario_local.append(producto)
        
        print("Archivo cargado con éxito")
        return inventario_local 
    except Exception as e:
        print(f"Error al cargar: {e}")
        return []
