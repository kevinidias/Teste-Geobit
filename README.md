# Desafio Programação - Desenvolvedor Python JR
<br>

## Descrição do Desafio

Pedimos que Leiam este documento do começo ao fim e com atenção, pois este foi contruído com o objetivo de avaliar seus conhecimentos técnicos e lógicos em programação. 

Dado o arquivo `data.json` o teste consiste em recuperar todos os dados lá contidos e aplicar a eles funções desenvolvidas por você ao longo desse teste. Entre as funções terão:

* Funções de leitura dos dados;
* Funções de alteração de alguns dados.
* Funções de adição de novos dados;
* Funções de filtragem dos dados;

Vale salientar que todas as funções de leitura, adição e alteração devem funcionar tanto sozinhas quanto em conjunto as outras funções. 

Para testagem foi adotada a linguagem `Python` na versão `3.8` e todos os recursos usados para execução deste desafio deve ser compatível com essa versão.  
<br>

## Funções

1. O nascimento atualmente está como timestamp. Faça uma função que para cada pessoa transforme nascimento para dia/mes/ano.
```python
def atualiza_nascimento_timestamp_para_date_string(data: list[dict]) -> list[dict]:
    ...
```

2. Faça uma função que leia o arquivo JSON e retorne um Dicionário
```python
def ler_json() -> list[dict]:
    ...
```

3. A altura está atualmente armezanada em `centímetros`, faça uma função que format esse valor para `metros`. 
```python
def atualiza_altura_centimentro_para_metros(data: list[dict]) -> list[dict]:
    ...
``` 

4. Faça uma função que adicione a cada pessoa uma chave imc contendo a categoria do IMC pertencente a ela.
``` python
def add_imcs(data: list[dict]) -> list[dict]:
    """ 
        Muito abaixo do peso:  menor que 17 kg/m²
        Abaixo do Peso: Entre 17 kg/m² e 18.4 kg/m²
        Peso normal: Entre 18.5 kg/m² e 29.9 kg/m²
        Acima do peso: Entre 30 kg/m² e 34.9 kg/m²
        Obesidade: Acime de 35 kg/m² 
    """
    ...
```

5. Façã uma função que adicione a cada pessoa o seu nome completo e retire as chaves nome e sobrenome
```python
def add_nome_completo(data: list[dict]) -> list[dict]:
    ...
```

6. Para cada pessoa no dicionário, adicione uma chave idade baseado no campo nascimento.
```python
def add_idade(data: list[dict]) -> list[dict]
    ...
```

7. Faça uma função que mantenha no dicionário somente pessoas maiores de idade e com IMC acima do peso normal.
```python
def filtra_maior_de_idade_com_imc_acima_do_peso(data: list[dict]) -> list[dict]:
    ...
```

8. Faça uma função que mantenha no dicionário somente pessoas do sexo `Feminino` e que moram em `Meeren` no estado de `Braavos`.
```python
def filtra_mulheres_de_meeren_braavos(data: list[dict]) -> list[dict]:
    ...
```

9. **(Bonus)** - A classe `Run` mostrada a seguir tem como objetivo centralizar todas as funções por você criada. Implemente seus métodos baseando-se nas descrições de cada um.
```python
class Run(object):
    json_data = {
        "pessoas": [],
        "filtros": {
            "menores_de_idade_com_imc_acima_peso": [],
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
        ...

    def execute_filtros(self):
        """
            Aplique cada filtro usando como data a variável 
            self.json_data['pessoas'] e adicione o resultado em 
            self.json_data['filtros'] na chave respectiva ao filtro.
        """
        ...

    def dict_to_json(self):
        """
            Transforme o dicionário self.json_data 
            em um arquivo chamado output.json
        """
        ...
```