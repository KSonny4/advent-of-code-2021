def main():
    with open("input.txt", encoding="utf-8") as f:
        lanternfishes = map(int, f.read().split(","))

    counter = 0
    while counter != 80:
        new_fish_list = []
        for fish in lanternfishes:
            if fish == 0:
                new_fish_list.append(6)  # fish gave birth
                new_fish_list.append(8)  # baby
            else:
                new_fish_list.append(fish - 1)
        lanternfishes = new_fish_list
        counter += 1

    print(len(lanternfishes))


if __name__ == "__main__":
    main()
