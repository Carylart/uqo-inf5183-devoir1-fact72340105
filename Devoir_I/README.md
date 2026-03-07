# Devoir I - Algorithmes de Recherche dans un Labyrinthe

Ce projet met en œuvre et compare trois algorithmes de recherche fondamentaux en intelligence artificielle pour résoudre un labyrinthe.
Les algorithmes implémentés sont la recherche en profondeur (DFS), la recherche en largeur (BFS) et A*.

Le programme génère un labyrinthe aléatoire, applique chaque algorithme pour trouver un chemin de l'entrée à la sortie, puis affiche une comparaison de leurs performances.

## Fonctionnalités

*   **Génération de labyrinthe** : Crée un labyrinthe de taille `n x n` avec un chemin solution garanti entre le point de départ `S` et le point d'arrivée `G`.
*   **Algorithmes de recherche** :
    *   **DFS (Depth-First Search)** : Explore aussi loin que possible le long de chaque branche avant de revenir en arrière.
    *   **BFS (Breadth-First Search)** : Explore tous les voisins à la profondeur actuelle avant de passer au niveau suivant.
    *   **A* (A-Star)** : Un algorithme de recherche informé qui utilise une heuristique (distance de Manhattan) pour trouver le chemin le plus court.
*   **Visualisation** : Affiche dans la console le labyrinthe généré, les zones explorées par chaque algorithme et le chemin solution trouvé.
*   **Analyse comparative** : Génère un tableau récapitulatif comparant les algorithmes sur la base de :
    *   Le nombre de nœuds explorés.
    *   La longueur du chemin trouvé.
    *   Le temps d'exécution.

## Utilisation

Pour exécuter le programme, lancez le script `main.py`.

```bash
python main.py
```

Les résultats, y compris les visualisations du labyrinthe et le tableau comparatif, seront affichés dans la console et enregistrés dans le fichier `log.txt`.

Les paramètres du labyrinthe (taille `n` et graine aléatoire `seed`) peuvent être modifiés dans le fichier `main.py`.

## Structure du projet

*   `main.py`: Le point d'entrée du programme. Il orchestre la génération du labyrinthe, l'exécution des algorithmes et l'affichage des résultats.
*   `maze.py`: Contient les fonctions pour la génération du labyrinthe et la création des représentations textuelles (labyrinthe, exploration, solution).
*   `dfs.py`: Implémentation de l'algorithme de recherche en profondeur (DFS).
*   `bfs.py`: Implémentation de l'algorithme de recherche en largeur (BFS).
*   `astar.py`: Implémentation de l'algorithme de recherche A*.
*   `log.txt`: Fichier généré contenant la sortie complète de l'exécution du programme.

## Exemple de résultat

À la fin de l'exécution, un tableau comparatif est généré, similaire à celui-ci :

```
Algorithme        Noeuds    Longueur    Temps (ms)
------------------------------------------------------------
DFS               137       137         0.225
BFS               119       29          0.136
A* (manhattan)    36        29          0.063
