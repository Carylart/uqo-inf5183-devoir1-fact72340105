import time
import heapq
from maze import WALL


def manhattan(a, b):
    """
    Calcule la distance de Manhattan entre deux points.

    Cette heuristique estime la distance restante jusqu'au but
    """

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar_maze(maze):
    """
    Recherche du chemin dans un labyrinthe avec l'algorithme A*.

    Principe de A* :
    ----------------
    A* choisit toujours le noeud ayant la plus petite valeur :

        f(n) = g(n) + h(n)

    où :

        g(n) = coût réel du chemin depuis le départ jusqu'à n
        h(n) = estimation heuristique du coût restant jusqu'au but

    L'algorithme utilise une file de priorité pour toujours explorer
    la case la plus prometteuse.

    Paramètre :
    -----------
    maze : matrice 2D représentant le labyrinthe

    Retourne :
    ----------
    visited : ensemble des cases explorées
    path : liste représentant le chemin trouvé
    explored_nodes : nombre total de noeuds explorés
    execution_time : temps d'exécution de l'algorithme
    """

    # Dimensions du labyrinthe
    rows = len(maze)
    cols = len(maze[0])

    # Position de départ et objectif
    start = (1, 1)
    goal = (rows-2, cols-2)

    # Directions possibles de déplacement
    # droite → bas → gauche → haut
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    # File de priorité (min-heap)
    # chaque élément est (f_score, position)
    open_set = []

    # On commence avec le noeud de départ
    heapq.heappush(open_set, (0, start))

    # Ensemble des cases déjà explorées
    visited = set()

    # Dictionnaire pour reconstruire le chemin final
    parent = {}

    # Dictionnaire contenant le coût réel g(n)
    # coût depuis le départ jusqu'à chaque case
    g_score = {start: 0}

    # Compteur du nombre de noeuds explorés
    explored_nodes = 0

    # Début du chronométrage
    start_time = time.perf_counter()

    # Boucle principale de l'algorithme A*
    while open_set:

        # On récupère la case ayant le plus petit f(n)
        f, (x, y) = heapq.heappop(open_set)

        # Si la case a déjà été explorée, on l'ignore
        if (x, y) in visited:
            continue

        # On marque la case comme visitée
        visited.add((x, y))

        # Incrément du nombre de noeuds explorés
        explored_nodes += 1

        # Si on atteint le but, la recherche est terminée
        if (x, y) == goal:
            break

        # Exploration des voisins
        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            neighbor = (nx, ny)

            # Vérifie que la case est dans les limites
            # et qu'elle n'est pas un mur
            if (
                0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] != WALL
            ):

                # Calcul du coût réel pour atteindre ce voisin
                tentative_g = g_score[(x, y)] + 1

                # Si ce voisin n'a jamais été visité
                # ou si on a trouvé un chemin plus court
                if neighbor not in g_score or tentative_g < g_score[neighbor]:

                    # Mise à jour du coût réel
                    g_score[neighbor] = tentative_g

                    # Calcul de l'estimation heuristique
                    h = manhattan(neighbor, goal)

                    # Calcul de la fonction d'évaluation
                    f_score = tentative_g + h

                    # Ajout du voisin dans la file de priorité
                    heapq.heappush(open_set, (f_score, neighbor))

                    # Enregistrement du parent pour reconstruire le chemin
                    parent[neighbor] = (x, y)

    # Fin du chronométrage
    end_time = time.perf_counter()

    # Reconstruction du chemin trouvé
    path = []

    if goal in parent or goal == start:

        node = goal

        # Remonter du but jusqu'au départ
        while node != start:
            path.append(node)
            node = parent[node]

        # Ajouter le point de départ
        path.append(start)

        # Inverser pour obtenir le chemin dans le bon ordre
        path.reverse()

    # Calcul du temps d'exécution
    execution_time = end_time - start_time

    # Stockage des résultats dans la fonction
    astar_maze.visited = visited
    astar_maze.path = path
    astar_maze.explored_nodes = explored_nodes
    astar_maze.execution_time = execution_time

    # Retour des résultats
    return visited, path, explored_nodes, execution_time