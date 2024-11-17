import json
import os

# Ruta al directorio y archivo JSON
DATA_DIR = "data"
DATA_PATH = os.path.join(DATA_DIR, "productos.json")

# Asegúrate de que el directorio y el archivo existan
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if not os.path.exists(DATA_PATH):
    with open(DATA_PATH, "w") as file:
        json.dump([], file)

# Función para cargar datos del archivo JSON
def cargar_datos():
    with open(DATA_PATH, "r") as file:
        return json.load(file)

# Función para guardar datos en el archivo JSON
def guardar_datos(productos):
    with open(DATA_PATH, "w") as file:
        json.dump(productos, file, indent=4)

# Crear un producto
def crear_producto(nombre, descripcion, precio, cantidad):
    productos = cargar_datos()
    nuevo_producto = {
        "id": len(productos) + 1,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "cantidad": cantidad,
    }
    productos.append(nuevo_producto)
    guardar_datos(productos)
    return nuevo_producto

# Leer todos los productos
def leer_productos():
    return cargar_datos()

# Actualizar un producto
def actualizar_producto(id_producto, nombre=None, descripcion=None, precio=None, cantidad=None):
    productos = cargar_datos()
    for producto in productos:
        if producto["id"] == id_producto:
            if nombre: producto["nombre"] = nombre
            if descripcion: producto["descripcion"] = descripcion
            if precio is not None: producto["precio"] = precio
            if cantidad is not None: producto["cantidad"] = cantidad
            guardar_datos(productos)
            return producto
    return None

# Eliminar un producto
def eliminar_producto(id_producto):
    productos = cargar_datos()
    original_count = len(productos)
    productos = [producto for producto in productos if producto["id"] != id_producto]
    if len(productos) == original_count:
        return False  # No se eliminó nada
    guardar_datos(productos)
    return True

