import json

class StockInvalidError(Exception):
    pass

class DispositivoEcologico():

    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.__stock = 0
        self.asignar_stock(stock)

    def asignar_stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidError("El stock no puede ser negativo")
        self.__stock = nuevo_stock

    def obtener_stock(self):
        return self.__stock

    def mostrar_ficha_tecnica(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {self.obtener_stock()} unidades"

class PanelSolar(DispositivoEcologico):

    def __init__(self, codigo: str, nombre: str, precio: float, stock: int, potencia_watts: float, eficiencia: float):
        super().__init__(codigo, nombre, precio, stock)

        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    def mostrar_ficha_tecnica(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {self.obtener_stock()} unidades | Potencia: {self.potencia_watts} | Eficiencia: {self.eficiencia}"

class GestorInventario():

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):

        catalogo = []
        for dispositivo in lista_dispositivos:
            producto = {
                "codigo": dispositivo.codigo,
                "nombre": dispositivo.nombre,
                "precio": dispositivo.precio,
                "stock": dispositivo.obtener_stock(),
            }
            if type(dispositivo) == PanelSolar:

                producto["potencia_wattts"] = dispositivo.potencia_watts
                producto["eficiencia"] = dispositivo.eficiencia
            catalogo.append(producto)
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            json.dump(catalogo, file, indent=4)

        print ("Catalogo guardado correctamente en la ruta del main.py")
        print("-" * 60)

"""
Instancias de objetos de prueba
"""

panel1 = PanelSolar(
    "PS-001",
    "Panel Solar Residencial",
    50_000,
    15,
    450,
    21.5
)

panel2 = PanelSolar(
    "PS-002",
    "Panel Solar Industrial",
    120_000,
    8,
    600,
    23.5
)

dispositivo1 = DispositivoEcologico(
    "DE-001",
    "Filtro de Agua",
    85_000,
    5
)

"""
Prueba de errores para no permitir stock negativo
y generar inconsistencias en el inventario.
"""
try:
    panel_invalido = PanelSolar(
        "PS-003",
        "Panel Solar Defectuoso",
        400_000,
        -5,
        850,
        26.5
    )
except StockInvalidError as error:
    print("-" * 60)
    print(f"Error controlado: {error}")

try:
    panel1.asignar_stock(-5)
except StockInvalidError as error:
    print("-" * 60)
    print(f"Error controlado: {error}")
    print("-" * 60)

productos = [panel1, panel2, dispositivo1]
print("Ficha técnica de productos:")
print("-" * 60)
for producto in productos:
    print(producto.mostrar_ficha_tecnica())
print("-" * 60)

"""
Bloque para probar la exportación de los productos al archivo JSON
que consiste en instanciar la clase y luego llamar al método
pasando la lista de productos y el nombre de archivo a guardar (persistencia)
"""

gestorinv = GestorInventario()

gestorinv.guardar_catalogo_json(productos, "catalogo_ecotech.json")

