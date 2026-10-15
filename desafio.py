import random

print("Vamos jogar um jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 1000.")
print("Você tem 15 tentativas para adivinhar o número.\n")

numero_secreto = random.randint(1, 1000)
tentativas_maximas = 15

input("Pressione Enter para começar o jogo...")

for tentativa_atual in range(1, tentativas_maximas + 1):
    print(f"\nTentativa {tentativa_atual} de {tentativas_maximas}")
    
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print(f"\n🎉 Parabéns! Você acertou o número secreto: {numero_secreto}")
        print(f"Você acertou em {tentativa_atual} tentativas!")
        break  # Sai do loop porque o usuário ganhou
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR que isso!")
    else:
        print("O número secreto é MENOR que isso!")

    if tentativa_atual == tentativas_maximas:
        print(f"\nGAME OVER! Suas tentativas acabaram. O número era {numero_secreto}.")