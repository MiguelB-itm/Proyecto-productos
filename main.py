from crud import crear_producto, leer_productos, actualizar_producto, eliminar_producto

def menu():
    while True:
        print("\nMenú de Gestión de Productos")
        print("1. Crear producto")
        print("2. Leer productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad disponible: "))
            producto = crear_producto(nombre, descripcion, precio, cantidad)
            print("Producto creado:", producto)
        
        elif opcion == "2":
            productos = leer_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                for producto in productos:
                    print(producto)
        
        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ") or None
            descripcion = input("Nueva descripción (dejar vacío para no cambiar): ") or None
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            precio = float(precio) if precio else None
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            producto_actualizado = actualizar_producto(id_producto, nombre, descripcion, precio, cantidad)
            if producto_actualizado:
                print("Producto actualizado:", producto_actualizado)
            else:
                print("Producto no encontrado.")
        
        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
            print("Producto eliminado.")
        
        elif opcion == "5":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
