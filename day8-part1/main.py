from statistics import median


def main():
    with open("input.txt", encoding="utf-8") as f:
        data = [x.strip().split("|")[1].split() for x in f.readlines()]
    print(data)

    lens = []
    for row in data:
        for measurrement in row:
            lens.append(len(measurrement))
    print(lens)
    a = lens.count(2)  # 1
    b = lens.count(4)  # 4
    c = lens.count(3)  # 7
    d = lens.count(7)  # 8
    print(a + b + c + d)


if __name__ == "__main__":
    main()
