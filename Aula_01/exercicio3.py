notaUm = int(input("Digite a nota do primeiro bimestre da disciplina: "))
notaDois = int(input("Digite a nota do segundo bimestre da disciplina: "))

peso1 = 2
peso2 = 3

mediaParc = (notaUm * peso1 + notaDois * peso2) / (peso1 + peso2)

print ("Média parcial = ", int(mediaParc))