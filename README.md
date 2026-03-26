# Sistema de Gestión de Inventario (Python)



Este es un programa de consola desarrollado en Python para administrar un inventario de productos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar), calcular estadísticas y persistir los datos en archivos CSV.

##  Características

El sistema ofrece un menú interactivo con las siguientes funcionalidades:

1.  **Gestión de Productos:** Agregar, buscar, actualizar y eliminar artículos.
2.  **Estadísticas:** Cálculo automático de valores totales y análisis del inventario.
3.  **Persistencia de Datos:** 
    *   **Guardar:** Exporta el inventario actual a un archivo `.csv`.
    *   **Cargar:** Importa datos desde un archivo `.csv` con opción de sobrescribir el inventario actual o fusionarlo (sumando cantidades si el producto ya existe).
4.  **Control de Errores:** Manejo de excepciones para entradas no válidas y errores inesperados.

##  Estructura del Proyecto

Para que el programa funcione correctamente, se requiere la siguiente estructura de archivos:

*   `app.py`: Archivo principal que contiene el bucle del menú y la lógica de interacción.
*   `servicios.py`: Contiene las funciones de lógica de negocio (`agregar_producto`, `buscar_producto`, etc.).
*   `archivos.py`: Contiene las funciones de lectura y escritura de archivos (`cargar_csv`, `guardar_csv`).

##  Requisitos

*   Python 3.x instalado.

##  Uso

1. Clona o descarga los archivos del proyecto.
2. Asegúrate de que `servicios.py` y `archivos.py` estén en la misma carpeta que el archivo principal.
3. Ejecuta el programa desde la terminal:
   ```bash
   python app.py

##  Instalación

Para clonar este repositorio, usa el siguiente comando:

```bash
git clone https://github.com/MauriDavi20/HISOTRIA_DE_USUARIO_M1.git

