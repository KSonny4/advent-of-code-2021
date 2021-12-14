from collections import Counter

def main():
    with open("input.txt", encoding="utf-8") as f:
        string, mappings = f.read().split("\n\n")

    mappings = dict([line.strip().split(" -> ") for line in mappings.split("\n")])

    counts = {}
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1

    string_set = Counter(string[n:n+2] for n in range(len(string)) if len(string[n:n+2]) == 2 )

    iteration = 40
    for _ in range(1, iteration + 1):

        new_set = {}
        to_delete = {}
        for (left,right), count in string_set.items():

            letter = mappings.get(left+right)
            if not letter:
                continue

            # Create new pairs ( +1 to the pair)
            new_set[left + letter] = new_set.get(left + letter, 0) + count
            new_set[letter + right] = new_set.get(letter + right, 0) + count

            # Remove counter pairs (-1 to the pair)
            to_delete[left+right] = to_delete.get(left+right, 0) - count

            counts[letter] = counts.get(letter, 0) + count

        for k, v in new_set.items():
            string_set[k] = string_set.get(k, 0) + v

        for k, v in to_delete.items():
            string_set[k] = string_set.get(k, 0) + v

    vals = counts.values()
    print(counts)
    print(max(vals)-min(vals))

if __name__ == "__main__":
    main()