from copy import deepcopy

from .leitura import ler_json


def add_imcs(data: list[dict]) -> list[dict]:
    """ 
        Muito abaixo do peso:  menor que 17 kg/m²
        Abaixo do Peso: Entre 17 kg/m² e 18.4 kg/m²
        Peso normal: Entre 18.5 kg/m² e 29.9 kg/m²
        Acima do peso: Entre 30 kg/m² e 34.9 kg/m²
        Obesidade: Acime de 35 kg/m² 
    """
    data = deepcopy(data)

    return {}


def add_nome_completo(data: list[dict]) -> list[dict]:
    data = deepcopy(data)

    return {}


def add_idade(data: list[dict]) -> list[dict]:
    data = deepcopy(data)

    return {}