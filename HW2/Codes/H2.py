from NQueens import *

class StateThreatenedQueens(State):

    def random(n):
        # Making a random state with board size n
        from random import randint
        begin_state = [randint(0, n-1) for i in range(n)]
        return StateThreatenedQueens(begin_state)

    def __check_collisions(self, a, b):
        if a == b:
            return False
        if (a[0]-b[0] == 0) or (a[1]-b[1] == 0) or (abs(a[0]-b[0]) == abs(a[1]-b[1])):
            return True
        return False

    def h(self):
        # Heuristic function
        h_cnt = 0
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.__check_collisions((i, self[i]), (j, self[j])):
                    h_cnt += 1
                    break
        return h_cnt

    
    def g(self):
        # g Function for A* Algorithm
        g_cnt = 0
        for i in range(self.n):
            g_cnt += abs(self[i] - self.begin_state[i])
        return g_cnt
    
    def next_states(self):
        # Return next states from all possible actions
        states = []
        for i in range(self.n):
            if self[i] > 0:
                state = self.deepcopy()
                state[i] = state[i] - 1
                states.append(state)
            if self[i] < self.n-1:
                state = self.deepcopy()
                state[i] = state[i] + 1
                states.append(state)
        return states

if __name__ == '__main__':

    n = int(input('Please input n: '))

    search = GreedySearch(StateThreatenedQueens.random(n), verbose=False)

    search2 = AStarSearch(StateThreatenedQueens.random(n), verbose=False)

    while not search.step():
        pass
