def valor_parcelas(valor_inteiro: float, num_parcelas: int):
    valor_parcela = valor_inteiro / num_parcelas
    return valor_parcela


def maior_parcela(parcela_valor: float, valor_inteiro: float, num_parcelas: int) -> float:
    sobra = valor_inteiro % num_parcelas
    parcela_maior = parcela_valor + sobra
    return parcela_maior


def lista_parcelas(parcela: float, num_parcelas: int):
    lista = list()
    for i in range(1, num_parcelas):
        lista += [parcela]
    return lista


def posit_parcela(lista: bytearray, parcela_desigual, parcela: float):
    if parcela_desigual > parcela:
        lista.insert(0, parcela_desigual)
    else:
        lista += [parcela_desigual]
    return lista
