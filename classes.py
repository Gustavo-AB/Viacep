import requests


class Api:
    def __init__(self, url):
        self.acesso = requests.get(url)
        self.api = self.acesso.json()

    def retornar_cep(self):
        return self.api['cep']

    def retornar_rua(self):
        return self.api['logradouro']

    def retornar_bairro(self):
        return self.api['bairro']

    def retornar_localidade(self):
        return self.api['localidade']

    def retornar_uf(self):
        return self.api['uf']

    def retornar_ddd(self):
        return self.api['ddd']