from collections import defaultdict
from dataclasses import dataclass
from typing import Generator, List, Tuple


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Pipe:
    start: Coordinates
    end: Coordinates

    @property
    def x(self) -> int:
        # use this to easily acccess x when they are same
        return self.start.x

    @property
    def y(self) -> int:
        # use this to easily acccess y when they are same
        return self.start.y

    def y_range(self) -> Generator[int, None, None]:
        y1 = self.start.y
        y2 = self.end.y
        return range(min(y1, y2), max(y1, y2) + 1)

    def x_range(self) -> Generator[int, None, None]:
        x1 = self.start.x
        x2 = self.end.x
        return range(min(x1, x2), max(x1, x2) + 1)

    def diag_same_range(self) -> Generator[int, None, None]:
        # Both x and y increases
        if self.start.x > self.end.x:
            return range(self.end.x, self.start.x + 1)
        if self.start.x < self.end.x:
            return range(self.start.x, self.end.x + 1)

    def diag_diff_range(self) -> Tuple[List[int], List[int]]:
        # Both x and y increases/decreases differently
        x1 = self.start.x
        x2 = self.end.x
        y1 = self.start.y
        y2 = self.end.y

        list1 = list(range(min(x1, x2), max(x1, x2) + 1))
        list2 = list(range(min(y1, y2), max(y1, y2) + 1))
        if x1 > x2:
            list1.reverse()

        if y1 > y2:
            list2.reverse()

        return list1, list2

    @property
    def is_diagonal_pipe_same_x_and_y(self) -> bool:
        return self.end.x == self.end.y and self.start.x == self.start.y

    @property
    def is_diagonal_pipe_different_x_and_y(self) -> bool:
        return self.start.x == self.end.y and self.end.x == self.start.y

    @property
    def is_same_x_coord(self) -> bool:
        return self.start.x == self.end.x

    @property
    def is_same_y_coord(self) -> bool:
        return self.start.y == self.end.y

    @property
    def is_same_x_or_y_coord(self) -> bool:
        return self.is_same_x_coord or self.is_same_y_coord

    @property
    def is_diagonal_pipe(self) -> bool:
        a = abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y)
        return a

    @property
    def is_proper_pipe(self) -> bool:
        return self.is_same_x_or_y_coord or self.is_diagonal_pipe


def main():

    with open("input1.txt", encoding="utf-8") as f:
        raw_input = [x.strip().split("->") for x in f.readlines()]
    data = [
        [list(map(int, y.split(","))) for y in list(map(str.strip, x))]
        for x in raw_input
    ]

    pipes = [Pipe(start=Coordinates(*x[0]), end=Coordinates(*x[1])) for x in data]

    filtered_pipes = [x for x in pipes if x.is_proper_pipe]

    crosses = defaultdict(dict)

    # Layout where pipe lays in grid
    for pipe in filtered_pipes:
        if pipe.is_same_x_coord:
            for y_pos in pipe.y_range():
                crosses[pipe.x][y_pos] = crosses.get(pipe.x, {}).get(y_pos, 0) + 1
        elif pipe.is_same_y_coord:
            for x_pos in pipe.x_range():
                crosses[x_pos][pipe.y] = crosses.get(x_pos, {}).get(pipe.y, 0) + 1
        elif pipe.is_diagonal_pipe_same_x_and_y:
            for n in pipe.diag_same_range():
                crosses[n][n] = crosses.get(n, {}).get(n, 0) + 1
        else:
            for n, m in zip(*pipe.diag_diff_range()):
                crosses[n][m] = crosses.get(n, {}).get(m, 0) + 1

    # filter out pipe hits > 2
    pipe_hits = [x.values() for x in crosses.values()]
    crossings = 0

    for pipe in pipe_hits:
        for hit in pipe:
            if hit > 1:
                crossings += 1
    print(crossings)


if __name__ == "__main__":
    main()
