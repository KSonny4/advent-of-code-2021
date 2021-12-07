def main():
    fishes_growth = 9 * [0]

    with open("input.txt", encoding="utf-8") as f:
        lanternfishes = map(int, f.read().split(","))

    for lan in lanternfishes:
        fishes_growth[lan] += 1

    for i in range(256):
        growth_zero = fishes_growth[0]
        for i in range(len(fishes_growth) - 1):
            fishes_growth[i] = fishes_growth[i + 1]
        fishes_growth[6] = fishes_growth[6] + growth_zero
        fishes_growth[8] = growth_zero

    print(sum(fishes_growth))


if __name__ == "__main__":
    main()
