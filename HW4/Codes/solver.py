

class MinConflictSolver():
    
    def __init__(self, problem):
        self.problem = problem
        self.problem.shuffle_assignment()

    def step(self):
        '''
        This method executes 1 step of min conflict alogrithm.
        returns True if answer is found and False otherwise.
        '''
        var = self.problem.get_conflict()

        # If there is no conflict, then we have found the answer
        if not var:
            return True

        # setting max value of conflicts
        min_conflict = len(self.problem.variables)

        # settings first element of domain, in case that
        # no better option was found
        min_conflict_value = var.domain[0]

        # finding value with minimum conflicts
        for value in var.domain:
            var.value = value
            if var.count_conflicts() < min_conflict:
                min_conflict = var.count_conflicts()
                min_conflict_value = value

        # setting value with minimum conflicts
        var.value = min_conflict_value

        # If we have not found the answer and there
        # was no other conflict, then return True
        if not self.problem.get_conflict():
            return True
        
        # returning False because answer is not found yet
        return False
