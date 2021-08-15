def copy_arr(grid):
    copy = [[0 for k in range(len(grid[0]))] for j in range(len(grid))]
    for k in range(len(grid)):
        for j in range(len(grid[0])):
            copy[k][j] = grid[k][j]
    return copy

def get_number_of_nodes_from_grid(grid):
    grid_nodes = 0
    copy = copy_arr(grid)
    print(id(copy))
    print(id(grid))

    print(copy)
    for k in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            node_sum = 0
            if grid[k][j] == 1:
                node_sum = grid[k + 1][j] + grid[k - 1][j] - grid[k][j + 1] - grid[k][j - 1]
                if node_sum != -2 and node_sum != 2:
                    grid_nodes += 1
                    copy[k][j] = 2


    return grid_nodes,copy



class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.dTable = [[0 for i in range(nodes)] for j in range(nodes)]
