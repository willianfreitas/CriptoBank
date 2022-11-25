from rest_framework.views import APIView
import json
import requests
from .GerenciarUsuario import GerenciamentoUsuarios
from .GerenciarCarteira import GerenciamentoCarteira
from django.http import HttpResponse
from django.core import serializers


class CadastrarUsuario(APIView):
    
    '''
    Cadastrar o Usuario no sistema

    Parametros:
        request(object):
            nome: Nome do Usuário
            email: Email do Usuário
            fone: Telefone do Usuário
    '''

    def post(self, request):

        post_json = json.loads(request.body)
        nomeUsuario = post_json.get('nome')
        emailUsuario = post_json.get('email')

        cadastrar_Usuario = GerenciamentoUsuarios(nomeUsuario=nomeUsuario,emailUsuario=emailUsuario)

        if cadastrar_Usuario.cadastraUsuario():
            return HttpResponse("Usuario cadastrado com sucesso.", content_type="application/json; charset=utf-8")
        return HttpResponse("Usuario já cadastrado em nosso banco de dados", content_type="application/json; charset=utf-8")

class CriarCarteira(APIView):
    '''
    Criar a carteira de um Usuario no sistema

    Parametros:
        request(object):
            nomeUsuario: Nome do Usuario
    '''

    def post(self, request):
        post_json = json.loads(request.body)
        nomeUsuario = post_json.get('nomeUsuario')

        criar_carteora = GerenciamentoCarteira(nomeUsuario=nomeUsuario)

        if criar_carteora.criaCarteira():
            return HttpResponse("Carteira criada com sucesso.", content_type="application/json; charset=utf-8")
        return HttpResponse("Não foi possível criar a carteira. Usuario não encontrado.", content_type="application/json; charset=utf-8")

    
class ConsultaUsuario(APIView):
    '''
    Consulta o cadastro de um Usuario.

    Parametros:
        request(object):
            nomeUsuario: Nome do Usuario
            emailUsuario: Email do Usuario
            foneUsuario: Telefone do Usuario
    '''
    def get(self, request):
        nomeUsuario = self.request.query_params.get('nomeUsuario')
        emailUsuario = self.request.query_params.get('emailUsuario')

        results = GerenciamentoUsuarios(nomeUsuario=nomeUsuario, emailUsuario=emailUsuario).consultaUsuario()

        if results:
            return HttpResponse(json.dumps(results, indent=4), content_type="charset=utf-8")
        return HttpResponse("Usuario não encontrado.", content_type="application/json; charset=utf-8")

class ConsultaCarteira(APIView):

    '''
    Consulta uma carteira com seus ativos registrados e seus valores

    Parametros:
        request(object):
            idCarteira: ID da Carteira
    '''

    def get(self, request):

        idCarteira = self.request.query_params.get('idCarteira')

        results = GerenciamentoCarteira(idCarteira=idCarteira).consultaAtivo()

        if results:
            results = serializers.serialize('json', results)
            return HttpResponse(json.dumps(results), content_type="charset=utf-8")
        return HttpResponse("Carteira não encontrada.", content_type="application/json; charset=utf-8")


class registrarAtivos(APIView):

    '''
    Cadastrar ativos na carteira do usuário.

    Parametros:
        request(object):
            idCarteira: ID da Carteira
            cripto: Nome da Moeda
            valor: Valor comprado
    '''
    
    def post(self, request):
        post_json = json.loads(request.body)
        idCarteira = post_json.get('idCarteira')
        cripto = post_json.get('cripto')
        valor = post_json.get('valor')

        result = GerenciamentoCarteira(idCarteira=idCarteira, cripto=cripto, value=valor)

        if result.registrarAtivo():
            return HttpResponse("Ativo registrado com sucesso", content_type="application/json; charset=utf-8")
        return HttpResponse("Carteira não encontrada.", content_type="application/json; charset=utf-8")
