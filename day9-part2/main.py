from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int
    val: int


def try_min(i, j, x, y, data) -> bool:
    len_i = len(data) - 1
    len_j = len(data[0]) - 1

    if (0 <= i + x <= len_i) and (0 <= j + y <= len_j):
        return data[i][j] < data[i + x][j + y]
    return True


def low_height(i, j, data) -> bool:
    a = try_min(i, j, 0, 1, data)
    b = try_min(i, j, 1, 0, data)
    c = try_min(i, j, 0, -1, data)
    d = try_min(i, j, -1, 0, data)
    return all([a, b, c, d])


def get_neighbours(
    i: int, j: int, data: List[List[int]], visited: List[Point]
) -> List[Point]:
    len_i = len(data) - 1
    len_j = len(data[0]) - 1
    neighbours = []
    a = [0, 1, 0, -1]
    b = [1, 0, -1, 0]
    for x, y in zip(a, b):
        new_i = i + x
        new_j = j + y
        if (0 <= new_i <= len_i) and (0 <= new_j <= len_j):
            if data[new_i][new_j] != 9:
                if not (new_i == 0 and new_j == 0):
                    if Point(new_i, new_j, data[new_i][new_j]) not in visited:
                        neighbours.append(Point(new_i, new_j, data[new_i][new_j]))
    return neighbours


def bfs_start(starting_point: Point, data: List[List[int]]) -> List[Point]:
    queue = []
    visited = []

    visited.append(starting_point)
    queue.append(starting_point)

    while queue:
        node = queue.pop(0)
        neighbours = get_neighbours(node.x, node.y, data, visited)
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited


def main():
    with open("input.txt", encoding="utf-8") as f:
        data = [[int(y) for y in x.strip()] for x in f.readlines()]

    low_points = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if low_height(i, j, data):
                low_points.append(Point(i, j, data[i][j]))

    basins = [bfs_start(low_point, data) for low_point in low_points]

    basins_sizes = sorted([len(basin) for basin in basins], reverse=True)
    print(basins_sizes[0] * basins_sizes[1] * basins_sizes[2])


if __name__ == "__main__":
    main()
