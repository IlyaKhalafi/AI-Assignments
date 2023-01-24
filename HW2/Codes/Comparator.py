from NQueens import *
from H1 import *
from H2 import *
from H3 import *
from time import time
from matplotlib import pyplot as plt

def random(n):
    # Making a random state with board size n
    from random import shuffle
    begin_state = [i for i in range(n)]
    shuffle(begin_state)
    return begin_state

def test(n, times):
    iterations = [[0 for i in range(2)] for j in range(3)]
    elapsed_time = [[0 for i in range(2)] for j in range(3)]
    
    begin_states = []
    for i in range(5):
        begin_states.append(random(n))
        
    for j, search_method in enumerate(Searches):
        for i, state_class in enumerate(States):
            for begin_state in begin_states:
                search = search_method(state_class(begin_state))
                a = time()
                while not search.step():
                    pass
                elapsed_time[i][j] += time() - a
                iterations[i][j] += search.iterations
                
    return iterations, elapsed_time


States = [StateCollisions, StateThreatenedQueens, StateDiagonalCollisions]
Searches = [GreedySearch, AStarSearch]

if __name__ == '__main__':
    
    values = [i for i in range(8, 17)] # range of values for n
    
    all_iterations = [[[] for i in range(2)] for j in range(3)]
    all_times = [[[] for i in range(2)] for j in range(3)]
    test_times = 10
    
    for value in values:
        iterations, elapsed_time = test(value, test_times)
        for i in range(3):
            for j in range(2):
                all_iterations[i][j].append(iterations[i][j])
                all_times[i][j].append(elapsed_time[i][j])
    
    titles = ['A* Search', 'Greedy Search']
    legends = [f'H{i}' for i in range(1, 4)]
    x_label = 'n'
    y_labels = ['iterations', 'computation time']
    plt.style.use('fivethirtyeight')
    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    
    measures = [all_iterations, all_times]
    
    for k, measure in enumerate(measures):
        for j in range(2):
            # plt.subplot(1, j+1, 1)
            axes[k][j].set_title(titles[j])
            axes[k][j].set_xlabel(x_label)
            axes[k][j].set_ylabel(y_labels[k])
            axes[k][j].grid(True)
            for i in range(3):
                # change all_iterations to all_times for plotting computation times
                axes[k][j].plot(values, measure[i][j])
            axes[k][j].legend(labels=legends, loc='upper left')
    
    fig.tight_layout()
    plt.show()
    
