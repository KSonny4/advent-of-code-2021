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


def main():
    with open("input.txt", encoding="utf-8") as f:
        data = [[int(y) for y in x.strip()] for x in f.readlines()]

    vals = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if low_height(i, j, data):
                vals.append(col)
    print(sum([x + 1 for x in vals]))


if __name__ == "__main__":
    main()
