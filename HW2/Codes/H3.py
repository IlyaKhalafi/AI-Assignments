from NQueens import *

class StateDiagonalCollisions(State):

    def random(n):
        # Making a random state with board size n
        from random import shuffle
        begin_state = [i for i in range(n)]
        shuffle(begin_state)
        return StateDiagonalCollisions(begin_state)

    def __check_diag_collisions(self, a, b):
        if a == b:
            return False
        if abs(a[0]-b[0]) == abs(a[1]-b[1]):
            return True
        return False


    def h(self):
        # Heuristic function
        h_cnt = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                h_cnt += int(self.__check_diag_collisions((i,self[i]), (j, self[j])))
        return h_cnt

    
    def g(self):
        # g Function for A* Algorithm
        perm_indices = [self.curr_indices.index(i) for i in self.begin_state] # permutation array 

        inv_cnt = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if (perm_indices[i] > perm_indices[j]):
                    inv_cnt += 1
        return inv_cnt
    
    def next_states(self):
        # Return next states from all possible actions
        states = []
        for i in range(self.n-1):
            state = self.deepcopy()
            state[i], state[i+1] = state[i+1], state[i]
            states.append(state)
        return states

if __name__ == '__main__':

    n = int(input('Please input n: '))

    search = GreedySearch(StateDiagonalCollisions.random(n), verbose=True)

    # search = AStarSearch(StateDiagonalCollisions.random(n), verbose=False)

    while not search.step():
        pass

