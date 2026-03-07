import random

# Constantes représentant les différents types de cases
WALL = '#'
PATH = '.'
START = 'S'
GOAL = 'G'


def print_maze(maze):
    """
    Affiche le labyrinthe dans la console.
    """

    for row in maze:
        print(" ".join(row))

def generate_random_path(n, rng):
    """
    Génère un chemin aléatoire entre S et G
    en se déplaçant seulement vers le bas ou la droite.
    """

    start = (1, 1)
    goal = (n-2, n-2)

    x, y = start

    path = [(x, y)]

    directions = [
        (1, 0),  # bas
        (0, 1),  # droite
    ]

    while (x, y) != goal:

        shuffled = directions[:]
        rng.shuffle(shuffled)

        for dx, dy in shuffled:
            nx = x + dx
            ny = y + dy

            if 1 <= nx < n-1 and 1 <= ny < n-1:
                x, y = nx, ny
                path.append((x, y))
                break

    return set(path)

def creates_closed_cell(maze, x, y):
    """
    Limite la création de poches locales.
    Vérifie les cases adjacentes et bloque celles qui auraient 3 murs ou plus.

    Principe :
    On regarde les 4 cases adjacentes (haut, bas, gauche, droite).
    Si l'une de ces cases est un chemin (PATH), on compte combien de murs l'entourent.

    Si cette case se retrouve avec 3 murs ou plus autour d'elle,
    cela signifie qu'elle serait quasiment enfermée → on bloque la création du mur.
    """

    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx = x + dx
        ny = y + dy

        if maze[nx][ny] == PATH:

            walls = 0

            if maze[nx-1][ny] == WALL: walls += 1
            if maze[nx+1][ny] == WALL: walls += 1
            if maze[nx][ny-1] == WALL: walls += 1
            if maze[nx][ny+1] == WALL: walls += 1

            # bloque si presque fermé
            if walls >= 3:
                return True

    return False

def generate_maze(n, seed, wall_prob=0.5):
    """
    Génère un labyrinthe de taille n x n.

    Étapes :
    1. Initialise le générateur aléatoire avec la seed
    2. Créer une grille remplie de chemins
    3. Ajouter les murs sur les bordures
    4. Générer un chemin aléatoire entre S et G
    5. Placer des murs aléatoirement en évitant les cases du chemin
    """

    # Générateur aléatoire
    rng = random.Random(seed)

    # Création de la grille remplie de chemins
    maze = [[PATH for _ in range(n)] for _ in range(n)]

    # Création des murs sur les bordures du labyrinthe
    for i in range(n):
        maze[0][i] = WALL
        maze[n-1][i] = WALL
        maze[i][0] = WALL
        maze[i][n-1] = WALL

    start = (1, 1)
    goal = (n-2, n-2)

    # Générer un chemin aléatoire
    path_cells = generate_random_path(n, rng)

    # Placement aléatoire des murs
    for i in range(1, n-1):
        for j in range(1, n-1):

            # Si la case fait partie du chemin, on ne met pas de mur
            if (i, j) in path_cells:
                continue

            # Sinon on place un mur avec une certaine probabilité
            if rng.random() < wall_prob:
                maze[i][j] = WALL
                # Cosmétique pour éviter les poches fermées
                if creates_closed_cell(maze, i, j):
                    maze[i][j] = PATH

    # Placement des positions de départ et d'arrivée
    maze[start[0]][start[1]] = START
    maze[goal[0]][goal[1]] = GOAL

    return maze

def show_exploration(maze, visited):
    """
    Affiche le labyrinthe en montrant toutes les cases explorées.

    Les cases explorées sont marquées avec 'p'.
    Les murs et les cases spéciales restent inchangés.

    Paramètres :
    maze : labyrinthe original
    visited : ensemble des cases visitées par DFS
    """

    # Création d'une copie du labyrinthe pour l'affichage
    display = [row[:] for row in maze]

    # Marquer les cases explorées
    for x, y in visited:
        if display[x][y] == '.':
            display[x][y] = 'p'

    # Afficher le labyrinthe ligne par ligne
    for row in display:
        print(" ".join(row))

def show_solution(maze, path):
    """
    Affiche le labyrinthe avec le chemin solution trouvé.

    Les cases du chemin sont marquées avec '*'.

    Paramètres :
    maze : labyrinthe original
    path : liste des coordonnées du chemin solution
    """

    # Création d'une copie du labyrinthe
    display = [row[:] for row in maze]

    # Marquer les cases du chemin
    for x, y in path:
        if display[x][y] == '.':
            display[x][y] = '*'

    # Afficher le labyrinthe
    for row in display:
        print(" ".join(row))

def print_path(path):
    """
    Affiche le chemin solution sous forme de coordonnées.

    Exemple :
    Chemin : S (1,1) -> (2,1) -> (3,1) -> ... -> G (14,14)
    """

    result = "Chemin : "

    for i, (x, y) in enumerate(path):

        if i == 0:
            result += f"S ({x}, {y}) -> "

        elif i == len(path) - 1:
            result += f"G ({x}, {y})"

        else:
            result += f"({x}, {y}) -> "

    print(result)