import os
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime

debug = False


def simulate(args):
    x_vel, y_vel, landing_zone = args
    x_pos = 0
    y_pos = 0

    max_x = max(landing_zone[0])
    max_y = min(landing_zone[1])

    max_y_val = -99999999
    while (x_pos <= max_x) and (y_pos >= max_y):
        x_pos = x_pos + x_vel
        y_pos = y_pos + y_vel

        if x_vel > 0:
            x_vel -= 1
        if x_vel < 0:
            x_vel += 1

        y_vel -= 1

        if y_pos > max_y_val:
            max_y_val = y_pos

        if debug:
            print(x_pos, y_pos)

        if landing_zone[0][0] <= x_pos <= landing_zone[0][1] and landing_zone[1][0] <= y_pos <= landing_zone[1][1]:
            return max_y_val

    return None


def main():
    start = datetime.now()
    with open("input.txt", encoding="utf-8") as f:
        landing_zone = [[int(y) for y in x[2:].split("..")] for x in
                        f.read().strip().replace("target area: ", "").split(", ")]

    print(f"Landing zone: {landing_zone}")

    print(f"Part 1 Using formula: {min(landing_zone[1]) * (min(landing_zone[1]) + 1) // 2}")

    x1 = -250
    x2 = 250
    y1 = -250
    y2 = 250

    possible_vals = [(x, y, landing_zone) for x in range(x1, x2) for y in
                     range(y1, y2)]

    with ProcessPoolExecutor() as executor:
        succ_vals = [x for x in executor.map(simulate, possible_vals) if x is not None]


    if debug:
        print(succ_vals)
    if succ_vals:
        print(f"Part 1: {max(succ_vals)}")
        print(f"Part 2: Total possible velocities: {len(succ_vals)}")
    print(f"Duration: {datetime.now() - start}")

if __name__ == "__main__":
    main()
