from copy import deepcopy
from datetime import datetime
from datetime import date

from leitura import ler_json


def add_imcs(data):
    """Muito abaixo do peso:  menor que 17 kg/m²
        Abaixo do Peso: Entre 17 kg/m² e 18.4 kg/m²
        Peso normal: Entre 18.5 kg/m² e 29.9 kg/m²
        Acima do peso: Entre 30 kg/m² e 34.9 kg/m²
        Obesidade: Acime de 35 kg/m² """

    datas = deepcopy(data)
    pessoas = datas['pessoas']
    for pessoa in pessoas:
        peso = pessoa['peso']
        if peso < 17:
            pessoa['IMC'] = 'Muito abaixo do peso'
        elif 17 < peso < 18.4:
            pessoa['IMC'] = 'Abaixo do peso'
        elif 18.5 < peso < 29.9:
            pessoa['IMC'] = 'Peso normal'
        elif 30 < peso < 34.9:
            pessoa['IMC'] = 'Acima do peso'
        else:
            pessoa['IMC'] = 'Obesidade'

    return datas



def add_nome_completo(data):

    datas = deepcopy(data)
    pessoas = datas['pessoas']
    for pessoa in pessoas:
        nome = pessoa['nome']
        sobrenome = pessoa['sobrenome']
        nome_completo = nome + " " + sobrenome
        pessoa['Nome completo'] = nome_completo
        pessoa.pop('nome')
        pessoa.pop('sobrenome')

    return datas


"""add = add_nome_completo()
print(add)"""


def add_idade(data):

    datas = deepcopy(data)
    pessoas = datas['pessoas']
    for pessoa in pessoas:
        data_nascimento = pessoa['nascimento']
        data_formatada = datetime.fromtimestamp(data_nascimento)
        data_formatada_ano = str(data_formatada)[0:4]
        data_atual = date.today()
        data_formatada_atual = str(data_atual)[0:4]
        idade = int(data_formatada_atual) - int(data_formatada_ano)
        pessoa['idade'] = idade

    return datas


"""add = add_idade()
print(add)"""
