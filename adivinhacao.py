import random

def jogar():
    print("************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("************************")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Escolha seu nível de dificuldade: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    elif(nivel == 3):
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 a 100: "))
        print("Você digitou " , chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 a 100!")
            continue

        acertou     = numero_secreto == chute
        chute_maior = numero_secreto < chute
        chute_menor = numero_secreto > chute

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            print("Você errou")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(chute_maior):
                print("O seu chute foi MAIOR que o número secreto")
            elif(chute_menor):
                print("O seu chute foi MENOR que o número secreto")
        if(rodada == tentativas):
            print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()