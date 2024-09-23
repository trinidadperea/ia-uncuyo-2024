import random
import matplotlib.pyplot as plt

def heuristic(state):
    h = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j]:
                h += 1
            offset = j - i
            if state[i] == state[j] - offset or state[i] == state[j] + offset:
                h += 1
    return h

def initial_state(size):
    board = []
    for i in range(size):
        num = random.randint(0, size - 1)
        board.append(num)
    return board

def best_neighbor(state):
    best_neighbor = state
    best_heuristic = heuristic(state)
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j:
                new_state = list(state)
                new_state[i] = j
                h = heuristic(new_state)
                if h < best_heuristic:
                    best_neighbor = new_state
                    best_heuristic = h
    return best_neighbor

def neighbors(state):
    neighbors_list = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j:
                new_state = list(state)
                new_state[i] = j  
                neighbors_list.append(new_state)
    return neighbors_list

def random_neighbor(state):
    i = random.randint(0, len(state) - 1)
    j = random.randint(0, len(state) - 1)
    new_state = list(state)
    new_state[i] = j
    return new_state

def random_state(size):
    state = []
    for i in range(size):
        num = random.randint(0, size - 1)
        state.append(num)
    return state

def plot_board(state):
    n = len(state)
    board = [[(i + j) % 2 for i in range(n)] for j in range(n)]

    for i in range(n):
        board[state[i]][i] = 2  

    plt.imshow(board, cmap="binary")  
    ax = plt.gca()  

    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                rect = plt.Rectangle((j-0.5, i-0.5), 1, 1, fill=True, color='red')
                ax.add_patch(rect)

    plt.xticks([])
    plt.yticks([])
    plt.show()

