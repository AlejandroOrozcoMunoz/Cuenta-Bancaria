class CuentaBancaria:
    def __init__(self, tasa_interes=0, bal=0): 
        self.tasa = tasa_interes
        self.balance = bal
    def deposito(self, amount):
        self.balance += amount
        return self
    def retiro(self, amount):
        if amount > self.balance:
            print("fondos insuficientes: cargar $5 cobro")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def mostrar_info_cuenta(self):
        print("Balance: $"+str(self.balance))
        return self
    def Generar_interes(self):
        if self.balance>0:
            self.balance*=(self.tasa+1)
        return self

usuario1 = CuentaBancaria(0.01,150)
usuario2 = CuentaBancaria()


usuario1.deposito(100).deposito(150).deposito(200).retiro(80).Generar_interes().mostrar_info_cuenta()
usuario2.deposito(100).deposito(150).retiro(50).retiro(50).retiro(50).retiro(105).Generar_interes().mostrar_info_cuenta()