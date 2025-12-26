from collections import deque

def read_input(filename = "input.txt"):
    with open(filename, "r") as f:
        line = f.readline().strip()
    M_left, C_left, M_right, C_right, boat, *model = line.split(",")
    return (int(M_left), int(C_left), int(M_right), int(C_right), boat.strip())

def conditions(state):
    M_left, C_left, M_right, C_right, boat = state
    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False
    if (M_left > 0 and M_left < C_left) or (M_right > 0 and M_right < C_right):
        return False
    return True

def get_successors(state):
    M_left, C_left, M_right, C_right, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []
    for m, c in moves:
        if boat == 'L':
            new_state = (M_left - m, C_left - c, M_right + m, C_right + c, 'R')
        else:
            new_state = (M_left + m, C_left + c, M_right - m, C_right - c, 'L')
        if conditions(new_state):
            successors.append(new_state)
    return successors

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    expansions = 0
    while stack:
        state, path = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        expansions += 1
        if state == goal:
            return path, expansions
        for succ in get_successors(state):
            if succ not in visited:
                stack.append((succ, path + [succ]))
    return None, expansions
    
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    expansions = 0
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        expansions += 1
        if state == goal:
            return path, expansions
        for succ in get_successors(state):
            if succ not in visited:
                queue.append((succ, path + [succ]))
    return None, expansions

if __name__ == "__main__":
    start = read_input("input.txt")
    goal = (0, 0, 3, 3, 'R')

    #dfs
    path, expansions = dfs(start, goal)
    print("The solution of Q1.1.a (DFS) is:")
    print("Solution Path:", path)
    print("Total cost =", (len(path) - 1))
    print("Number of node expansions =", expansions)

    #bfs
    path, expansions = bfs(start, goal)
    print("The solution of Q1.1.b (BFS) is:")
    print("Solution Path:", path)
    print("Total cost =", (len(path) - 1))
    print("Number of node expansions =", expansions)