from exec3Funções import *

valorTotal = float(input('Informe o valor total: '))
parcelasNum = int(input('Informe o número de parcelas: '))

print()

parcelasValor = valor_parcelas(valorTotal, parcelasNum)
parcelasMaior = maior_parcela(parcelasValor, valorTotal, parcelasNum)

parcelasLista = lista_parcelas(parcelasValor, parcelasNum)
parcelasListaPosit = posit_parcela(parcelasLista, parcelasMaior, parcelasValor)

print("O valor das parcelas é:")
for i in range(0, parcelasNum):
    print(f"{i + 1}: R$ {parcelasListaPosit[0 + i]:.2f}")
