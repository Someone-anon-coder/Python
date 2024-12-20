import time
import pygame
import pickle
import random

import numpy as np
from collections import defaultdict

class TicTacToe:
    def __init__(self) -> None:
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.init_pygame()

    def init_pygame(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Tic-Tac-Toe Testing")
        self.font = pygame.font.Font(None, 74)
        self.clock = pygame.time.Clock()

    def reset(self) -> np.ndarray:
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.render()
        
        return self.board

    def available_actions(self) -> list:
        return list(zip(*np.where(self.board == 0)))

    def make_move(self, action) -> bool:
        if self.board[action] == 0:
            self.board[action] = self.current_player
            done, winner = self.check_winner()
            self.render()
            self.current_player = -self.current_player
            
            return done, "Player 1 wins!" if winner == 1 else "Player 2 wins!" if winner == -1 else "Draw!" if winner == 0 else None
        return False, None

    def check_winner(self) -> bool:
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player) or np.all(self.board[:, i] == self.current_player):
                print(f"Player {1 if self.current_player == 1 else 2} wins!")
                return True, 1 if self.current_player == 1 else -1
        
        if np.all(np.diag(self.board) == self.current_player) or np.all(np.diag(np.fliplr(self.board)) == self.current_player):
            print(f"Player {1 if self.current_player == 1 else 2} wins!")
            return True, 1 if self.current_player == 1 else -1
        
        if not np.any(self.board == 0):
            print("It's a draw!")
            return True, 0
        
        return False, None

    def render(self) -> None:
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

    def close_pygame(self) -> None:
        pygame.quit()

class QLearningAgent:
    def __init__(self, player: int, q_table: dict) -> None:
        self.q_table = q_table
        self.player = player
        self.actions_taken = ""
    
    def get_state(self, board: np.ndarray) -> tuple:
        return tuple(map(tuple, board))
    
    def choose_action(self, board: np.ndarray, available_actions: list) -> tuple:
        q_values = [self.q_table[(self.get_state(board), action)] for action in available_actions]
        max_q = max(q_values)
        chosen_action = random.choice([a for a, q in zip(available_actions, q_values) if q == max_q])
        
        self.actions_taken += f"""\nGame State: \n{board}\n"""
        self.actions_taken += f"""Available Actions: \n"""
        for q_value in q_values:
            self.actions_taken += f"\t{q_value}\n"
        self.actions_taken += f"""Chosen Action: \n\t{max_q}\n"""
        
        print(f"\nPlayer {1 if self.player == 1 else 2} Q-values: {q_values}")
        print(f"\nPlayer {1 if self.player == 1 else 2} chooses action: {chosen_action} \nwith Q-value: {max_q}\n")
        
        return chosen_action
    
    def save_actions_taken(self, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(str(self.actions_taken))

def load_q_table(filename: str) -> dict:
    with open(filename, 'rb') as f:
        q_table = pickle.load(f)
    
    return defaultdict(lambda: 0, q_table)

def user_move(available_actions: list) -> tuple:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // 100, x // 100
                if (row, col) in available_actions:
                    return (row, col)

def main() -> None:
    agent1_file = "Files/agent1_q_table.pkl"
    agent2_file = "Files/agent2_q_table.pkl"
    actions_taken_file = "Files/actions_taken.txt"
    
    env = TicTacToe()
    
    user_player = int(input("Choose player 1 (X) or player 2 (O): "))
    if user_player == 1:
        user_player = 1
    else:
        user_player = -1
    
    agent_player = -user_player
    agent_q_table_file = agent1_file if agent_player == 1 else agent2_file
    
    q_table = load_q_table(agent_q_table_file)
    agent = QLearningAgent(player=agent_player, q_table=q_table)
    
    while True:
        print("Starting new game...")
        state = env.reset()
        done = False
        agent.actions_taken += "Game Start: \n"
        
        while not done:
            if env.current_player == user_player:
                available_actions = env.available_actions()
                action = user_move(available_actions)
            else:
                available_actions = env.available_actions()
                action = agent.choose_action(state, available_actions)
            
            print(env.board)
            
            done, game_result = env.make_move(action)

            if done:
                print()
                time.sleep(2)
        
        agent.actions_taken += f"Game End: {game_result}\n\n\n"
        agent.save_actions_taken(actions_taken_file)

if __name__ == "__main__":
    main()