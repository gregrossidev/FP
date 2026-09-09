import random

print("Joguin")
print("Adivinhe o número que estou penando entre 1 e 100")
print("Você tem 8 tentativas")

numero_secreto = random.randint(1,100)
contador = 7
acertou = False

while contador > 0:
    print("Você ainda tem", contador, "tentativas")
    tentativa = int(input("digite seu palpite: "))
    contador -=1

    if tentativa == numero_secreto:
        print("Parabéns, ta certo")
        acertou = True
        break
    elif tentativa < numero_secreto:
        print("o número secreto é MAIOR que seu palpite")
    else:
        print("o número secreto é MENOR que seu palpite")

if not acertou:
    print("Errrooou, o número certo é:", numero_secreto)
else:
    print ("Parabéns, ta certo")
