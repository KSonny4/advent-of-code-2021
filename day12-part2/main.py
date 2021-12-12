from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

DEBUG = False
PART2 = False


@dataclass
class Cave:
    name: str
    is_big_cave: bool


def vertex_in_visited(
    vertex: Cave, visited: List[str], small_cave_that_we_can_visit_twice: str
) -> bool:
    if vertex.name == small_cave_that_we_can_visit_twice:
        num_of_visits = len([x for x in visited if x == vertex.name])
        return num_of_visits == 2

    return vertex.name in visited


def find_all_paths(
    graph: Dict[str, List[Cave]], start: str, small_cave_that_we_can_visit_twice: str
) -> List[List[str]]:
    visited_list = []

    def depthFirst(
        graph: Dict[str, List[Cave]], current_vertex: str, visited: List[str]
    ):
        visited.append(current_vertex)
        for vertex in graph[current_vertex]:
            # if vertex.name not in visited or vertex.is_big_cave:
            if (
                not vertex_in_visited(
                    vertex, visited, small_cave_that_we_can_visit_twice
                )
                or vertex.is_big_cave
            ):
                depthFirst(graph, vertex.name, visited.copy())
        if visited[0] == "start" and visited[-1] == "end":
            visited_list.append(visited)

    depthFirst(graph, start, [])

    if DEBUG:
        print(visited_list)

    return visited_list


def is_big_cave(name: str) -> bool:
    return all([x.isupper() for x in name])


def main():
    graph = defaultdict(list)
    small_caves = set()
    with open("input.txt", encoding="utf-8") as f:
        for line in f.readlines():

            line_split = line.strip().split("-")
            is_cave_0_big = is_big_cave(line_split[0])
            is_cave_1_big = is_big_cave(line_split[1])

            if line_split[0] not in ["start", "end"]:
                if not is_cave_0_big:
                    small_caves.add(line_split[0])
            if line_split[1] not in ["start", "end"]:
                if not is_cave_1_big:
                    small_caves.add(line_split[1])

            graph[line_split[0]].append(Cave(line_split[1], is_cave_1_big))
            graph[line_split[1]].append(Cave(line_split[0], is_cave_0_big))

    if DEBUG:
        print(graph)

    all_paths = set()
    for small_cave in small_caves:
        for path in find_all_paths(graph, "start", small_cave):
            all_paths.add(str(path))
    print(f"paths with 2 visits of caves: {len(all_paths)}")


if __name__ == "__main__":
    main()
