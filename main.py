from classes import *


print('=-'*15)
print(f'{"Consultar CEP":^30}')
print('=-'*15)

while True:
    try:
        cep = str(input('Digite seu cep: '))
        via_cep = Api(f'https://viacep.com.br/ws/{cep}/json')
    except:
        print('Algo deu errado! Verifique se está tudo certo.')
    else:
        print('=-'*15)
        print(f'CEP: {via_cep.retornar_cep()}')
        print(f'Logradouro: {via_cep.retornar_rua()}')
        print(f'Bairro: {via_cep.retornar_bairro()}')
        print(f'Localidade: {via_cep.retornar_localidade()}')
        print(f'Uf: {via_cep.retornar_uf()}')
        print(f'DDD: {via_cep.retornar_ddd()}')
        break

