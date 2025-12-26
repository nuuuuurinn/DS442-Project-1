import heapq

def read_input(filename = "input.txt"):
    with open(filename, "r") as f:
        M_left, C_left, M_right, C_right, boat, model = f.readline().strip().split(",")
    state = (int(M_left), int(C_left), int(M_right), int(C_right), boat.strip())
    cost_model = model.strip()
    return state, cost_model

def conditions(state):
    M_left, C_left, M_right, C_right, boat = state
    if (M_left < 0 or M_left > 3) or (C_left < 0 or C_left > 3) or (M_right < 0 or M_right > 3) or (C_right < 0 or C_right > 3): 
        return False
    if (M_left > 0 and C_left > M_left) or (M_right > 0 and C_right > M_right):
        return False
    return True

def calculate_cost(action, model):
    m, c, direction = action
    if model == 'A':
        return 2 * m + 1 * c
    elif model == 'B':
        return 2 if direction == 'L->R' else 1

def get_successors(state):
    M_left, C_left, M_right, C_right, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    successors = []
    for m, c in moves:
        if boat == 'L':
            new_state = (M_left - m, C_left - c, M_right + m, C_right + c, 'R')
            direction = "L->R"
        else:
            new_state = (M_left + m, C_left + c, M_right - m, C_right - c, 'L')
            direction = "R->L"
        if conditions(new_state):
            successors.append((new_state, (m, c, direction)))
    return successors

def ucs(initial_state, model):
    goal = (0, 0, 3, 3, 'R')
    fringe = []
    heapq.heappush(fringe, (0, initial_state, [initial_state]))
    visited = set()
    expansions = 0
    while fringe:
        cost, state, path = heapq.heappop(fringe)
        if state[:4] == goal[:4]:
            return path, cost, expansions
        if state in visited:
            continue
        visited.add(state)
        expansions += 1
        for succ, action in get_successors(state):
            if succ not in visited:
                new_cost = cost + calculate_cost(action, model)
                heapq.heappush(fringe, (new_cost, succ, path + [succ]))
    return [], 0, expansions

if __name__ == "__main__":
    state, model = read_input()
    for model in ["A", "B"]:
        path, total_cost, expansions = ucs(state, model)
        print(f"The solution of UCS (Cost Model {model}) is:")
        print("Solution Path:", path)
        print(f"Total cost = {total_cost}")
        print(f"Number of node expansions = {expansions}\n")
