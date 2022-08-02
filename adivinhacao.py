import random

def jogar():
    print("*********************")
    print("Jogo da adivinhação")
    print("*********************")

    # gera_aleatorio = random.random() * 100  minha solução !!!
    # numero_secreto = round(gera_aleatorio)

    numero_secreto = random.randrange(1,101)
    numero_tentativas = 0
    pontos = 1000

    print("Qual nível você quer?")
    print("(1) Fácil, (2) Médio , (3) Difícil")

    nivel= int(input("Defina um nível: "))

    if (nivel == 1):
        numero_tentativas = 20
    elif(nivel == 2):
        numero_tentativas = 15
    elif(nivel == 3):
        numero_tentativas = 5

    for rodada in range(1, numero_tentativas + 1): #for, por enquanto pode ser usado para limitar, diferente do while
        print(f"Tentativa {rodada} de {numero_tentativas}")
        chute = input("Digite um numero entre 1 e 100: ")
        chute_int = int(chute)
        if (chute_int < 1 or chute_int > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue #sai do laço mas não encerra

        maior = numero_secreto < chute_int
        menor = numero_secreto > chute_int
        acertou = numero_secreto == chute_int

        if (acertou):
            print("Parabéns, você acertou")
            print(f"Você fez {pontos}")
            break #Encerra o laço
        else:
            if (maior):
                print("O Número digitado é maior que o correto")
                if(rodada == numero_tentativas):
                    print(print(f"O Número secreto era {numero_secreto} e você fez {pontos} pontos"))
            elif (menor):
                print("O Número digitado é menor que o correto")
                if (rodada == numero_tentativas):
                    (print(f"O Número secreto era {numero_secreto} e você fez {pontos} pontos"))
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos
    print("Fim de jogo")
if(__name__ == "__main__" ):
    jogar()