from enum import Enum
from state import Connect4State

class AgentType(Enum):
    Bot = 1
    Human = 2
    
# TODO! move methods to outside of class
class Agent():
    
    def __init__(self,  
                decision_depth:int,
                piece_sign:str, # sign of agent's pieces on the board
                mode:AgentType = AgentType.Bot):
        # TODO: add env type
        '''
        piece_sign = sign of agent pieces on the board
        goal = agent goal, whether 
        mode = whether to make moves itself or get moves from input
            -> goal will be ignored if mode = AgentType.Human
        '''
        self.depth = decision_depth
        self.piece_sign = piece_sign
        self.mode = mode
        
    def __min_value(self,
                    curr_state:Connect4State, # current state
                    depth : int, # depth to traverse in adversial tree
                    alpha : int, # alpha for alpha-beta prunning 
                    beta : int # beta for alpha-beta prunning
                    ):
        ''' 
        Implementation of min for prunned minimax algorithm
        '''
        if depth == 0 or curr_state.isTerminal:
            return (-1, curr_state.value)
        
        minEval = +1e6
        minAction = -1
        for action, child_state in curr_state.next_states():
            _, eval = self.__max_value(child_state, depth - 1, alpha, beta)
            if eval < minEval:
                minEval = eval
                minAction = action
            beta = min(beta, eval)
            if minEval <= alpha:
                break
        return (minAction, minEval)
    
    def __max_value(self,
                    curr_state:Connect4State, # current state
                    depth : int, # depth to traverse in adversial tree
                    alpha : int, # alpha for alpha-beta prunning 
                    beta : int # beta for alpha-beta prunning 
                    ):
        ''' 
        Implementation of Max for prunned minimax algorithm
        '''
        if depth == 0 or curr_state.isTerminal:
            return (-1, curr_state.value)
        
        maxEval = -1e6
        maxAction = -1
        for action, child_state in curr_state.next_states():
            _, eval = self.__min_value(child_state, depth - 1, alpha, beta)
            if eval > maxEval:
                maxEval = eval
                maxAction = action
            alpha = max(alpha, eval)
            if beta <= maxEval:
                break
        return (maxAction, maxEval)
    
    
    def play(self, 
            curr_state : Connect4State,
            ):
        '''
        This function takes current state and make
        a move based on that.
        '''
                
        # Getting human input and check it to be in range [0,7]
        if self.mode == AgentType.Human:
            print(str(curr_state))
        while self.mode == AgentType.Human:
            action = int(input(f'Please input your move(integer 0~{str(len(curr_state.board[0])-1)}):  '))
            if not action in range(len(curr_state.board[0])):
                print(f'Input should be a integer in range of [0, {str(len(curr_state.board[0])-1)}]')
            else:
                return action

        # Making a move using minimax algorithm
        action = -1
        if curr_state.curr_player_number == 1:
            action,_ = self.__max_value(curr_state, self.depth, -1e6, +1e6)
        else:
            action,_ = self.__min_value(curr_state, self.depth, -1e6, +1e6)  
        print(f"Bot's move: {str(action)}")      
        return action
                
        
            