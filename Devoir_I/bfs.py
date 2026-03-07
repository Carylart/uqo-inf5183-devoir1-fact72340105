import time
from collections import deque
from maze import WALL

def bfs_maze(maze):
    """
    Explore un labyrinthe en utilisant l'algorithme BFS (Breadth-First Search).

    Principe :
    - Utilise une file (FIFO : First In First Out)
    - Explore les voisins dans l'ordre :
      droite → bas → gauche → haut
    - Évite les murs (#)
    - Ne revisite pas les cases déjà explorées

    Paramètre :
    maze : matrice 2D représentant le labyrinthe

    Retourne :
    visited : ensemble des cases explorées
    path : liste des coordonnées du chemin trouvé
    explored_nodes : nombre total de noeuds explorés
    execution_time : temps d'exécution de l'algorithme
    """

    # Dimensions du labyrinthe
    rows = len(maze)
    cols = len(maze[0])

    # Position du départ et de l'arrivée
    start = (1, 1)
    goal = (rows-2, cols-2)

    # Ordre d'exploration des voisins
    directions = [
        (0, 1),   # droite
        (1, 0),   # bas
        (0, -1),  # gauche
        (-1, 0)   # haut
    ]

    # Initialisation de la file BFS
    queue = deque([start])

    # Ensemble des cases visitées
    visited = set([start])

    # Dictionnaire pour reconstruire le chemin
    parent = {}

    # Compteur de noeuds explorés
    explored_nodes = 0

    # Début du chronométrage
    start_time = time.perf_counter()

    # Boucle principale BFS
    while queue:

        # Retire la première case de la file (FIFO)
        x, y = queue.popleft()

        explored_nodes += 1

        # Si on atteint le but
        if (x, y) == goal:
            break

        # Exploration des voisins
        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            # Vérifie que la case est valide
            if (
                0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] != WALL and
                (nx, ny) not in visited
            ):

                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    end_time = time.perf_counter()

    # Reconstruction du chemin
    path = []

    if goal in parent or goal == start:

        node = goal

        while node != start:
            path.append(node)
            node = parent[node]

        path.append(start)
        path.reverse()

    execution_time = end_time - start_time

    # Sauvegarde des résultats comme attributs de la fonction
    bfs_maze.visited = visited
    bfs_maze.path = path
    bfs_maze.explored_nodes = explored_nodes
    bfs_maze.execution_time = execution_time

    return visited, path, explored_nodes, execution_time