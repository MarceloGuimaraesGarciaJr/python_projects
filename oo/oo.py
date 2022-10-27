def adiciona_conta (numero,titular,saldo,limite):
    conta = {"nome": titular,"numero": numero, "saldo": saldo, "limite": limite}
    return conta

def deposita (conta, valor):
    conta["saldo"] += valor

def saca (conta, valor):
    conta["saldo"] -= valor

def extrato (conta):
    print("Seu saldo é {}".format(conta["saldo"]))