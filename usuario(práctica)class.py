#Poner en práctica la creación de clases e instancias
#Poner en práctica la invocación de métodos y acceso a atributos desde distintas instancias
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("La compra fue rechazada por exceder el límite de crédito")
#pagar_tarjeta(self, monto): crea un método que pague un monto de la tarjeta de crédito, haciendo que se 
# reduzca el saldo_pagar.

    def pagar_tarjeta(self, monto):
        if self.saldo_pagar - monto >= 0:
            self.saldo_pagar -= monto
        else:
            print("El monto del pago execede el saldo pendiente", "saldo pendiente:", self.saldo_pagar)

#mostrar_saldo_usuario(self): crea un método que imprima el nombre completo del usuario 
# y el saldo a pagar de su tarjeta.Ejemplo: “Usuario: Nariyoshi Miyagi, Saldo a Pagar: $50”
    def mostrar_saldo(self):
        print("Usuario:", self.nombre, self.apellido, "Saldo a pagar:", self.saldo_pagar)

#BONUS: transferir_deuda(self, otro_usuario, monto): crea un método que reduzca la deuda 
# (saldo_pagar) del usuario por el monto, y agrega esa cantidad al saldo_pagar de otro_usuario
    def transferir_deuda(self, otro_usuario, monto):
        if monto > self.saldo_pagar:
            print("No se puede transferir más deuda que la que de debe. Saldo pendiente:", self.saldo_pagar)
        else:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto
            print(self.nombre, self.apellido, "ha transferido", monto, "a", otro_usuario.nombre, otro_usuario.apellido)

usuario1 = Usuario("Mathias", "Ortiz", "jxJtF@example.com")
usuario2 = Usuario("Jorge", "Ortiz", "jxF@example.com")
usuario3= Usuario("Julio", "Mendoza", "gdiaol@example.com")

#Haz que el primer usuario haga 2 compras y luego pague su tarjeta. Muestra su saldo
usuario1.hacer_compra(2000)
usuario1.hacer_compra(400)
usuario1.pagar_tarjeta(2400)
usuario1.mostrar_saldo()

#Haz que el segundo usuario haga 1 compra y luego pague 2 veces su tarjeta. Muestra su saldo
usuario2.hacer_compra(1000)
usuario2.pagar_tarjeta(800)
usuario2.pagar_tarjeta(1000)
usuario2.mostrar_saldo()

#Haz que el tercer usuario haga 3 compras y luego pague su tarjeta 4 veces. Muestra su saldo
usuario3.hacer_compra(1000)
usuario3.hacer_compra(10000)
usuario3.hacer_compra(1200)
usuario3.pagar_tarjeta(4000)
usuario3.pagar_tarjeta(1000)
usuario3.pagar_tarjeta(3000)
usuario3.pagar_tarjeta(600)
usuario3.mostrar_saldo()
