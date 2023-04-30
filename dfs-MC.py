# function to check if the state is valid or not
def is_valid_state(state):
    m, c, b = state
    # check if there are more cannibals than missionaries on either bank
    if c > m and m > 0:
        return False
    # check if there are negative number of cannibals or missionaries
    if m < 0 or c < 0:
        return False
    # check if the boat is carrying more than two people
    if b != 0 and b != 1:
        return False
    return True

# function to generate child states
def generate_child_states(state):
    m, c, b = state
    children = []
    if b == 1:
        for i in range(3):
            for j in range(3):
                new_state = (m - i, c - j, 0)
                if is_valid_state(new_state):
                    children.append(new_state)
    else:
        for i in range(3):
            for j in range(3):
                new_state = (m + i, c + j, 1)
                if is_valid_state(new_state):
                    children.append(new_state)
    return children

# depth first search function
def dfs(initial_state, goal_state):
    visited_states = []
    stack = [[initial_state]]
    while stack:
        path = stack.pop()
        current_state = path[-1]
        if current_state == goal_state:
            return path
        visited_states.append(current_state)
        for child in generate_child_states(current_state):
            if child not in visited_states:
                new_path = list(path)
                new_path.append(child)
                stack.append(new_path)
    return None

# function to print the output in a visual manner
def print_output(path):
    for state in path:
        m, c, b = state
        left_bank = f'M: {m} C: {c}'
        right_bank = f'M: {3 - m} C: {3 - c}'
        if b == 1:
            print(f'{left_bank: <10} B -----> {right_bank}')
        else:
            print(f'{left_bank} <----- B {right_bank: >10}')

# define the initial and goal states
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

# call the dfs function and print the output
path = dfs(initial_state, goal_state)
print_output(path)
