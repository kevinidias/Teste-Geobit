from copy import deepcopy
from datetime import datetime


def atualiza_nascimento_timestamp_para_date_string(data):

    datas = deepcopy(data)
    pessoas = datas['pessoas']
    for pessoa in pessoas:
        data_nascimento = pessoa['nascimento']
        data_datetime = datetime.fromtimestamp(data_nascimento)
        data_formatada = data_datetime.strftime("%d/%m/%Y")
        pessoa['nascimento'] = data_formatada

    return datas


"""atualiza = atualiza_nascimento_timestamp_para_date_string()
print(atualiza)"""


def atualiza_altura_centimetro_para_metro(data):
    datas = deepcopy(data)
    pessoas = datas['pessoas']
    for pessoa in pessoas:
        altura = pessoa['altura']
        metros = altura / 100
        pessoa['altura'] = metros

    return datas


"""atualiza = atualiza_altura_centimetro_para_metro()
print(atualiza)"""
