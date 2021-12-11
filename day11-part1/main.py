from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int
    val: int
    flashed: bool


def print_board(_round: int, data: List[List[Point]]) -> None:
    print(f"=====Round {_round}=======")
    for row in data:
        for cell in row:
            print(cell.val, end="")
        print()
    print(f"=====Round {_round}=======")


def update_neighbours(queue: List[Point], point: Point, data: List[List[Point]]) -> int:
    flashes = 0
    len_i = len(data) - 1
    len_j = len(data[0]) - 1

    point.flashed = True
    point.val = 0

    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for pos in positions:
        x, y = pos[0], pos[1]
        new_i = point.x + x
        new_j = point.y + y
        if (0 <= new_i <= len_i) and (0 <= new_j <= len_j):
            cell = data[new_i][new_j]

            if not cell.flashed:
                cell.val += 1

            if cell.val > 9 and cell not in queue:
                cell.val = 0
                queue.append(cell)
                flashes += 1

    return flashes


def check_all_flash(data: List[List[Point]]) -> bool:
    first = data[0][0].val
    for row in data:
        for cell in row:
            if cell.val != first:
                return False
    return True


def main():
    debug = False
    part2 = True
    rounds = 9999999 if part2 else 100
    flashes = 0

    with open("input.txt", encoding="utf-8") as f:
        data = [
            [Point(x_pos, y_pos, int(y), False) for y_pos, y in enumerate(x.strip())]
            for x_pos, x in enumerate(f.readlines())
        ]

    for _round in range(1, rounds + 1):

        flashing_queue = []

        for row in data:
            for cell in row:
                cell.val += 1
                if cell.val == 10:
                    cell.val = 0
                    flashing_queue.append(cell)
                    flashes += 1

        while len(flashing_queue):
            cell = flashing_queue.pop()
            flashes += update_neighbours(flashing_queue, cell, data)

        if part2:
            sync = check_all_flash(data)

            if sync:
                print(f"PART2: flash in sync in round: {_round}")
                return

        for row in data:
            for cell in row:
                cell.flashed = False

        if debug:
            print_board(_round, data)

    print(f"PART1: flashes count: {flashes}")


if __name__ == "__main__":
    main()
