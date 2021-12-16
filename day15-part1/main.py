import sys
import heapq


def print_arr(d, i, j):
    string = ""
    for x in range(i):
        for y in range(j):
            try:
                # print(d[(x,y)], end='')
                string += str("X" if d[(x, y)] == sys.maxsize else d[(x, y)])
            except:
                # print(0, end='')
                string += "0"
        string += "\n"
    return string


def main():
    """
    This code is not nice, it keeps a log of debug which code!
    """
    with open("input0.txt", encoding="utf-8") as f:
        matrix = [[int(y) for y in x.strip()] for x in f.readlines()]
    end_x, end_y = len(matrix), len(matrix[0])

    positions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    risks = {(i, j): sys.maxsize for i in range(end_x) for j in range(end_y)}
    queue = [(0, (0, 0))]

    with open("log1.log", "w") as f:

        while queue:
            current_risk, position = heapq.heappop(queue)

            for x, y in positions:
                neighbor_position = (x + position[0], y + position[1])
                if neighbor_position in risks:
                    new_risk = (
                        current_risk
                        + matrix[neighbor_position[0]][neighbor_position[1]]
                    )
                    if new_risk < risks[neighbor_position]:
                        risks[neighbor_position] = new_risk
                        arr = print_arr(risks, end_x, end_y)
                        f.write("-----------------\n")
                        f.write(arr)
                        f.write("-----------------\n")
                        heapq.heappush(queue, (new_risk, neighbor_position))

    print(risks[(end_x - 1, -1)])


if __name__ == "__main__":
    main()
