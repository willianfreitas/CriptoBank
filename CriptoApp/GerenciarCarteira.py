from CriptoApp.models import Client, Registers, Wallet

class GerenciamentoCarteira:

    def __init__(self, idCarteira:int=None, nomeUsuario:str=None, cripto:str=None, value:float=None):
        self.idCarteira = idCarteira
        self.nomeUsuario = nomeUsuario
        self.cripto = cripto
        self.valor = value

    def criaCarteira(self):
        
        aux = Client.objects.filter(name=self.nomeUsuario).all().values("idclient")

        if aux:
            Wallet.objects.create(idclient=aux[0]['idclient'])
            return True
        else: 
            return False

    def consultaCarteira(self):
        
        if self.idCarteira:
            results = Registers.objects.filter(idwallet=self.idCarteira).all()
        else:
            idCarteira = Wallet.objects.filter(idclient=self.nomeUsuario).all()
            results = Registers.objects.filter(idwallet=idCarteira).all()

        return results

    def registrarAtivo(self):

        aux = Wallet.objects.filter(idwallet=self.idCarteira).all().values("idwallet")

        if aux:
            Registers.objects.create(idwallet=aux[0]['idwallet'], cripto=self.cripto, value=self.valor)
            return True
        else:
            return False

    def consultaAtivo(self):

        result = Registers.objects.filter(idwallet=self.idCarteira).all()

        if result:
            return result
        else:
            return False


