# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Choisir l'opération.")
print("1.Addition")
print("2.Soustraction")
print("3.Multiplication")
print("4.Division")

while True:
    # take input from the user
    choice = input("Choisissez l'opération (1/2/3/4) : ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le second nombre : "))
        except ValueError:
            print("Entrée invalide, merci d'entrer un nombre.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            if num2 == 0:
                print("Erreur ! La division par zéro n'est pas autorisée !")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is anything but yes
        next_calculation = input("Encore un calcul ? (oui/non): ")
        if next_calculation != "oui":
          break
    else:
        print("Entrée non valide")