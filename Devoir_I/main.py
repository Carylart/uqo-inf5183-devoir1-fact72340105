from maze import generate_maze, print_maze

def main():
    """
    Point d'entrée du programme.
    """

    n = 16      # Taille du labyrinthe
    seed = 42   # Seed pour reproductibilité

    maze = generate_maze(n, seed)

    print_maze(maze)


if __name__ == "__main__":
    main()