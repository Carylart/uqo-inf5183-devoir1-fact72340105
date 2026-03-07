from maze import generate_maze, print_maze, show_exploration, show_solution, print_path
from dfs import dfs_maze
from bfs import bfs_maze
from astar import astar_maze

def print_stats(explored_nodes, path, exec_time):
    """
    Affiche les statistiques de l'exploration.

    Statistiques affichées :
    - nombre de noeuds explorés
    - longueur du chemin trouvé
    - temps d'exécution
    """

    print("\nStatistiques :")
    print("Nombre de noeuds explorés :", explored_nodes)
    print("Longueur du chemin trouvé :", len(path))
    print("Temps d'exécution :", f"{exec_time:.6f} secondes")
    print()
    print_path(path)

def main():
    """
    Point d'entrée du programme.
    """

    n = 16      # Taille du labyrinthe
    seed = 42   # Seed pour reproductibilité

    # Génération du labyrinthe
    maze = generate_maze(n, seed)
    print_maze(maze)

    # DFS
    dfs_maze(maze)

    print("\nExploration DFS :")
    show_exploration(maze, dfs_maze.visited)

    print("\nSolution DFS :")
    show_solution(maze, dfs_maze.path)

    print_stats(
        dfs_maze.explored_nodes,
        dfs_maze.path,
        dfs_maze.execution_time
    )

    # BFS
    bfs_maze(maze)

    print("\nExploration BFS :")
    show_exploration(maze, bfs_maze.visited)

    print("\nSolution BFS :")
    show_solution(maze, bfs_maze.path)

    print_stats(
        bfs_maze.explored_nodes,
        bfs_maze.path,
        bfs_maze.execution_time
    )

    # A*
    astar_maze(maze)

    print("\nExploration A* :")
    show_exploration(maze, astar_maze.visited)

    print("\nSolution A* :")
    show_solution(maze, astar_maze.path)

    print_stats(
        astar_maze.explored_nodes,
        astar_maze.path,
        astar_maze.execution_time
    )

if __name__ == "__main__":
    main()