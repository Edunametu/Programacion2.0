class Cliente():
    nombre=""
    apellido=""
    saldo=0
    def _init_(self, nombre,apellido,saldo):
        self.nombre=nombre 
        self.apellido=apellido
        self.saldo=saldo
    def transferir(self,monto,cuenta):
        if self.saldo>0 & self.saldo>monto:
            saldo=-monto
        else:
            print("saldo insuficiente")    
    

Cliente1=Cliente("marco","lamas",2000)
Cliente1.transferir()
