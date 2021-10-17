import json


def ler_json():
    arquivo_json = open('../data.json', 'r')
    data = json.load(arquivo_json)
    return data

