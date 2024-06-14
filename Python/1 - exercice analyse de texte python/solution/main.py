import re

def analyze_text(text):
    # Compter le nombre de caractères (y compris les espaces et la ponctuation)
    num_characters = len(text)

    # Compter le nombre de mots (en utilisant les espaces comme séparateurs)
    words = text.split()
    num_words = len(words)

    # Compter le nombre de phrases (en supposant que les phrases se terminent par '.', '!', ou '?')
    sentences = re.split(r'[.!?]', text)
    # Supprimer les chaînes vides résultantes de la séparation
    sentences = [s for s in sentences if s.strip()]
    num_sentences = len(sentences)

    return num_characters, num_words, num_sentences

def main():
    # Demander à l'utilisateur d'entrer un texte
    text = input("Entrez un texte : ")

    # Analyser le texte
    num_characters, num_words, num_sentences = analyze_text(text)

    # Afficher les résultats
    print(f"Nombre de caractères : {num_characters}")
    print(f"Nombre de mots : {num_words}")
    print(f"Nombre de phrases : {num_sentences}")

if __name__ == "__main__":
    main()