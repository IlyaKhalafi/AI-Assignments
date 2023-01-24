from agent import *
from environment import Connect4Env
from state import Connect4State

if __name__ == '__main__':
    agent1 = Agent(4, '*', mode=AgentType.Human)
    agent2 = Agent(4, 'o', mode=AgentType.Bot)
    
    agents_sign = {-1: agent1.piece_sign,
                   1: agent2.piece_sign}
    
    begin_state = Connect4State.empty_board(8, 6, agents_sign)
    env = Connect4Env(begin_state, [agent1, agent2])
    
    while not env.step():
        pass
    env.print_status()