def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    while True:
        user_input = input("Veuillez entrer une liste de nombres séparés par des virgules (ou 'q' pour quitter) : ")
        if user_input.lower() == 'q':
            print("Au revoir!")
            break
        try:
            number_list = [int(x.strip()) for x in user_input.split(',')]
            print("Liste originale:", number_list)
            sorted_list = insertion_sort(number_list)
            print("Liste triée:", sorted_list)
        except ValueError:
            print("Erreur : Veuillez entrer uniquement des nombres séparés par des virgules.")
        except Exception as e:
            print(f"Erreur inattendue : {e}")