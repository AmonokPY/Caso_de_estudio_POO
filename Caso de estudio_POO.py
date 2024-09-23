class Products:
    #AGREGARMOS UN COMENTARIO
    def __init__(self):
        # Inicializa las variables privadas para almacenar el nombre, valor y el inventario
        self.__key: str = ""  # Nombre del producto
        self.__value: int = 0  # Valor del producto
        self.__inventory = {}  # Diccionario para almacenar el inventario

    def add_inventory(self):
        # Permite agregar productos al inventario solicitando el nombre y el valor
        print(
            '----Digite primero el nombre del producto y después el valor, para salir digite "termine"----'
        )
        while True:
            self.__key = input("Digite el nombre del producto: ")
            if self.__key.lower() == "termine":  # Salir si el usuario escribe "termine"
                break
            while True:
                try:
                    self.__value = int(
                        input("Digite el valor del producto, sin comas: ")
                    )
                    break
                except ValueError:
                    print(
                        "Valor erróneo. Por favor, ingrese un número entero sin comas."
                    )

            # Agregar el producto y su valor al diccionario de inventario
            self.__inventory[self.__key] = self.__value

    def show_inventory(self):
        # Muestra todos los productos en el inventario
        print("Inventario actual:")
        for key, value in self.__inventory.items():
            print(f"Producto: {key}, Valor: {value}")

    def addition_inventory(self):
        # Calcula el valor total del inventario sumando los valores de todos los productos
        return sum(self.__inventory.values())

    # ---------------------- Uso de decoradores (@property y @setter) ----------------------
    # Getter para obtener el inventario
    @property
    def inventory(self):
        # El decorador @property convierte este método en una propiedad de solo lectura.
        # Esto significa que ahora podemos acceder a __inventory directamente como si
        # fuera un atributo, pero manteniendo la encapsulación.
        return self.__inventory

    # Setter para modificar el inventario
    @inventory.setter
    def inventory(self, inventory):
        # El decorador @inventory.setter define un setter que permite asignar un nuevo valor
        # a __inventory. Así, podemos controlar cómo se modifica esta variable desde fuera
        # de la clase y mantener la validación si fuera necesario.
        self.__inventory = inventory


class Employees:
    def __init__(self, num_employees: int, num_types_employees: int):
        # Inicializa el número de empleados y tipos de empleados (niveles de salario)
        self.__num_employees = num_employees
        self.__num_types_employees = num_types_employees
        self.__employees = {}

    def salario(self):
        # Pide el salario y el número de empleados por tipo, y los almacena en un diccionario
        for i in range(1, self.__num_types_employees + 1):
            while True:
                try:
                    salario = float(
                        input(f"Digite el salario del tipo de empleado #{i}: ")
                    )
                    break
                except ValueError:
                    print("Digite un número válido para el salario.")

            while True:
                try:
                    num = int(input("Digite el número de empleados con ese salario: "))
                    break
                except ValueError:
                    print("Digite un número válido para el número de empleados.")

            # Agregar empleados de este tipo con su respectivo salario al diccionario
            for j in range(num):
                self.__employees[f"empleado {i}_{j + 1}"] = salario

    def show_employees(self):
        # Muestra el número de empleados actuales y sus salarios
        print("Número de empleados actuales:")
        for key, value in self.__employees.items():
            print(f"Empleado: {key}, Salario: {value}")

    def addition_salary(self):
        # Calcula el costo total de los salarios sumando todos los salarios del diccionario
        return sum(self.__employees.values())

    # ---------------------- Uso de decoradores (@property y @setter) ----------------------

    # Getter para obtener el diccionario de empleados
    @property
    def employees(self):
        # @property permite acceder a __employees como si fuera un atributo, sin necesidad
        # de llamar explícitamente a un método. Ideal para mantener la encapsulación y
        # controlar el acceso a datos sensibles.
        return self.__employees

    # Setter para modificar el diccionario de empleados
    @employees.setter
    def employees(self, employees):
        # @setter permite definir cómo se debe modificar el atributo __employees desde
        # fuera de la clase. Con esto, se puede hacer validaciones o transformaciones
        # antes de cambiar el valor real.
        self.__employees = employees

    # Getter para obtener el número de empleados
    @property
    def num_employees(self):
        return self.__num_employees

    # Setter para modificar el número de empleados
    @num_employees.setter
    def num_employees(self, num_employees):
        self.__num_employees = num_employees

    # Getter para obtener el número de tipos de empleados
    @property
    def num_types_employees(self):
        return self.__num_types_employees

    # Setter para modificar el número de tipos de empleados
    @num_types_employees.setter
    def num_types_employees(self, num_types_employees):
        self.__num_types_employees = num_types_employees


class Administration(Products, Employees):  # multiherencia
    def __init__(self, num_employees: int, num_types_employees: int, name: str):
        # Inicializa las clases heredadas y asigna el nombre de la administración y las ventas
        Products.__init__(self)
        Employees.__init__(self, num_employees, num_types_employees)
        self.__name = name
        self.__sales = 0  # Para registrar las ventas

    def add_sales(self):
        # Pide el monto de ventas y lo almacena
        while True:
            try:
                self.__sales = float(input("Digite el monto total de ventas: "))
                break
            except ValueError:
                print("Digite un número válido para el monto de ventas.")

    def calculate_profit(self):
        # Calcula la ganancia restando los gastos (inventario + salarios) de las ventas
        total_expenses = self.addition_inventory() + self.addition_salary()
        profit = self.__sales - total_expenses
        return profit

    def show_summary(self):
        # Muestra el resumen de la administración: inventario, empleados, ventas, gastos y ganancia
        print(f"Nombre de la Administración: {self.__name}")
        self.show_inventory()
        self.show_employees()
        print(f"Total Ventas: {self.__sales}")
        print(f"Total Gastos: {self.addition_inventory() + self.addition_salary()}")
        print(f"Ganancia: {self.calculate_profit()}")

    # ---------------------- Uso de decoradores (@property y @setter) ----------------------

    # Getter para obtener el nombre de la administración
    @property
    def name(self):
        # Este @property permite acceder a __name como si fuera un atributo, manteniendo
        # la encapsulación, es decir, la capacidad de controlar cómo se accede y modifica
        # este valor.
        return self.__name

    # Setter para modificar el nombre de la administración
    @name.setter
    def name(self, name):
        # Permite modificar el nombre de la administración. Puedes agregar validaciones
        # si se desea restringir qué tipo de valores se pueden asignar a __name.
        self.__name = name

    # Getter para obtener las ventas
    @property
    def sales(self):
        # El decorador @property permite acceder a __sales sin necesidad de usar un método,
        # lo que simplifica el código al trabajar con este valor como si fuera un atributo público.
        return self.__sales

    # Setter para modificar las ventas
    @sales.setter
    def sales(self, sales):
        # Permite modificar el valor de las ventas. Nuevamente, puedes agregar validaciones
        # si es necesario.
        self.__sales = sales


# Crear una instancia de la clase Administration y ejecutar los métodos
admin = Administration(
    4, 2, "Mi Empresa"
)  # Inicializa con 4 empleados y 2 tipos de salarios
admin.add_inventory()  # Agregar productos al inventario
admin.salario()  # Ingresar salarios de empleados
admin.add_sales()  # Registrar ventas
admin.show_summary()  # Mostrar resumen de administración: inventario, empleados, ventas, gastos y ganancia

#AGREMAMOS AL FINAL UN COMENTARIO

