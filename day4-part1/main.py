from dataclasses import dataclass
from typing import List, Tuple, Optional
from pprint import pprint

@dataclass
class Cell:
    num: int
    hit: bool


def tag_boards(num: int, boards: List[List[List[Cell]]]) -> None:
    for board in boards:
        for row in board:
            for cell in row:
                if cell.num == num:
                    cell.hit = True


def check_boards(boards: List[List[List[Cell]]]) -> Optional[List[List[Cell]]]:
    for num,board in enumerate(boards):
        # Check rows
        for row in board:
            if all([x.hit for x in row]):
                return board

        for col in range(5):
            if all([board[row][col].hit for row in range(5)]):
                return board
    return None

def sum_board_unmarked(board: List[List[Cell]]) -> int:
    a  = []
    for row in board:
      for cell in row:
        if not cell.hit:
          a.append(cell.num)
    return sum(a)
    

def play(numbers: List[int], boards: List[List[List[Cell]]]) -> Tuple[int, List[List[Cell]]]:
    for num in numbers:
        tag_boards(num, boards)
        winner_board = check_boards(boards)
        if winner_board:
            return num, winner_board


def main():
    with open("input.txt", encoding="utf-8") as f:
        numbers, *boards = f.read().rstrip().split("\n\n")

    numbers = [int(num) for num in numbers.split(",")]
    boards = [[line.split() for line in board.split("\n")] for board in boards]

    boards = [
        [[Cell(int(elt), False) for elt in line] for line in board] for board in boards
    ]

    last_number, winner_board = play(numbers, boards)

    sum_umarked = sum_board_unmarked(winner_board)

    print(sum_umarked*last_number)

if __name__ == "__main__":
    main()
