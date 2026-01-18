from dataclasses import dataclass

#Se cree la clase CuentaBancaria con los atributos nombre, saldo y numero_cuenta
@dataclass
class CuentaBancaria:
    __nombre : str # se aplica un encapsulamiento 
    __saldo :float
    __numero_cuenta : str

    def imprimir_informacion(self) -> str:
        return f"Cuenta {self.__numero_cuenta} de {self.__nombre} tiene un saldo de ${self.__saldo:,.2f}"

    
    # Puente para leer el saldo
    @property
    def saldo(self):
        return self.__saldo

    # Puente para modificar el saldo (validando que sea número)
    @saldo.setter
    def saldo(self, nuevo_saldo):
        self.__saldo = float(nuevo_saldo)

    # Puente para leer el numero de cuenta
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    # Puente para leer el nombre
    @property
    def nombre(self):
        return self.__nombre