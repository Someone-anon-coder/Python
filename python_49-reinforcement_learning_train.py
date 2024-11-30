import time
import pygame
import random
import numpy as np
from collections import defaultdict

class TicTacToe:
    def __init__(self) -> None:
        """
            Args: 
                None

            Returns:
                None

            Concept:
                Initializes class Tictactoe and sets up the board, current player, and player wins and pygame.
        """
        
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.player1_wincount = 0
        self.player2_wincount = 0
        self.draw_count = 0
        self.init_pygame()

    def init_pygame(self) -> None:
        """
            Args:
                None

            Returns:
                None

            Concept:
                Initializes pygame and sets up the screen, font, and clock.
        """
        
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Tic-Tac-Toe Training")
        self.font = pygame.font.Font(None, 74)
        self.clock = pygame.time.Clock()

    def reset(self) -> np.ndarray:
        """
            Args:
                None
            
            Returns:
                None
            
            Concept:
                Resets the board, current player, and player wins.
        """
        
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.render()
        
        return self.board

    def available_actions(self) -> list:
        """
            Args:
                None
            
            Returns:
                list of available actions
            
            Concept:
                Returns a list of all available actions for the agent on the board.
        """
        
        return list(zip(*np.where(self.board == 0)))
    
    def make_move(self, action: tuple[int, int]) -> tuple[int, bool]:
        """
            Args:
                action: Action selected by the agent (tuple)
            
            Returns:
                value of reward and whether the game is over with this move
                
            Concept:
                Makes a move on the board and updates the current player.
        """
        
        if self.board[action] == 0:
            self.board[action] = self.current_player
            reward, done = self.check_winner()
            self.render()
            self.current_player = -self.current_player
            
            return reward, done
        return 0, False
    
    def check_winner(self) -> tuple[int, bool]:
        """
            Args:
                None
            
            Returns:
                player who won and that the game is over
            
            Concept:
                Checks if there is a winner on the board.
        """
        
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player) or np.all(self.board[:, i] == self.current_player):
                print(f"Player {1 if self.current_player == 1 else 2} wins!")
                print(self.board)
                
                if self.current_player == 1:
                    self.player1_wincount += 1
                else:
                    self.player2_wincount += 1
                
                return 1 if self.current_player == 1 else -1, True
        
        if np.all(np.diag(self.board) == self.current_player) or np.all(np.diag(np.fliplr(self.board)) == self.current_player):
            print(f"Player {1 if self.current_player == 1 else 2} wins!")
            print(self.board)
            
            if self.current_player == 1:
                self.player1_wincount += 1
            else:
                self.player2_wincount += 1
                
            return 1 if self.current_player == 1 else -1, True
        
        if not np.any(self.board == 0):
            print("It's a draw!")
            print(self.board)
            
            self.draw_count += 1
            
            return 0, True
        
        return 0, False

    def check_critical(self, player: int) -> tuple[float, tuple[int, int]]:
        """

        Args:
            player: specifier of player

        Returns:
            reward and critical position on the board and location of critical position.

        Concept:
            Checks if there is a critical position on the board. Critical position is a position that if one move can decide the winner.
        """
        
        for i in range(3):
            if np.sum(self.board[i, :] == player) == 2 and np.any(self.board[i, :] == 0):
                return 0.1, (i, np.where(self.board[i, :] == 0)[0][0])
            
            if np.sum(self.board[:, i] == player) == 2 and np.any(self.board[:, i] == 0):
                return 0.1, (np.where(self.board[:, i] == 0)[0][0], i)
        
        if np.sum(np.diag(self.board) == player) == 2 and np.any(np.diag(self.board) == 0):
            idx = np.where(np.diag(self.board) == 0)[0][0]
            return 0.1, (idx, idx)
        
        if np.sum(np.diag(np.fliplr(self.board)) == player) == 2 and np.any(np.diag(np.fliplr(self.board)) == 0):
            idx = np.where(np.diag(np.fliplr(self.board)) == 0)[0][0]
            return 0.1, (idx, 2 - idx)
        
        opponent = -player
        for i in range(3):
            if np.sum(self.board[i, :] == opponent) == 2 and np.any(self.board[i, :] == 0):
                return -0.1, (i, np.where(self.board[i, :] == 0)[0][0])
            
            if np.sum(self.board[:, i] == opponent) == 2 and np.any(self.board[:, i] == 0):
                return -0.1, (np.where(self.board[:, i] == 0)[0][0], i)
        
        if np.sum(np.diag(self.board) == opponent) == 2 and np.any(np.diag(self.board) == 0):
            idx = np.where(np.diag(self.board) == 0)[0][0]
            return -0.1, (idx, idx)
        
        if np.sum(np.diag(np.fliplr(self.board)) == opponent) == 2 and np.any(np.diag(np.fliplr(self.board)) == 0):
            idx = np.where(np.diag(np.fliplr(self.board)) == 0)[0][0]
            return -0.1, (idx, 2 - idx)
        
        return 0.2, None

    def render(self) -> None:
        """
            Args:
                None
            
            Returns:
                None
            
            Concept:
                Renders the board on the screen.
        """
        
        self.screen.fill((255, 255, 255))
        for row in range(3):
            for col in range(3):
                if self.board[row, col] == 1:
                    pygame.draw.line(self.screen, (0, 0, 0), (col * 100 + 15, row * 100 + 15), (col * 100 + 85, row * 100 + 85), 15)
                    pygame.draw.line(self.screen, (0, 0, 0), (col * 100 + 15, row * 100 + 85), (col * 100 + 85, row * 100 + 15), 15)
                elif self.board[row, col] == -1:
                    pygame.draw.circle(self.screen, (0, 0, 0), (col * 100 + 50, row * 100 + 50), 40, 15)
        
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 100), (300, i * 100), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (i * 100, 0), (i * 100, 300), 5)

        pygame.display.flip()
        
        # time.sleep(0.1)  # Delay for 100 milliseconds # Uncomment to see the moves taken by the agent in real time

    def close_pygame(self) -> None:
        """
            Args:
                None
            
            Returns:
                None
            
            Concept:
                Closes the pygame window.
        """
        
        pygame.quit()

class QLearningAgent:
    def __init__(self, player: int, epsilon: int=0.1, alpha: int=0.5, gamma: int=0.9) -> None:
        """
            Args:
                player: The specifier for the current player
                epsilon: The exploration rate
                alpha: The learning rate
                gamma: The discount factor
            
            Returns:
                None
            
            Concept:
                Initializes the class QLearningAgent with the given parameters; and sets the q_table to an empty dictionary.
        """
        
        self.q_table = defaultdict(lambda: 0)
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.player = player
    
    def get_state(self, board: np.ndarray) -> tuple:
        """
            Args:
                board: The current board being played at the moment
            
            Returns:
                State as the board condition
                
            Concept:
                Returns the state as the board condition.
        """
        
        return tuple(map(tuple, board))
    
    def choose_action(self, board: np.ndarray, available_actions: list) -> int:
        """
            Args:
                board: The current board being played at the moment
                available_actions: A list of actions that can be taken on the current board
            
            Returns:
                A calculated action of the available actions
            
            Concept:
                Returns a calculated action of the available actions and if epsilon value is greater than a random value then a random action is returned.
        """
        
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_actions)
        
        q_values = [self.q_table[(self.get_state(board), action)] for action in available_actions]
        max_q = max(q_values)
        
        return random.choice([a for a, q in zip(available_actions, q_values) if q == max_q])
    
    def update_q_table(self, state: tuple, action: int, reward: int, next_state: tuple, next_actions: list) -> None:
        """
            Args:
                state: The current board at the moment
                action: Action taken by the agent
                reward: reward given for that action in that condition
                next_state: The next board to played
                next_actions: Actions available to model on the next board
            
            Returns:
                None
            
            Concept:
                Updates the q_table with the given parameters.
        """
        
        current_q = self.q_table[(state, action)]
        if next_actions:
            max_next_q = max([self.q_table[(next_state, a)] for a in next_actions])
        else:
            max_next_q = 0
        self.q_table[(state, action)] = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
    
    def save_model(self, filename: str) -> None:
        """
            Args:
                filename: filename for the q_table to be saved in
            
            Returns:
                None
            
            Concept:
                Saves the q_table in the given filename.
        """
        
        import pickle
        with open(filename, 'wb') as f:
            pickle.dump(dict(self.q_table), f)
    
    def load_model(self, filename: str) -> None:
        """
            Args:
                filename: filename for the q_table to be loaded from
            
            Returns:
                None
            
            Concept:
                Loads the q_table from the given filename.
        """
        
        import pickle
        with open(filename, 'rb') as f:
            self.q_table = defaultdict(lambda: 0, pickle.load(f))

def train(episodes: int, epsilon: float, alpha: float, gamma: float) -> None:
    env = TicTacToe()
    agent1 = QLearningAgent(player=1, epsilon=epsilon, alpha=alpha, gamma=gamma)
    agent2 = QLearningAgent(player=-1, epsilon=epsilon, alpha=alpha, gamma=gamma)
    
    try:
        for episode in range(episodes):
            print(f"Episode {episode + 1}/{episodes}")
            
            state = env.reset()
            done = False
            while not done:
                player = env.current_player
                agent = agent1 if player == 1 else agent2
                state_tuple = agent.get_state(state)
                actions = env.available_actions()
                action = agent.choose_action(state, actions)
                
                reward, critical_location = env.check_critical(player)
                
                """
                    If critical location is given and agent wins, give 2 reward points
                    If critical location is given and agent doesn't mark there and loses, give 2 penalty points
                """
                if critical_location:
                    if action == critical_location:
                        reward = 2
                    elif done and reward == -1:
                        reward = -2
                
                reward_move, done = env.make_move(action)
                next_state_tuple = agent.get_state(env.board)
                next_actions = env.available_actions()
                agent.update_q_table(state_tuple, action, reward + reward_move, next_state_tuple, next_actions)
                
                if done and reward != 0:
                    other_agent = agent2 if player == 1 else agent1
                    other_agent.update_q_table(state_tuple, action, -reward, next_state_tuple, next_actions)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

    finally:
        env.close_pygame()
        print(f"Player 1 wins: {env.player1_wincount} times")
        print(f"Player 2 wins: {env.player2_wincount} times")
        print(f"Draws: {env.draw_count}")

    agent1.save_model('Files/agent1_q_table.pkl')
    agent2.save_model('Files/agent2_q_table.pkl')

if __name__ == "__main__":
    epsilon = 0.25    # Exploration Rate
    alpha = 0.07      # Learning Rate
    gamma = 0.8       # Discount Factor
    episodes = 10000 # Iteration Count
    
    train(episodes=episodes, epsilon=epsilon, alpha=alpha, gamma=gamma)