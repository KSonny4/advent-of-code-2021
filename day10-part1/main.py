from typing import Optional


def check(string: str) -> Optional[str]:
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
    return None


def main():
    price = {
        "{": 1197,
        "[": 57,
        "(": 3,
        "<": 25137,
        "}": 1197,
        "]": 57,
        ")": 3,
        ">": 25137,
    }

    with open("input.txt", encoding="utf-8") as f:
        data = [x.strip() for x in f.readlines()]

    total = 0
    for string in data:
        result = check(string)
        if result:
            total += price[result]
    print(total)


if __name__ == "__main__":
    main()
