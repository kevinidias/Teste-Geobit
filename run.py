from desafio import adicoes, atualizacoes, filtros, leitura


if __name__ == '__name__':
    # leitura
    data = leitura.ler_json()

    # atualizacoes
    atualizacoes.atualiza_altura_centimetro_para_metro(data)
    atualizacoes.atualiza_nascimento_timestamp_para_date_string(data)

    # Adições
    adicoes.add_idade(data)
    adicoes.add_imcs(data)
    adicoes.add_nome_completo(data)

    # filtros
    filtros.filtra_maior_de_idade_com_imc_acima_do_peso(data)
    filtros.filtra_mulheres_de_meeren_braavos(data)