import random as rd

def jogar():

    print_oppening()

    palavra_secreta = select_secret_word()

    letras_acertadas = ["_" for letra in palavra_secreta]
    numero_letras = (len(palavra_secreta))
    erros = 0
    rodadas = 0
    enforcou = False
    acertou = False

    rodadas = select_dificult()

    print(f"A palavra tem {numero_letras} letras.")
    while(not enforcou and not acertou):

        print(f"Você tem {rodadas} tentativas. Essa é sua {erros + 1} tentativa.")
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == rodadas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Você ganhou")
    else:
        print(f"Você perderu, a palavra secreta era {palavra_secreta}")

def print_oppening():
        print("*************")
        print("Jogo da Forca")
        print("*************")

def select_secret_word():
        arquivo = open("palavras.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        numero = rd.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

def select_dificult():
        dificuldade = int(input("Escolha sua dificuldade 1 - Fácil , 2 - Médio, 3 - Difícil  "))

        if (dificuldade == 1):
            rodadas = 10
        elif (dificuldade == 2):
            rodadas = 8
        else:
            rodadas = 6

        return rodadas

if(__name__=="__main__"):
    jogar()



