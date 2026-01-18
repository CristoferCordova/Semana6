from Modelos.Cuentabancaria import CuentaBancaria
from Modelos.CuenttaBancariaAhorroJoven import CuentaBancariaAhorroJoven    
from Servicios.Transacciones import Transacciones

def main():
    cuenta1 = CuentaBancaria("Juan Perez", 1000.0, "123-456-789")
    cuenta2 = CuentaBancariaAhorroJoven("Ana Gomez", 500.0, "987-654-321", 50.0)
    transacciones = Transacciones()
    print("Información inicial de las cuentas:")
    print(cuenta1.imprimir_informacion())
    print(cuenta2.imprimir_informacion())
    transacciones.depositar(cuenta1, 200.0)
    transacciones.retirar(cuenta2, 100.0)
    transacciones.transferir(cuenta1, cuenta2, 300.0) 
    transacciones.bonificar(cuenta2, 25.0)
    print("\nInformación de las cuentas después de las transacciones:")
    print(cuenta1.imprimir_informacion())   
    print(cuenta2.imprimir_informacion())

    transacciones.retirar(cuenta2, 100)
if __name__ == "__main__":
    main()

