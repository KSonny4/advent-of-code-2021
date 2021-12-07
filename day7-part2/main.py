from functools import cache


@cache
def range_sum(stop: int) -> int:
    return sum(range(1, stop + 1))


def main():
    with open("input.txt", encoding="utf-8") as f:
        data = list(map(int, f.read().split(",")))

    best_res = float("inf")
    for i in range(min(data), max(data) + 1):
        res = sum([range_sum(abs(x - i)) for x in data])
        best_res = min(best_res, res)
    print(best_res)


if __name__ == "__main__":
    main()
