from queue import PriorityQueue
from abc import ABC, abstractmethod

class State(ABC):
    # This is an abstract class which should be implemented for differeNT heuristics
    # Should not be used directly
    from copy import deepcopy
    
    def __init__(self, queens_indices):
        self.n = len(queens_indices)
        self.__begin_state = queens_indices
        self.curr_indices = queens_indices
    
    @abstractmethod    
    def random(n):
        # Making a random state with board size n
        return None
    
    @abstractmethod
    def h(self):
        # Heuristic function
        pass
    
    @abstractmethod
    def g(self):
        # g Function for A* Algorithm
        pass
    
    @abstractmethod
    def next_states(self):
        # Return next states from all possible actions
        pass

    @property
    def begin_state(self):
        return self.__begin_state
    
    def __getitem__(self, indices):
        return self.curr_indices[indices]

    def __setitem__(self, indices, items):
        self.curr_indices[indices] = items

    # Next two methods will be used in PriorityQueue
    # We will just define them to skip errors
    def __gt__(self, other):
        return self.curr_indices > other.curr_indices

    def __eq__(self, other):
        return self.curr_indices == other.curr_indices

    def __repr__(self):
        return ''.join([str(num) for num in self.curr_indices])

class SearchMethod(ABC):
    # Abstract class to use for implementing search algorithms

    def __init__(self, state, verbose=False):
        self.n = state.n
        self.state = state
        self.pq = PriorityQueue()
        self.passed_states = {str(state)}
        self.verbose = verbose
        self.iterations = 0

    @property
    def status(self):
        h = self.state.h()
        if h == 0:
            return f'Answer found : {str(self.state.curr_indices)} during {self.iterations} iterations'
        
        if self.pq.empty() and not self.state.curr_indices == self.state.begin_state:
            return f'No answer was found for beginning state {self.state.begin_state}'
        
        return f'Ongoing search on {self.state.curr_indices} --> h = {str(h)}'

    @abstractmethod
    def step(self):
        pass

class GreedySearch(SearchMethod):

    def __push_state(self, new_state):
        if not str(new_state) in self.passed_states:
            self.pq.put((new_state.h(), new_state))
            self.passed_states.add(str(new_state))

    def step(self):
        for state in self.state.next_states():
            self.__push_state(state)

        if self.pq.empty():
            print(f'No answer was found for beginning state {self.state.begin_state}')
            return True

        h, self.state = self.pq.get()
        self.iterations += 1
        
        if self.verbose == True:
            print(f'queens indices in rows: {str([(i,self.state[i]) for i in range(self.n)])} --> h = {str(h)}')

        if h == 0:
            print(self.status)
            return True

        return False
        
        
class AStarSearch(SearchMethod):

    def __push_state(self, new_state):
        if not str(new_state) in self.passed_states:
            self.pq.put((new_state.h() + new_state.g(), new_state))
            self.passed_states.add(str(new_state))

    def step(self):
        for state in self.state.next_states():
            self.__push_state(state)

        if self.pq.empty():
            print(f'No answer was found for beginning state {self.state.begin_state}')
            return True

        f, self.state = self.pq.get()
        self.iterations += 1
        
        if self.verbose == True:
            print(f'queens indices in rows: {str([(i,self.state[i]) for i in range(self.n)])} --> g+h = {str(f)}')
    
        if self.state.h() == 0:
            print(self.status)
            return True

        return False

