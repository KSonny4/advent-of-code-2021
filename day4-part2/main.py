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


def check_boards(boards: List[List[List[Cell]]]) -> List[List[List[Cell]]]:
    winners = []
    for board in boards:
        # Check rows
        for row in board:
            if all([x.hit for x in row]):
                winners.append(board)

        for col in range(5):
            if all([board[row][col].hit for row in range(5)]):
                winners.append(board)
    return winners


def sum_board_unmarked(board: List[List[Cell]]) -> int:
    a = []
    for row in board:
        for cell in row:
            if not cell.hit:
                a.append(cell.num)
    return sum(a)


def play(
    numbers: List[int], boards: List[List[List[Cell]]]
) -> Tuple[int, List[List[Cell]]]:
    last_winner_board = None
    last_num = 0
    for num in numbers:
        tag_boards(num, boards)
        winners = check_boards(boards)
        print(last_num)
        if winners:
            print(f"num of winners: {len(winners)}")
            for w in winners:
                print(f"len boards: befor: {len(boards)}")
                # filter out winner board
                boards = [x for x in boards if x != w]
                print(f"len boards: after: {len(boards)}")

                last_winner_board = w
                last_num = num
    return last_num, last_winner_board


def main():
    with open("input.txt", encoding="utf-8") as f:
        numbers, boards = f.read().rstrip().split("\n\n")

    numbers = [int(num) for num in numbers.split(",")]
    boards = [[line.split() for line in board.split("\n")] for board in boards]

    # board[board_num][row][column]
    boards = [
        [[Cell(int(elt), False) for elt in line] for line in board] for board in boards
    ]

    last_number, winner_board = play(numbers, boards)

    # pprint(winner_number_board, winner_board)

    sum_umarked = sum_board_unmarked(winner_board)

    print(sum_umarked * last_number)


if __name__ == "__main__":
    main()
