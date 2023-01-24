
class Connect4State():
    from copy import deepcopy
    
    def __init__(self,
                board:list, # 2D array of integers representing game board
                            # each cell is either of these:
                            # Empty(0), MaxPlayerPiece(1), MinPlayerPiece(-1)
                agents_sign:dict, # sign of each agent's piece on the board
                curr_player_number:int = -1 # 1 or -1 depending on players min or max
                ):
        '''
        begin_state: beginning state of the pieces
        '''
        self.board = board
        self.isTerminal = False
        self.draw_flag = False
        self.value = self.__calculate_value()
        self.agents_sign = agents_sign
        self.curr_player_number = curr_player_number

    def empty_board(width:int, height:int, agents_sign:dict):
        '''
        This is a class method.
        Instead of using the __init__ function, this method can make
        an state with empty board of size width x height and agents sign
        and returns this instance of the class.
        '''
        board = [[0 for i in range(width)] for j in range(height)]
        return Connect4State(board, agents_sign)
    
    def next_states(self):
        # TODO! Caution: yields value and action together
        '''
        This is successor function.
        yields all possible next moves
        '''
        for action in range(len(self.board[0])):
            new_state = self.apply_action(action, self.curr_player_number)
            if new_state != None:
                yield (action, new_state)
    
    def apply_action(self,
                    action : int, # Integer in range [0, 7]
                    player_number : int # palyer that made the move, 1 or -1
                    ):
        '''
        Takes an action and return a new state 
        that chosen action is applied to.
        action: is equal to index of column that
        is chosen to put a piece in it
        '''
        # If chosen column is full, return null   
        if self.board[-1][action] != 0:
            return None
        
        # Finding first empty row in action column
        index = 0
        while self.board[index][action] != 0:
            index += 1
            
        # Making new state and returning it
        new_board = Connect4State.deepcopy(self.board)
        new_board[index][action] = player_number
        return Connect4State(new_board, self.agents_sign, -player_number)
    
    def __check_potential(self, start, end):
        '''
        calculates heuristic for 4 continous cells from
        start cell to end cell.
        start & end are tuples that contain
        x,y of start cell and end cell
        '''
        # First we fetch continous rows out of the board
        x_direction = int((end[0]-start[0]) / abs(end[0]-start[0]) if end[0]-start[0]!=0 else 0)
        y_direction = int((end[1]-start[1]) / abs(end[1]-start[1]) if end[1]-start[1]!=0 else 0)
        cells = None
        if x_direction == 0:
            # For columns
            cells = [self.board[start[0]][j] 
                    for j in range(start[1], end[1]+y_direction, y_direction)            
                    ]
        elif y_direction == 0:
            # For rows
            cells = [self.board[i][start[1]] 
                    for i in range(start[0], end[0]+x_direction, x_direction)           
                    ]
        else:
            # For diagonals
            cells = [self.board[start[0]+x_direction*i][start[1]+i*y_direction] 
                    for i in range(0, abs(end[0]-start[0])+1)           
                    ]
        
        ''' 
        Rule 1: if cells have more than 1 color
        Then postision is equal because neither
        of 2 players can win in this cells
        '''
        if 1 in cells and -1 in cells:
            return 0

        '''
        Rule 2: value of these 4 cells is 10 to the power 
        same colored piece in these 4 continous cells
        with sign equal to player that has pieces in these
        4 cells
        '''
        cells_sum = sum(cells)
        cells_value = 0
        if cells_sum != 0:
            cells_value = (10 ** abs(cells_sum)) * (cells_sum / abs(cells_sum))


        # if all 4 cells have same pieces then
        # we shuold mark this state as a terminal
        if abs(cells_sum) == 4:
            self.isTerminal = True
        
        return cells_value    
    
    def __calculate_value(self):
        '''
        Calculates heuristic function for current game board as value
        h(state) =  amount of same colored pieces in 4 continous cells that
                    does not contains more than 1 color of pieces
        '''
        x_size = len(self.board)
        y_size = len(self.board[0])
        
        value = 0
        '''
        checking 4 continous cells
        (3, 0): right    | (0, 3): up
        (3, 3): up-right | (3, -3): bottom right
        other directions will be checked symmetrically
        during process of other cells
        '''
        directions = [(3, 0), (0, 3), (3, 3), (3, -3)]
        self.draw_flag = True
        for i in range(x_size):
            for j in range(y_size):
                for direction in directions:
                    if i + direction[0] in range(x_size) and j + direction[1] in range(y_size):
                        potential = self.__check_potential((i,j), (i+direction[0],j+direction[1]))       
                        if potential != 1e4:
                            self.draw_flag = False
                        value += potential
        return value
                    
    def __repr__(self):
        output = '-' * (2*(len(self.board) + 3)) + '\n'
        board = self.board.copy()
        board.reverse()
        for row in board:
            output += '|'
            for piece in row:
                output += self.agents_sign[piece] if piece != 0 else ' '
                output += '|'
            output += '\n'
            output += '-' * (2*(len(board) + 3)) + '\n'
        for i in range(len(self.board[0])):
            output += f' {i}'
        output += '\n'
        return output