import random

# Recebendo quantidade de estrelas da constelação
while 1:
    quantidadeEstrelas = int(input('Informe a quantidade de estrelas para formar a constelação (no mínimo 4, no máximo 8): \n'))
    if quantidadeEstrelas >= 4 and quantidadeEstrelas <= 8:
        break
    else:
        print('Informe uma quantidade de estrelas de 4 a 8')


constelacao = []

# Adicionando números aleatórios de 0 a 1 na matriz constelacao
for i in range(quantidadeEstrelas):
    linha = []
    for j in range(quantidadeEstrelas):
        linha.append(random.randint(0,1))

    constelacao.append(linha)

# Retirando alguma possivel ligação de uma estrela com ela mesma
for i in range(quantidadeEstrelas):
    constelacao[i][i] = 0


# Ajustando possíveis ligações isoladas / incompletas
for i in range(quantidadeEstrelas):
    for j in range(quantidadeEstrelas):
        if constelacao[i][j] == 1:
            constelacao[j][i] = 1


# Printando matriz por linha
for estrela in constelacao:
    print(estrela)


print(f'Agora, informe as estrelas que deseja verificar se são diretamente interligadas. (de 0 a {quantidadeEstrelas-1})')

# Recebendo estrelas para teste de ligação
while 1:
    numEstrela1 = int(input('Escolha uma estrela: \n'))
    numEstrela2 = int(input('Escolha outra estrela: \n'))
    if numEstrela1 == numEstrela2:
        print('Escolha estrelas diferentes!')
    elif numEstrela1 >= 0 and numEstrela1 <= quantidadeEstrelas-1 and numEstrela2 >= 0 and numEstrela2 <= quantidadeEstrelas-1:
        print('Estrelas escolhidas:')
        break
    else:
        print(f'Escolha estrelas de 0 a {quantidadeEstrelas-1}!')


estrela1 = constelacao[numEstrela1]
estrela2 = constelacao[numEstrela2]

print(f'Estrela {numEstrela1}: {estrela1}')
print(f'Estrela {numEstrela2}: {estrela2}')

# Testando interligação direta
if estrela1[numEstrela2] == 1 and estrela2[numEstrela1] == 1:
    print('As estrelas são interligadas!')
else:
    print('As estrelas não são interligadas.')