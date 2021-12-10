from typing import Union, List

price = {
    "{": 3,
    "[": 2,
    "(": 1,
    "<": 4,
    "}": 3,
    "]": 2,
    ")": 1,
    ">": 4,
}


def get_total_score(result: str) -> int:
    total = 0
    for x in result:
        total *= 5
        total += price[x]
    return total


def check(string: str) -> Union[str, List[str]]:
    q = []
    vals = {
        "{": "}",
        "[": "]",
        "(": ")",
        "<": ">",
    }

    for s in string:
        if s in vals.keys():
            s_opposite = vals[s]
            q.insert(0, s_opposite)
        else:
            if s != q[0]:
                print(f"Expected {q[0]}, got {s}")
                return s
            q.pop(0)
    return q


def main():

    with open("input.txt", encoding="utf-8") as f:
        data = [x.strip() for x in f.readlines()]

    results = []
    for string in data:
        result = check(string)
        if isinstance(result, list):
            total = get_total_score(result)
            results.append(total)
    results = sorted(results)
    print(results[len(results) // 2])


if __name__ == "__main__":
    main()
