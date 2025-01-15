#!/usr/bin/python3
import random
import os

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):

        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.non_mine_cells = width * height - len(self.mines)  # Total non-mine cells
        self.revealed_cells = 0
    def display_board(self, reveal_all=False):

        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal_all or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_adjacent_mines(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_adjacent_mines(self, x, y):

        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal_cell(self, x, y):

        if (y * self.width + x) in self.mines:
            return False

        if not self.revealed[y][x]:
            self.revealed[y][x] = True
            self.revealed_cells += 1

            if self.revealed_cells == self.non_mine_cells:
                return "win"

        if self.count_adjacent_mines(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal_cell(nx, ny)
        return True

    def play(self):

        while True:
            self.display_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                result = self.reveal_cell(x, y)
                if result == False:
                    self.display_board(reveal_all=True)
                    print("Game Over! You hit a mine.")
                    break
                elif result == "win":
                    self.display_board(reveal_all=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
