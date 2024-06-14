# Créer un jeu de cartes
def créer_jeu():
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
    return [valeur + ' de ' + couleur for couleur in couleurs for valeur in valeurs]