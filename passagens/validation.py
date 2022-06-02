from datetime import datetime


def origem_destino_iguais(origem, destino, lista_de_erros):
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino devem ser diferentes.'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = "Não inclua números neste campo."


def data_ida_maior_que_data_volta(data_ida: datetime, data_volta: datetime, lista_erros: dict):
    if data_ida > data_volta:
        lista_erros['data_ida'] = "Data de ida não pode ser maior que a data de volta"


def data_ida_menor_que_data_pesquisa(data_ida: datetime, data_pesquisa: datetime, lista_erros: dict):
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = "Data de ida não pode ser menor que a data de hoje"
