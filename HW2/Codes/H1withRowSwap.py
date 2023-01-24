from NQueens import *

class StateCollisionsWithRowSwap(State):

    def random(n):
        # Making a random state with board size n
        from random import shuffle
        begin_state = [i for i in range(n)]
        shuffle(begin_state)
        return StateCollisionsWithRowSwap(n, begin_state)

    def __check_collisions(self, a, b):
        if a == b:
            return False
        if (a[0]-b[0] == 0) or (a[1]-b[1] == 0) or (abs(a[0]-b[0]) == abs(a[1]-b[1])):
            return True
        return False

    def h(self):
        # Heuristic function
        h_cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                h_cnt += int(self.__check_collisions((i, self[i]), (j, self[j])))
        return h_cnt

    
    def g(self):
        # g Function for A* Algorithm
        g_cnt = 0
        for i in range(n):
            g_cnt += abs(self[i] - self.__begin_state[i])
        return g_cnt
    
    def next_states(self):
        # Return next states from all possible actions
        states = []
        for i in range(self.n-1):
            state = self.deepcopy()
            state[i], state[i+1] = state[i+1], state[i]
            states.append(state)
        return states

if __name__ == '__main__':

    # n = int(input('Please input n: '))
    n = 6

    search = GreedySearch(n, StateCollisionsWithRowSwap.random(n), verbose=False)

    # search = AStarSearch(n, StateCollisions.random(n), verbose=False)

    while not search.step():
        pass
