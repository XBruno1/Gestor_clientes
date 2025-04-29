import csv
import config as config

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} (DNI: {self.dni})"

class Clientes:
    lista_clientes = []

    @classmethod
    def cargar(cls):
        cls.lista_clientes.clear()
        try:
            with open(config.DATABASE_PATH, newline="", encoding="utf-8") as fichero:
                reader = csv.reader(fichero, delimiter=";")
                cls.lista_clientes = [Cliente(dni, nombre, apellido) for dni, nombre, apellido in reader]
        except FileNotFoundError:
            cls.lista_clientes = []

    @classmethod
    def guardar(cls):
        with open(config.DATABASE_PATH, "w", newline="", encoding="utf-8") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            writer.writerows((c.dni, c.nombre, c.apellido) for c in cls.lista_clientes)

    @classmethod
    def buscar(cls, dni):
        return next((cliente for cliente in cls.lista_clientes if cliente.dni == dni), None)

    @classmethod
    def crear(cls, dni, nombre, apellido):
        if cls.buscar(dni):
            raise ValueError(f"El cliente con DNI {dni} ya existe.")
        nuevo_cliente = Cliente(dni, nombre, apellido)
        cls.lista_clientes.append(nuevo_cliente)
        cls.guardar()
        return nuevo_cliente

    @classmethod
    def modificar(cls, dni, nombre, apellido):
        cliente = cls.buscar(dni)
        if cliente:
            cliente.nombre = nombre
            cliente.apellido = apellido
            cls.guardar()
            return cliente
        return None

    @classmethod
    def borrar(cls, dni):
        cliente = cls.buscar(dni)
        if cliente:
            cls.lista_clientes.remove(cliente)
            cls.guardar()
            return cliente
        return None

    def __init__(self):
        self.cargar()

# Cargar los clientes al importar el módulo
Clientes.cargar()
