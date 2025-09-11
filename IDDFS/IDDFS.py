from copy import deepcopy

# Goal state for the 8-puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 is the blank tile

# Directions: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    """Find the position of the blank (0)"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    """Check if the current state is the goal state"""
    return state == goal_state

def get_neighbors(state):
    """Generate all possible moves from current state"""
    neighbors = []
    x, y = find_blank(state)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(state)
            # Swap blank with the adjacent tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def dls(state, depth, visited):
    """Depth-Limited Search"""
    if is_goal(state):
        return state

    if depth == 0:
        return None

    visited.add(str(state))  # Convert to string for hashable

    for neighbor in get_neighbors(state):
        if str(neighbor) not in visited:
            result = dls(neighbor, depth - 1, visited)
            if result is not None:
                return result

    return None

def iddfs(start_state, max_depth=50):
    """Iterative Deepening DFS"""
    for depth in range(max_depth):
        visited = set()
        result = dls(start_state, depth, visited)
        if result is not None:
            print(f"Solved at depth {depth}")
            return result
    return None

# Example starting state
start_state = [[1, 2, 3],
               [4, 5, 6],
               [8, 7, 0]]

# Run IDDFS
solution = iddfs(start_state)

if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found within the depth limit.")
