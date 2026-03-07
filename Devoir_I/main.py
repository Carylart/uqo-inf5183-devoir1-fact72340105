from maze import generate_maze, show_maze, show_exploration, show_solution, show_path
from dfs import dfs_maze
from bfs import bfs_maze
from astar import astar_maze

def log(*args):
    """
    Affiche dans la console et écrit dans un fichier texte.
    """
    text = " ".join(str(a) for a in args)

    print(text)

    with open("log.txt", "a") as file:
        file.write(text + "\n")

def log_stats(explored_nodes, path, exec_time):
    """
    Affiche les statistiques de l'exploration.

    Statistiques affichées :
    - nombre de noeuds explorés
    - longueur du chemin trouvé
    - temps d'exécution
    """

    log("\nStatistiques :")
    log("Nombre de noeuds explorés :", explored_nodes)
    log("Longueur du chemin trouvé :", len(path))
    log("Temps d'exécution :", f"{exec_time:.6f} secondes")
    log(show_path(path))
    log()

def comparison_table(dfs_nodes, dfs_path, dfs_time,
                     bfs_nodes, bfs_path, bfs_time,
                     astar_nodes, astar_path, astar_time):
    """
    Génère un tableau comparatif entre DFS, BFS et A*.
    """

    result = ""

    result += "Algorithme        Noeuds    Longueur    Temps (ms)\n"
    result += "-" * 60 + "\n"

    result += f"DFS               {dfs_nodes:<9} {len(dfs_path):<10} {dfs_time*1000:.3f}\n"
    result += f"BFS               {bfs_nodes:<9} {len(bfs_path):<10} {bfs_time*1000:.3f}\n"
    result += f"A* (manhattan)    {astar_nodes:<9} {len(astar_path):<10} {astar_time*1000:.3f}\n"

    return result

def main():
    """
    Point d'entrée du programme.
    """

    n = 16      # Taille du labyrinthe
    seed = 42   # Seed pour reproductibilité

    # Génération du labyrinthe
    maze = generate_maze(n, seed)
    log(show_maze(maze))

    # DFS
    dfs_maze(maze)

    log("\nExploration DFS :")
    log(show_exploration(maze, dfs_maze.visited))

    log("\nSolution DFS :")
    log(show_solution(maze, dfs_maze.path))

    log_stats(
        dfs_maze.explored_nodes,
        dfs_maze.path,
        dfs_maze.execution_time
    )

    # BFS
    bfs_maze(maze)

    log("\nExploration BFS :")
    log(show_exploration(maze, bfs_maze.visited))

    log("\nSolution BFS :")
    log(show_solution(maze, bfs_maze.path))

    log_stats(
        bfs_maze.explored_nodes,
        bfs_maze.path,
        bfs_maze.execution_time
    )

    # A*
    astar_maze(maze)

    log("\nExploration A* :")
    log(show_exploration(maze, astar_maze.visited))

    log("\nSolution A* :")
    log(show_solution(maze, astar_maze.path))

    log_stats(
        astar_maze.explored_nodes,
        astar_maze.path,
        astar_maze.execution_time
    )

    # Tableau comparatif
    log(
        comparison_table(
            dfs_maze.explored_nodes, dfs_maze.path, dfs_maze.execution_time,
            bfs_maze.explored_nodes, bfs_maze.path, bfs_maze.execution_time,
            astar_maze.explored_nodes, astar_maze.path, astar_maze.execution_time
        )
    )

if __name__ == "__main__":
    main()