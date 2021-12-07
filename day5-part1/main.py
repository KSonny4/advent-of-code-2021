from collections import defaultdict
from dataclasses import dataclass
from typing import Generator


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
        if self.start.x != self.end.x:
            raise Exception(
                f"Error when accesing attribute x for {self}."
                " You want to access this method only if self.start.x != self.end.x."
            )
        return self.start.x

    @property
    def y(self) -> int:
        # use this to easily acccess y when they are same
        if self.start.y != self.end.y:
            raise Exception(
                f"Error when accesing attribute y for {self}."
                " You want to access this method only if self.start.y != self.end.y"
            )
        return self.start.y

    def y_range(self) -> Generator[int, None, None]:
        y1 = self.start.y
        y2 = self.end.y
        return range(min(y1, y2), max(y1, y2) + 1)

    def x_range(self) -> Generator[int, None, None]:
        x1 = self.start.x
        x2 = self.end.x
        return range(min(x1, x2), max(x1, x2) + 1)

    @property
    def is_same_x_coord(self) -> bool:
        return self.start.x == self.end.x

    @property
    def is_same_y_coord(self) -> bool:
        return self.start.y == self.end.y

    @property
    def is_same_x_or_y_coord(self) -> bool:
        return self.is_same_x_coord or self.is_same_y_coord


def main():
    with open("input1.txt", encoding="utf-8") as f:
        raw_input = [x.strip().split(" -> ") for x in f.readlines()]
    data = [[map(int, y.split(",")) for y in x] for x in raw_input]

    pipes = [Pipe(start=Coordinates(*x[0]), end=Coordinates(*x[1])) for x in data]

    filtered_pipes = [x for x in pipes if x.is_same_x_or_y_coord]

    crosses = defaultdict(dict)

    # Layout where pipe lays in grid
    for pipe in filtered_pipes:
        if pipe.is_same_x_coord:
            for y_pos in pipe.y_range():
                crosses[pipe.x][y_pos] = crosses.get(pipe.x, {}).get(y_pos, 0) + 1
        if pipe.is_same_y_coord:
            for x_pos in pipe.x_range():
                crosses[x_pos][pipe.y] = crosses.get(x_pos, {}).get(pipe.y, 0) + 1

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
