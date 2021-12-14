import numpy as np

PART1 = True


def fold_by_x(arr: np.array, loc: int) -> np.array:
    first = np.flipud(arr[(loc + 1) :, :])
    arr[(2 * loc - len(arr) + 1) : loc, :] += first
    arr = arr[:loc, :]
    return arr


def fold_by_y(arr: np.array, loc: int) -> np.array:
    first = np.fliplr(arr[:, (loc + 1) :])
    arr[:, (2 * loc - len(arr[0]) + 1) : loc] += first
    return arr[:, :loc]


def main():
    coords = []
    with open("input_hofy.txt", encoding="utf-8") as f:
        coordinates, folding = f.read().split("\n\n")

    for line in coordinates.split():
        line_split = list(map(int, line.strip().split(",")))
        coords.append(tuple(line_split))

    max_x = max([x[0] for x in coords])
    max_y = max([x[1] for x in coords])

    arr = np.zeros((max_x + 1, max_y + 1))

    for coordinate in coords:
        arr[coordinate] = 1

    print(arr)

    folding = [x.split()[-1].split("=") for x in folding.split("\n")]
    for command in folding:
        fold_row = int(command[1])
        if command[0] == "x":
            arr = fold_by_x(arr, fold_row)
        elif command[0] == "y":
            arr = fold_by_y(arr, fold_row)
        else:
            raise Exception("Unknown command.")

        if PART1:
            print(np.count_nonzero(arr))
            return

    arr[arr > 0] = 77  # Convert all vals > 0 to some more visible num
    arr = np.transpose(arr)  # Transpose so we can print it
    print(arr)
    letters = np.hsplit(arr, 8)
    for letter in letters:
        print(letter)
        print()
    return


if __name__ == "__main__":
    main()
