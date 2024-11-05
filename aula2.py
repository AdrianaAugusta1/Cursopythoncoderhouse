saldo = 950.60
saque = float(input("Quanto voce quer sacar?"))
saldo = saldo - saque
print(f"Seu novo saldo é {saldo}")


fruta = ["maça", "banana", "pera", "abacaxi", "laranja"]
nova_fruta = input("Digite o nome de uma fruta?")
if nova_fruta in fruta:
    print(f"Essa fruta '{nova_fruta}' já faz parte da lista!")
else:
    fruta.append(nova_fruta)
    print(f"A fruta '{nova_fruta}' foi adicionada a lista!")


    palavra = input("Digite uma palavra!")
vogais = ["a", "e", "i", "o", "u"]
nova_palavra = ""
for letra in palavra:
  if letra in vogais:
    nova_palavra += "*"
  else:
    nova_palavra += letra
print(nova_palavra)