from Modelos.Cuentabancaria import CuentaBancaria

class CuentaBancariaAhorroJoven(CuentaBancaria): # se aplica herencia, heredad de la clase padre CuentaBancaria
    
    def __init__(self, nombre: str, saldo: float, numero_cuenta: str, bonificacion: float):
        super().__init__(nombre, saldo, numero_cuenta)
        # Variable Privada (Caja fuerte)
        self.__bonificacion = bonificacion

    
    # Puente para LEER
    @property
    def bonificacion(self):
        return self.__bonificacion

    # Puente para MODIFICAR
    @bonificacion.setter
    def bonificacion(self, valor):
        self.__bonificacion = valor


    def imprimir_informacion(self) -> str:
        info_base = super().imprimir_informacion() #aplicación de polimorfismo, seagrega la bonificación
        return f"{info_base} y una bonificación de {self.__bonificacion:,.2f}"
    
