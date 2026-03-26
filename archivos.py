import csv

opcion = None
inventario = []
valor_total = 0
cantidad_total = 0

def guardar_csv(inventario,ruta):
    try:
        archivo = open(ruta, "w" ,newline="", encoding="utf-8")
       
        writer = csv.writer(archivo)

        writer.writerow(["nombre", "precio unitario", "cantidad"])
        for producto in inventario:
            writer.writerow([producto["nombre"], producto["precio unitario"], producto["cantidad"]])

        archivo.close()
        print("archivo guardado")

    except:
        print("Error al guardar el archivo")

    
def cargar_csv(ruta):
    try:
        archivo = open(ruta, "r" , encoding="utf-8")
        reader =csv.reader(archivo)

        next(reader)

        for fila in reader:
            producto = {"nombre": fila[0], "precio unitario": float(fila[1]), "cantidad": int(fila[2])}

            inventario.append(producto)

            archivo.close()
            print("archivo cargado")
            return inventario
    except:
      print("Error al cargar el archivo")
      return[]