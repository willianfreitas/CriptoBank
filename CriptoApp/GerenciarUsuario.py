from CriptoApp.models import Client, Registers, Wallet
from django.db.models import Sum

class GerenciamentoUsuarios:

    def __init__(self, nomeUsuario:str=None, emailUsuario:str=None):
        self.nomeUsuario = nomeUsuario
        self.emailUsuario = emailUsuario
    
    def cadastraUsuario(self) -> bool:
        
        aux = Client.objects.filter(email=self.emailUsuario)
        
        if not aux:
            Client.objects.create(name=self.nomeUsuario, email=self.emailUsuario)
            return True
        return False

    def consultaUsuario(self):

        if self.nomeUsuario:
            usuario = Client.objects.filter(name=self.nomeUsuario).all().values()
        elif self.emailUsuario:
            usuario = Client.objects.filter(email=self.emailUsuario).all().values()
        else:
            return False
        
        carteira = Wallet.objects.filter(idclient=usuario[0]['idclient']).all().values('idwallet')
        saldo = Registers.objects.filter(idwallet=carteira[0]['idwallet']).aggregate(Sum('value'))

        aux = usuario[0]
        aux['saldo'] = saldo['value__sum']
        
        return aux

