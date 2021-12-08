from typing import Dict, Iterable, List

len_to_number = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}


def sort_string(string: str) -> str:
    return "".join(sorted(string))


def filter_out_assigned_letter_values(
    data: List[str], vals_to_filter: Iterable[str]
) -> List[str]:
    return [
        x
        for x in data
        if not sort_string(x) in [sort_string(y) for y in vals_to_filter]
    ]


def get_mapping(data: List[str]) -> Dict[str, str]:
    # Return mapping sorted_value to number

    # get 1,4,7,8 digits, thats easy as we already know which numbers these are
    string_to_int_mapping = {
        x: len_to_number[len(x)] for x in data if len(x) in len_to_number.keys()
    }
    data = filter_out_assigned_letter_values(data, string_to_int_mapping.keys())

    # get 9, it has len == 6, and 4 and 7 digit are subset of 9 digit
    numbers_len_6 = [y for y in [x for x in data if len(x) == 6]]
    int_to_string_mapping = {v: k for k, v in string_to_int_mapping.items()}

    num_4 = {*int_to_string_mapping[4]}
    num_7 = {*int_to_string_mapping[7]}

    for possible_9_val in numbers_len_6:
        poss_9 = {*possible_9_val}
        diff4 = num_4.difference(poss_9)
        diff7 = num_7.difference(poss_9)
        if len(diff4) == 0 and len(diff7) == 0:
            int_to_string_mapping |= {9: possible_9_val}
            numbers_len_6 = filter_out_assigned_letter_values(
                numbers_len_6, [possible_9_val]
            )
            data = filter_out_assigned_letter_values(data, [possible_9_val])
            break

    # Get 0, 7 is subset of it and it has len(6)
    for possible_0_val in numbers_len_6:
        poss_0 = {*possible_0_val}
        diff7 = num_7.difference(poss_0)
        if len(diff7) == 0:
            int_to_string_mapping |= {0: possible_0_val}
            data = filter_out_assigned_letter_values(data, [possible_0_val])
            numbers_len_6 = filter_out_assigned_letter_values(
                numbers_len_6, [possible_0_val]
            )
            break

    # 6, last number with len(6)
    int_to_string_mapping |= {6: numbers_len_6[0]}
    data = filter_out_assigned_letter_values(data, [numbers_len_6[0]])

    # 3, 1 is subset of 3
    num_1 = {*int_to_string_mapping[1]}
    for possible_3_val in data:
        poss_3 = {*possible_3_val}
        diff1 = num_1.difference(poss_3)
        if len(diff1) == 0:
            int_to_string_mapping |= {3: possible_3_val}
            data = filter_out_assigned_letter_values(data, [possible_3_val])
            break

    # 5, 5 is subset of 6
    num_6 = {*int_to_string_mapping[6]}
    for possible_5_val in data:
        poss_5 = {*possible_5_val}
        diff5 = poss_5.difference(num_6)
        if len(diff5) == 0:
            int_to_string_mapping |= {5: possible_5_val}
            data = filter_out_assigned_letter_values(data, [possible_5_val])
            break

    # Last value is 2
    int_to_string_mapping |= {2: data[0]}
    return {v: k for k, v in int_to_string_mapping.items()}


def main():
    with open("input.txt", encoding="utf-8") as f:
        data = [list(map(str.split, x.strip().split("|"))) for x in f.readlines()]

    vals = []
    for row in data:
        mapping = get_mapping([sort_string(x) for x in row[0]])
        num = int("".join([str(mapping[sort_string(x)]) for x in row[1]]))
        vals.append(num)
    print(sum(vals))


if __name__ == "__main__":
    main()
