import random

print("*******************************")
print("Jogo da adivinhação do Marcelo")
print("*******************************")

secret_number = random.randrange(1, 101)
tentativas = 0
pontuacao = 1000
#definir dificuldade do jogo

print("Qual a dificuldade do seu jogo?")

dificuldade = int(input("(1) - Fácil, (2) - Médio, (3) - Difícil "))

if (dificuldade == 1):
        tentativas = 20
        nome_dificuldade = str("Fácil")
elif (dificuldade == 2):
        tentativas = 15
        nome_dificuldade = str("Médio")
else:
    tentativas = 10
    nome_dificuldade = str("Difícil")
print(f"a dificuldade escolida é: {nome_dificuldade}")

for chances in range(1, tentativas +1):

    print(f"Tentativa {chances} de {tentativas}")
    print(f"Sua pontuação atual é: {pontuacao} pontos")

    chute = int(input("Digite seu número: "))

    acertou = chute == secret_number
    numero_menor = chute < secret_number
    numero_maior = chute > secret_number

    if (acertou):
        print("Você ganhou!")
        print(f"Sua pontuação foi {pontuacao} pontos")
        break
    else:
        if(numero_maior):
            print("O Número digitado é maior que o número secreto")
            pontuacao = abs(pontuacao - chute)
            if (chances == tentativas):
                print(f"O número secreto era {secret_number}")
                print(f"Sua pontuação foi {pontuacao}")
        elif(numero_menor):
            print("O Número digitado é menor que o número secreto")
            pontuacao = abs(pontuacao - chute)
            if (chances == tentativas):
                print(f"O número secreto era {secret_number}")
                print(f"Sua pontuação foi {pontuacao}")




