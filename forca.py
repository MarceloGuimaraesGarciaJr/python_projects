def jogar():
    print("*************")
    print("Jogo da Forca")
    print("*************")

    palavra_secreta = "casas".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    numero_letras = (len(palavra_secreta))
    erros = 0
    rodadas = 6
    enforcou = False
    acertou = False

    print(f"A palavra tem {numero_letras} letras.")
    while(not enforcou and not acertou):

        print(f"Você tem {rodadas} tentativas. Essa é sua {erros} tentativa.")
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
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Você ganhou")
    else:
        print(f"Você perderu, a palavra secreta era {palavra_secreta}")
if(__name__=="__main__"):
    jogar()
