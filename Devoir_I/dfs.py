import time

def dfs_maze(maze):
    """
    Explore un labyrinthe en utilisant l'algorithme DFS (Depth-First Search).

    Principe :
    - Utilise une pile (LIFO : Last In First Out)
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

    # Variables pour stocker la position du départ et de l'arrivée
    start = (1, 1)
    goal = (rows-2, cols-2)

    # Ordre d'exploration des voisins
    # droite → bas → gauche → haut
    directions = [
        (0, 1),   # droite
        (1, 0),   # bas
        (0, -1),  # gauche
        (-1, 0)   # haut
    ]

    # Initialisation de la pile DFS avec la position de départ
    stack = [start]

    # Ensemble des cases déjà visitées
    visited = set([start])

    # Dictionnaire permettant de reconstruire le chemin, parent[case] = case précédente
    parent = {}

    # Compteur du nombre de noeuds explorés
    explored_nodes = 0

    # Début du chronométrage
    start_time = time.perf_counter()

    # Boucle principale de l'algorithme DFS
    while stack:

        # Retire la dernière case ajoutée dans la pile (LIFO)
        x, y = stack.pop()

        # Incrémente le compteur de noeuds explorés
        explored_nodes += 1

        # Si on atteint le but, on arrête la recherche
        if (x, y) == goal:
            break

        # Exploration des voisins dans l'ordre défini
        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            # Vérifie que la case est dans les limites du labyrinthe, n'est pas un mur et qu'elle n'a pas encore été visitée
            if (
                0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] != '#' and
                (nx, ny) not in visited
            ):

                # Ajoute la case dans la pile pour exploration future
                stack.append((nx, ny))

                # Marque la case comme visitée
                visited.add((nx, ny))

                # Enregistre le parent pour reconstruire le chemin
                parent[(nx, ny)] = (x, y)

    # Fin du chronométrage
    end_time = time.perf_counter()

    # Reconstruction du chemin depuis le goal jusqu'au start
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    # Ajoute le point de départ
    path.append(start)

    # Inverse la liste pour obtenir le chemin dans le bon ordre
    path.reverse()

    # Calcul du temps d'exécution
    execution_time = end_time - start_time

    # Sauvegarde des résultats comme attributs de la fonction
    dfs_maze.visited = visited
    dfs_maze.path = path
    dfs_maze.explored_nodes = explored_nodes
    dfs_maze.execution_time = execution_time

    return visited, path, explored_nodes, execution_time