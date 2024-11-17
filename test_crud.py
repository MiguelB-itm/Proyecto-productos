import unittest
import crud  # Importa las funciones del módulo CRUD
import os
import json

class TestCRUDOperations(unittest.TestCase):

    def setUp(self):
        """ Configura un entorno de pruebas limpio antes de cada prueba """
        self.test_data_path = "data/test_productos.json"
        crud.DATA_PATH = self.test_data_path  # Redirige las funciones CRUD al archivo de pruebas

        # Crea un archivo JSON vacío para las pruebas
        os.makedirs(os.path.dirname(self.test_data_path), exist_ok=True)
        with open(self.test_data_path, "w") as file:
            json.dump([], file)

    def tearDown(self):
        """ Limpia el entorno de pruebas después de cada prueba """
        if os.path.exists(self.test_data_path):
            os.remove(self.test_data_path)

    def test_crear_producto(self):
        """ Prueba para crear un producto """
        producto = crud.crear_producto("Producto1", "Descripción1", 100.0, 10)
        self.assertEqual(producto["nombre"], "Producto1")
        self.assertEqual(producto["descripcion"], "Descripción1")
        self.assertEqual(producto["precio"], 100.0)
        self.assertEqual(producto["cantidad"], 10)

    def test_leer_productos(self):
        """ Prueba para leer productos """
        crud.crear_producto("Producto1", "Descripción1", 100.0, 10)
        productos = crud.leer_productos()
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0]["nombre"], "Producto1")

    def test_actualizar_producto(self):
        """ Prueba para actualizar un producto existente """
        producto = crud.crear_producto("Producto1", "Descripción1", 100.0, 10)
        producto_actualizado = crud.actualizar_producto(producto["id"], nombre="ProductoModificado")
        self.assertIsNotNone(producto_actualizado)
        self.assertEqual(producto_actualizado["nombre"], "ProductoModificado")

        # Intentar actualizar un producto inexistente
        resultado = crud.actualizar_producto(999, nombre="Inexistente")
        self.assertIsNone(resultado)

    def test_eliminar_producto(self):
        """ Prueba para eliminar un producto """
        producto = crud.crear_producto("Producto1", "Descripción1", 100.0, 10)
        resultado = crud.eliminar_producto(producto["id"])
        self.assertTrue(resultado)

        # Intentar eliminar un producto inexistente
        resultado = crud.eliminar_producto(999)
        self.assertTrue(resultado)  # Devuelve True, pero no elimina nada


    def test_crear_producto_error(self):
        """Prueba de error al crear un producto con datos inválidos"""
        with self.assertRaises(ValueError):  # Suponiendo que manejarás este error
            crud.crear_producto("", "Descripción", 100.0, 10)  # Nombre vacío

        with self.assertRaises(ValueError):
            crud.crear_producto("Producto", "Descripción", -50.0, 10)  # Precio negativo


    def test_leer_productos_error(self):
        """Prueba de error al leer productos si el archivo no existe"""
        os.remove(self.test_data_path)  # Elimina el archivo temporalmente
        productos = crud.leer_productos()
        self.assertEqual(productos, [])  # Debe retornar una lista vacía


    def test_actualizar_producto_error(self):
        """Prueba de error al intentar actualizar un producto inexistente"""
        producto_actualizado = crud.actualizar_producto(999, nombre="NuevoNombre")
        self.assertIsNone(producto_actualizado)  # Debe devolver None


    def test_eliminar_producto_error(self):
        """Prueba de error al intentar eliminar un producto inexistente"""
        resultado = crud.eliminar_producto(999)  # ID que no existe
        self.assertTrue(resultado)  # Función debe manejarlo correctamente y retornar True



if __name__ == "__main__":
    unittest.main()
