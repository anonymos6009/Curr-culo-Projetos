idade = int(input("Digite sua idade: "))
carteira = input("Você possui carteira de motorista? (s/n): ")
if idade >= 18 and carteira == "s":
    print("Você pode dirigir! 🚗💨")
elif idade >= 18 and carteira == "n":
    print("Você tem idade, mas precisa tirar a carteira! 📝")
else:
    print("Você ainda não pode dirigir! 🛑")