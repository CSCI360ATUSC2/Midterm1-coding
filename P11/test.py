# DO NOT MODIFY THIS SCRIPT #
from p11 import a_star_search

if __name__ == "__main__":
    # Terrain types and their day and night costs
    terrain_costs = {
        'P': (1, 2),  # Plain: 1 during day, 2 during night
        'M': (5, 10), # Mountain: 5 during day, 10 during night
        'F': (3, 4),  # Forest: 3 during day, 4 during night
        'W': (float('inf'), float('inf')),  # Water: impassable
        'T': (0, 0)   # Teleportation point
    }

    # ===== Subproblem 1 ===== #
    grid = [
        ['S', 'P', 'M', 'P', 'W'],
        ['P', 'W', 'P', 'P', 'P'],
        ['P', 'M', 'F', 'W', 'P'],
        ['P', 'P', 'F', 'P', 'P'],
        ['M', 'P', 'F', 'P', 'G']
    ]
    K = 100

    shortest_path_cost, shortest_path = a_star_search(grid, K, terrain_costs)
    print(">>> Problem 11 Subproblem 1")
    print("\tPath cost:", shortest_path_cost)
    print("\tPath sequence:", shortest_path)
    # ===== END OF Subproblem 1 ===== #
    
    # ===== Subproblem 2 ===== #
    grid = [
        ['S', 'P', 'M', 'P', 'W'],
        ['P', 'W', 'P', 'P', 'P'],
        ['P', 'M', 'F', 'W', 'P'],
        ['P', 'P', 'F', 'P', 'P'],
        ['M', 'P', 'F', 'P', 'G']
    ]
    K = 3

    shortest_path_cost, shortest_path = a_star_search(grid, K, terrain_costs)
    print(">>> Problem 11 Subproblem 2")
    print("\tPath cost:", shortest_path_cost)
    print("\tPath sequence:", shortest_path)
    # ===== END OF Subproblem 2 ===== #

    # ===== Subproblem 3 ===== #
    grid = [
        ['S', 'P', 'P', 'T', 'P'],
        ['P', 'W', 'M', 'P', 'P'],
        ['P', 'M', 'F', 'W', 'P'],
        ['P', 'P', 'T', 'P', 'P'],
        ['M', 'P', 'F', 'P', 'G']
    ]
    K = 5

    shortest_path_cost, shortest_path = a_star_search(grid, K, terrain_costs)
    print(">>> Problem 11 Subproblem 3")
    print("\tPath cost:", shortest_path_cost)
    print("\tPath sequence:", shortest_path)
    # ===== END OF Subproblem 3 ===== #
