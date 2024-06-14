def solve_hanoi(n, source, destination, auxiliary, moves):
    if n == 1:
        moves.append((source, destination))
        print(f"Déplacer le disque 1 de {source} à {destination}")
    else:
        solve_hanoi(n - 1, source, auxiliary, destination, moves)
        moves.append((source, destination))
        print(f"Déplacer le disque {n} de {source} à {destination}")
        solve_hanoi(n - 1, auxiliary, destination, source, moves)

if __name__ == "__main__":
    import sys
    n = 3  # Par défaut, 3 disques
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Veuillez entrer un nombre entier pour le nombre de disques.")
            sys.exit(1)
    
    moves = []
    solve_hanoi(n, 'A', 'C', 'B', moves)
    print(f"Total des mouvements: {len(moves)}")