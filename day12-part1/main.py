from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

DEBUG = False
PART2 = False


@dataclass
class Cave:
    name: str
    is_big_cave: bool


def find_all_paths(graph: Dict[str, List[Cave]], start: str) -> None:
    visited_list = []

    def dfs(graph: Dict[str, List[Cave]], current_vertex: str, visited: List[str]):
        visited.append(current_vertex)
        for vertex in graph[current_vertex]:
            if vertex.name not in visited or vertex.is_big_cave:
                dfs(graph, vertex.name, visited.copy())
        if visited[0] == "start" and visited[-1] == "end":
            visited_list.append(visited)

    dfs(graph, start, [])

    if DEBUG:
        print(visited_list)
    print(len(visited_list))


def is_big_cave(name: str) -> bool:
    return all([x.isupper() for x in name])


def main():
    graph = defaultdict(list)
    with open("input.txt", encoding="utf-8") as f:
        for line in f.readlines():
            line_split = line.strip().split("-")

            graph[line_split[0]].append(Cave(line_split[1], is_big_cave(line_split[1])))
            graph[line_split[1]].append(Cave(line_split[0], is_big_cave(line_split[0])))

    if DEBUG:
        print(graph)

    find_all_paths(graph, "start")


if __name__ == "__main__":
    main()
