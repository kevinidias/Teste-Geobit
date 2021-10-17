from copy import deepcopy
from datetime import datetime
from datetime import date


def filtra_maior_de_idade_com_imc_acima_do_peso(data):

    datas = deepcopy(data)
    pessoas = datas['pessoas']
    filtro = []
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
        data_nascimento = pessoa['nascimento']
        data_formatada = datetime.fromtimestamp(data_nascimento)
        data_formatada_ano = str(data_formatada)[0:4]
        data_atual = date.today()
        data_formatada_atual = str(data_atual)[0:4]
        idade = int(data_formatada_atual) - int(data_formatada_ano)
        pessoa['idade'] = idade
        if pessoa['idade'] > 18:
            if pessoa[
                'IMC'] == 'Acima do peso':  # trocar por obesidade para ver
                filtro.append(pessoa)

    return filtro


"""filtrar = filtra_maior_de_idade_com_imc_acima_do_peso()
print(filtrar)
"""


def filtra_mulheres_de_meeren_braavos(data):
    datas = deepcopy(data)
    pessoas = datas['pessoas']
    filtro = []
    for pessoa in pessoas:
        if 'F' in pessoa.values():
            if 'Meeren' in pessoa['endereço']['cidade']:
                if 'Braavos' in pessoa['endereço']['estado']:
                    filtro.append(pessoa)

    return filtro


"""filtrar = filtra_mulheres_de_meeren_braavos()
print(filtrar)
"""
