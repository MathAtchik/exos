import random

# Créer un jeu de cartes
def créer_jeu():
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
    return [valeur + ' de ' + couleur for couleur in couleurs for valeur in valeurs]

# Mélanger le jeu de cartes
def mélanger_jeu(jeu):
    random.shuffle(jeu)
    return jeu

# Distribuer les cartes à un nombre donné de joueurs et de cartes
def distribuer_cartes(jeu, nombre_de_joueurs, nombre_de_cartes):
    mains = [[] for _ in range(nombre_de_joueurs)]
    for i in range(nombre_de_joueurs * nombre_de_cartes):
        mains[i % nombre_de_joueurs].append(jeu[i])
    return mains

# Fonction principale
def main():
    jeu = créer_jeu()
    jeu_mélangé = mélanger_jeu(jeu)
    
    # Demander à l'utilisateur de saisir le nombre de joueurs
    nombre_de_joueurs = int(input("Entrez le nombre de joueurs : "))
    
    # Demander à l'utilisateur de saisir le nombre de cartes à distribuer
    nombre_de_cartes = int(input("Entrez le nombre de cartes à distribuer à chaque joueur : "))
    
    # Vérifier si le nombre de cartes demandé est possible
    if nombre_de_joueurs * nombre_de_cartes > len(jeu_mélangé):
        print("Il n'y a pas assez de cartes pour distribuer ce nombre à chaque joueur.")
        return
    
    mains = distribuer_cartes(jeu_mélangé, nombre_de_joueurs, nombre_de_cartes)
    for i, main in enumerate(mains):
        print(f"Main du joueur {i + 1}: {main}")

# Exécution de la fonction principale
if __name__ == "__main__":
    main()