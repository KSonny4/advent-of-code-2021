from statistics import median


def main():
    with open("input.txt", encoding="utf-8") as f:
        data = list(map(int, f.read().split(",")))

    med = int(median(data))
    res = sum([abs(x - med) for x in data])
    print(res)


if __name__ == "__main__":
    main()
