#1 creamos otro archivo donde guardaremos las funciones usadas en este programa. 
# Usamos import y el nombre del archivo para poder invocar las funciones en este codigo.
from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto,eliminar_producto,calcular_estadisticas
from archivos import cargar_csv,guardar_csv


#2 inicializamos las variables globales: inventario, los contadores de valor_total y cantidad_total,
# E inicializamos opcion = None para que nos funcione de manera correcta dentro del while.
opcion = None
inventario = []
nombre = None
precio = None
cantidad = None

#3 usamos el bucle while para que  nos aparezca el menu hasta que el usuario presione 4 para salir del programa.
while opcion != 9:
    print("="*60)
    print("REGISTRO DE INVENTARIO".center(60))
    print("="*60)
    print("1. Agregar productos")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto ")
    print("6. Calcular estadisticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
#4 utilizamos try y except para validar que el usuario coloque un numero valido y otro para un error inesperado
    try:
        opcion = int(input("\n¿qué acción desea realizar? opciones (1-9): "))

        if opcion == 1:
            agregar_producto(inventario,nombre,precio,cantidad)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            producto = buscar_producto(inventario)

            if producto is None:
                print("Producto no encontrado")
            else:
                print("-"*60)
                print(f"Nombre: {producto['nombre']}")
                print(f"Precio: {producto['precio']}")
                print(f"Cantidad: {producto['cantidad']}")

            input("Presione ENTER para volver al menú")

        elif opcion == 4:
            actualizar_producto(inventario)

        elif opcion == 5:
            nombre = input("Nombre del producto:")
            eliminar_producto(inventario,nombre)

        elif opcion == 6:
            calcular_estadisticas(inventario)
            input("Presione ENTER para volver al menu")

        elif opcion == 7:
            ruta = input("Nombre del archivo: ")
            if not ruta.endswith(".csv"):
                ruta += ".csv"

            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Nombre del archivo: ").strip()

            if not ruta.lower().endswith(".csv"):
                ruta += ".csv"
                
            nuevos = cargar_csv(ruta)

            if nuevos:
                respuesta = input("¿Sobrescribir inventario actual? (S/N): ").lower()

                if respuesta == "s":
                    inventario = nuevos
                    print("Inventario reemplazado.")
                else:
                    for nuevo in nuevos:
                        encontrado = False

                        for producto in inventario:
                            if producto["nombre"].lower() == nuevo["nombre"].lower():
                                producto["cantidad"] += nuevo["cantidad"]
                                producto["precio"] = nuevo["precio"]
                                encontrado = True
                                break

                        if not encontrado:
                            inventario.append(nuevo)

                    print("Inventario fusionado.")

            input("Presione ENTER para volver al menú")

        elif opcion < 1 or opcion > 9:
            print("Opción inválida")
            input("Presione ENTER")

    except ValueError:
        print("Error: Debe ingresar un número válido")
        input("Presione ENTER")

    except Exception as e:
        print("Error inesperado:", e)
        input("Presione ENTER")

print("-"*60)
print("Hasta luego!")