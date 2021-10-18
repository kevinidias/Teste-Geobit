import json

from leitura import ler_json

from adicoes import add_imcs, add_idade, add_nome_completo
from atualizacoes import (
    atualiza_altura_centimetro_para_metro,
    atualiza_nascimento_timestamp_para_date_string
)
from filtros import (
    filtra_maior_de_idade_com_imc_acima_do_peso,
    filtra_mulheres_de_meeren_braavos
)


class Run(object):
    json_data = {
        "pessoas": [],
        "filtros": {
            "maior_de_idade_com_imc_acima_peso": [],
            "mulheres_meeren_braavos": []
        }
    }

    def __init__(self, data):
        ...

    def execute_adicoes_e_atualizacoes(self):
        """
            Leia o arquivo json usando a função ler_json e acima do
            retorno aplique todas as adições e atualizações. Por fim,
            adicione todas as pessoas já formatadas ao
            self.json_data['pessoas']
        """
        data = ler_json()
        imc = add_imcs(data)
        idade = add_idade(imc)
        nome_completo = add_nome_completo(idade)
        cent_metro = atualiza_altura_centimetro_para_metro(nome_completo)
        data_string = atualiza_nascimento_timestamp_para_date_string(cent_metro)

        self.json_data['pessoas'] = data_string
        return data_string

    def execute_filtros(self):
        """
            Aplique cada filtro usando como data a variável 
            self.json_data['pessoas'] e adicione o resultado em 
            self.json_data['filtros'] na chave respectiva ao filtro.
        """
        data = self.json_data['pessoas']
        maior_idade = filtra_maior_de_idade_com_imc_acima_do_peso(data)
        filtra_mulheres = filtra_mulheres_de_meeren_braavos(data)
        self.json_data['filtros'][
            'maior_de_idade_com_imc_acima_peso'] = maior_idade
        self.json_data['filtros'][
            'mulheres_meeren_braavos'] = filtra_mulheres

    def dict_to_json(self):
        """
            Transforme o dicionário self.json_data
            em um arquivo chamado output.json
        """
        with open("output.json", "w") as outfile:
            json.dump(self.json_data, outfile)
