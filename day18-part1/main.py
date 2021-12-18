import json
import os
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime

debug = False


def main():
    with open("input0.txt", encoding="utf-8") as f:
        hw = [json.loads(x) for x in f.readlines()]

    print(hw)
    print(len(hw))


if __name__ == "__main__":
    main()
