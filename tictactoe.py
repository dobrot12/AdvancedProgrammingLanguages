import numpy as np
import random
import hashlib
from itertools import permutations
import pandas as pd
import copy 
import random 
import numpy as np 
import math 
import os



class tictactoe:
    """
    Class containing the game logic
    
    Attributes:
        move
        Function to make a move
        
        switch_player
        switches the player after a move
        
        reset_board
        resets the board after the game has finished
        

        
        
    
    Methods:
    
        get_random_first_player: int
        Returns a starting player randomly
        
        possible_move: list
        Returns a list of all possible moves depending on the game state
        
        get_current_state: str
        returns the current state of the game as a hex code used to check if the state
        has allready been recorded
        
        calc_reward_q: int
        returns the calculated reward fo the q agent depending on the game state
        
        check_full_board: Bool 
        Checks if the board is full 
        
        check_win: Bool
        Checks if the game is won 
        
        
        
        
        
        
    
    
    
    
    """

    def __init__(self, size):
        self.size = size
        self.board_size = size * size
        self.board = np.zeros(self.board_size)
        self.p = [1,100]
        self.p_turn = self.get_random_first_player()
        self.win = False
        self.full_board = False
        self.reward = 0

      
       
        
       
    def get_random_first_player(self):
        """returns random first player
        Parameters
        ----------
        none
        """
        
       
        p_turn_first = self.p[random.randint(0, 1)]
        return p_turn_first
        
        
    
    def possible_move(self):
        """return all possible moves
        Parameters
        ----------
        none
        """
  
        possible_moves = np.argwhere(self.board == 0)
        return possible_moves
    
    def move(self,move):
        """makes a move
        Parameters
        ----------
        none
        """
        
        
        self.board[move] = self.p_turn#here comes logic from player
        
        self.check_win()
        self.check_full_board()
        
        self.switch_player()
        
    def get_current_state(self):
        """returns current state as hexcode
        Parameters
        ----------
        none
        """
        

        return hashlib.sha1(self.get_board()).hexdigest() 
        game.win 
    
    def calc_reward_q(self):
        """calculates rewards for q agent
        Parameters
        ----------
        none
        """
        if sum([self.win,self.full_board])==0:
            self.reward = 0
        elif self.win and self.p_turn==100:
            self.reward = 10
            self.win = False
        elif self.win and self.p_turn==1:
            self.reward = -10
            self.win = False
            
        elif self.full_board:
            self.reward = 5
            self.full_board = False
    
      
    def switch_player(self):
        """switches player
        Parameters
        ----------
        none
        """
        if sum([self.win,self.full_board])==0:
      
             self.p_turn = [i for i in self.p if i!=self.p_turn][0]
        
           
         
             
    
    def check_win(self):
        """checks if someone has won 
        Parameters
        ----------
        none 
        """
        local_board = np.copy(self.board.reshape([self.size, self.size]))
        summs = np.concatenate([local_board.sum(axis=0),  # columns
                               local_board.sum(axis=1),  # rows
                               np.trace(local_board),  # diagonal
                               np.trace(np.fliplr(local_board))], axis=None)
        if  sum(summs==self.p_turn*3)>0:
            self.win =True
        
        else:
            self.win =False
        win = self.win
            
        return win
            
    def check_full_board(self):
        """check if board is full
        Parameters
        ----------
        none
        """        
        
        if len(np.argwhere(self.board == 0))==0:
            self.full_board = True
        else:
            self.full_board = False
        full_board = self.full_board
            
        return full_board
    def reset_board(self):
        """resets board to initial state
        Parameters
        ----------
        none
        """
        
        self.board = np.zeros(self.board_size)
        self.p = [1,100]
        self.p_turn = self.get_random_first_player()
        self.win = False
        self.full_board = False
    
    def get_board(self):
        """returns a copy of the board
        Parameters
        ----------
        none
        """
        return np.copy(self.board.reshape([self.size, self.size]))
         
            
        
class Player:
    """
    Class containing the game logic
    
    Attributes:
        play_again
        Function to invoke a new game
        
        play
        invokes a game of tictactoe
        
        
        q_move_2
        functions that lets trained agent make a move
        
        make_move
        function to make moves used to train the agent 
        
        show_board
         prints the board into the console
         
         random_move
         makes a random move used to train the agent
         
                 q_move
        makes a move for the agent
        
        update_q
        updates the values in the q table
         

    Methods:
    
        get_qtable: matrix
        Returns the q table
        
        get_board_to_state: list
        returns board to state
        
        wins: Bool
        returns rewards for the agent
        
        get_random_first_player: int
        Returns a starting player randomly
        
        possible_move: list
        Returns a list of all possible moves depending on the game state
        
        get_current_state: str
        returns the current state of the game as a hex code used to check if the state
        has allready been recorded
        
        calc_reward_q: int
        returns the calculated reward fo the q agent depending on the game state
        
        check_full_board: Bool 
        Checks if the board is full 
        
        check_win: Bool
        Checks if the game is won 
        
    """
    def __init__(self,game, alpha=0.01, gamma=0.7, epsilon=1):
        """initialize
        Parameters
        ----------
        game: object
        game object
        
        player:int
        turn of player
        
        qtable: dict 
        qtable
        
        state_list:list
        list of states
        
        alpha: float
        learning rate
        
        gamma:float
        weight on future rewards
        
        epsilon:float
        threhshold to decide if agent should explore or exploit
        
        reward:int
        rewards form the game
        
        """
        self.game = game
        self.player = game.p_turn
        self.qtable = {}
        self.board_to_state = {}
        self.state_list = []
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.reward = 0
        self.our_reward_lut = {10: -10, 5: 5, 0: 0, -10: 10}
   
        

        
            
            
            
         
    def play(self):
        """let you play a game

        Parameters
        ----------
        none
        ------
        
        """
      
        if game.p_turn==1:
             
                move = int(input("Enter index number of your move (0 to 8): "))
              
              
               
                
                
                try:
                    
                    if move in game.possible_move():
                        game.move(move)
                        win = game.check_win()
                        full_board = game.check_full_board()
                      
                      
                        if win==True:
                            print("winner is: ",self.game.p_turn)
                          
                            game.reset_board()
                      
                        
                        elif full_board==True:
                            print("draw")
                         
                            game.reset_board()
                          
                    else:
                        print("Choose from the set of possible moves")
                        self.play()
                except:
                    
                    print("There was an error. Try Again")
                    self.play()
        else:
                
                self.q_move_2()
                print("AI made move board now looks like this:")
                
            
                win = game.check_win()
                full_board = game.check_full_board()
               
              
                if win==True:
                    print("winner is: ",game.p_turn)
                
                    game.reset_board()
              
                
                elif full_board==True:
                    print("draw")
               
                    game.reset_board()
                   
    def q_move_2(self):
        """lets the trained agent make moves

        Parameters
        ----------
       none

        """
        possible_moves = game.possible_move()
        self.current_state = game.get_current_state()

        # If the current_state does not exist in the qtable, insert it
        if self.current_state not in self.qtable:
            self.action = random.choice(possible_moves)
            # New entry in the qtable, init to zero.
           

        # Insert epsilon choice here, exploit or explore
        
            
            game.move(self.action)  # Random choice

            
            
        else:  # Exploit our qtable
            self.action =[int(max(self.qtable[self.current_state] , key=self.qtable[self.current_state].get).strip('[&]') ) ]  
            game.move(self.action) 

           
     

        
   
        
    def get_qtable(self):
        """returns qtable
        Parameters
        ----------
        none
        
        """
        return self.qtable

    def get_board_to_state(self):
        """returns board to state
        Parameters
        ----------
        none
        """
        
        return self.board_to_state
        
    
    
    def make_move(self):
        """Makes moves to train the agent 
        Parameters
        ----------
        none
        """
        
        self.player = game.p_turn
        
        self.show_board()

        if self.player==1:
                  
                    
                    self.random_move()
                    win = game.check_win()
                    full_board = game.check_full_board()
                  
                    if win==True:
                        print("winner is: ",self.player)
                        self.reward = -10
                        game.reset_board()
                    
                    elif full_board==True:
                        print("draw")
                        self.reward = 5
                        game.reset_board()
            
                  
        else:
            
                    
                    self.q_move()
                
                    win = game.check_win()
                    full_board = game.check_full_board()
                    
                    if win==True:
                        print("winner is: ",self.player)
                        self.reward = 10
                        game.reset_board()
                    
                    elif full_board==True:
                        print("draw")
                        self.reward = 5
                        game.reset_board()
      
    def show_board(self):
        """displays the board in the console
        Parameters
        ----------
        none
        """
        
        
        for row in game.get_board():
            
       
            
            for item in row:
                if item==100:
                    item="X"
                elif item == 1:
                    item = "o"
                elif item ==0:
                    item = "-"
                
                print(item, end=" ")
            print()
        print(f"Board{os.linesep}-")
                
    def wins(self,state, n_move):
        """returns reward
        Parameters
        ----------
        state:list
        state of the board
        n_move:
            number of turns played
        """
        
        state = state[0:n_move]
        win_state = [
                [1,2,3],
                [4,5,6],
                [7,8,9],
                [1,4,7],
                [2,5,8],
                [3,6,9],
                [1,5,9],
                [7,5,3],
            ]
        if n_move%2!=0:
                
      
                if state[::2] in win_state:
                    val = 10
                else:
                    val =0
        else:
                state = state[1:n_move]
                if state[::2] in win_state:
                    val = -10
                else:
                    val = 0
        return val
         
    def random_move(self):
        """makes a randommove
        Parameters
        ----------
        none
        """
        
        
        possible_move = game.possible_move()
        move = random.choice(possible_move)
        
        action = move
        game.move(move)
      
        self.new_state_after_rand = game.get_current_state()
        if self.new_state_after_rand not in self.qtable:
            # New entry in the qtable, init to zero.
            self.board_to_state[self.new_state_after_rand] = game.get_board()
            action_vs_qvalue = dict()
            for action in possible_move:
                    action_vs_qvalue[str(action)] = 0
       
            self.qtable[self.new_state_after_rand] = action_vs_qvalue
            game.calc_reward_q()
            self.reward_after_rand=game.reward
            self.qtable[self.new_state_after_rand][str(action)] =game.reward
        else:
            game.calc_reward_q()
            self.reward_after_rand=game.reward
            self.qtable[self.new_state_after_rand][str(action)] =game.reward
      

    def q_move(self):
        """makes a move for the q agent, records new states in the q table
        Parameters
        ----------
        none
        """
        possible_moves = game.possible_move()
        self.current_state = game.get_current_state()

        # If the current_state does not exist in the qtable, insert it
        if self.current_state not in self.qtable:
            # New entry in the qtable, init to zero.
            self.board_to_state[self.current_state] = game.get_board()
            action_vs_qvalue = dict()
            for action in possible_moves:
                    action_vs_qvalue[str(action)] = 0
       
            self.qtable[self.current_state] = action_vs_qvalue
           

        # Insert epsilon choice here, exploit or explore
        if random.uniform(0, 1) < self.epsilon:
            self.action = random.choice(possible_moves)
            game.move(self.action)  # Random choice
            self.new_state = game.get_board()
            game.calc_reward_q()
            self.reward = game.reward
           
            
            
        else:  # Exploit our qtable
            self.action =[int(max(self.qtable[self.current_state] , key=self.qtable[self.current_state].get).strip('[&]') ) ]  
            game.move(self.action) 
            self.new_state = game.get_board()
            game.calc_reward_q()
            self.reward = game.reward
              
        self.qtable[self.current_state][str(self.action)] = self.reward
        
        if len(self.qtable)>1:
            self.update_q()
   
 
            
        
     
            
            
            
    def update_q(self):
        """updates the q table 
        Parameters
        ----------
        none
        """
     
        old_value = self.qtable[self.current_state][str(self.action)]
           
        next_max = max(self.qtable[self.new_state_after_rand].values())
         # In case the tree for next state has not been made yet, simply return 0
             

        # Note that the reward we actually get is the reward after the tree has made its move. We then reverse that reward vs the lut to get our own.
        new_value = (1 - self.alpha) * old_value + self.alpha * (
                    self.our_reward_lut[self.reward_after_rand] + self.gamma * next_max)
        self.qtable[self.current_state][str(self.action)] = new_value
        self.epsilon = self.epsilon*0.9999
        
        


game= tictactoe(3) 
inst = Player(game)

wins = []
def train(n):
    """wraper function to train the q agent
        Parameters
        ----------
        n: int 
        number of training epochs              
        """
        
    for i in range(0,n):
   
        inst.make_move()
        print("training ",(i/n)*100,"% done")
    
def play():
    """wraper function to initialise the game
        Parameters
        ----------
        none
        """
    game.reset_board()

    while True:
        inst.show_board()
        inst.play() 
        
if __name__ == "__main__":

    train(10000)
    play()


