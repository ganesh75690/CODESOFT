import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.human_player = 'X'
        self.ai_player = 'O'

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position, player):
        self.board[position] = player

    def is_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner(self.human_player) or self.is_winner(self.ai_player) or self.is_board_full()

    def minimax(self, depth, maximizing_player):
        if self.is_winner(self.human_player):
            return -1
        elif self.is_winner(self.ai_player):
            return 1
        elif self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for move in self.available_moves():
                self.make_move(move, self.ai_player)
                eval = self.minimax(depth + 1, False)
                self.make_move(move, ' ')
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for move in self.available_moves():
                self.make_move(move, self.human_player)
                eval = self.minimax(depth + 1, True)
                self.make_move(move, ' ')
                min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self):
        best_move = -1
        best_eval = -math.inf
        for move in self.available_moves():
            self.make_move(move, self.ai_player)
            eval = self.minimax(0, False)
            self.make_move(move, ' ')

            if eval > best_eval:
                best_eval = eval
                best_move = move

        return best_move

def main():
    game = TicTacToe()

    while not game.is_game_over():
        game.display_board()
        human_move = int(input("Enter your move (0-8): "))
        if human_move not in game.available_moves():
            print("Invalid move. Try again.")
            continue
        game.make_move(human_move, game.human_player)

        if game.is_game_over():
            break

        ai_move = game.get_best_move()
        print(f"\nAI plays {ai_move}")
        game.make_move(ai_move, game.ai_player)

    game.display_board()

    if game.is_winner(game.human_player):
        print("You win!")
    elif game.is_winner(game.ai_player):
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
