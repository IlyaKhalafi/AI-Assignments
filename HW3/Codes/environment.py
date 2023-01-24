class Connect4Env():
    
    def __init__(self,
                begin_state,
                agents:list):
        self.curr_state = begin_state
        self.agents = agents
        self.__winner = -1 # index of winner, = -1 means no winner yet
        
    
    def step(self):
        if self.curr_state.isTerminal:
            return True
        
        for i, agent in enumerate(self.agents):
            new_state = None
            while new_state == None:
                action = agent.play(self.curr_state.deepcopy())
                new_state = self.curr_state.apply_action(action, 2*i-1)
            self.curr_state = new_state
            
            if self.curr_state.isTerminal:
                self.__winner = i
                return True
            
        return False
    
    def print_status(self):
        if self.curr_state.draw_flag:
            print('Game Result : Draw!')
        elif self.__winner == -1:
            print('Game is not finished yet!')
        else:
            print(str(self.curr_state))
            print(f'player {self.__winner} with sign {self.agents[self.__winner].piece_sign} won the game!')
            print(f"Winner's Agent Type: {self.agents[int((self.__winner+1)/2)].mode.name}")
            print(f'final value: {self.curr_state.value}\n')
        