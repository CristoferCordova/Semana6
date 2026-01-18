from Modelos.Cuentabancaria import CuentaBancaria
from Modelos.CuenttaBancariaAhorroJoven import CuentaBancariaAhorroJoven

class Transacciones:
    def transferir(self, cuenta_origen: CuentaBancaria, cuenta_destino: CuentaBancaria, monto: float) -> None:
        # Usamos .saldo (el puente)
        if cuenta_origen.saldo >= monto:
            cuenta_origen.saldo -= monto
            cuenta_destino.saldo += monto
        else:
            raise ValueError("Saldo insuficiente para la transferencia")
        
    def depositar(self, cuenta: CuentaBancaria, monto: float) -> None:
        cuenta.saldo += monto

    def retirar(self, cuenta: CuentaBancaria, monto: float) -> None:
        if cuenta.saldo >= monto:
            cuenta.saldo -= monto
        else:
            raise ValueError("Saldo insuficiente para el retiro")
        
    def bonificar(self, cuenta: CuentaBancariaAhorroJoven, bonificacion: float) -> None:
        # Aquí usamos los puentes .bonificacion y .saldo
        cuenta.bonificacion += bonificacion
        cuenta.saldo += bonificacion