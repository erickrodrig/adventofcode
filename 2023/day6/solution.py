def solution_p1(lines: list[str]) -> int:
    ways = 1

    t_list = map(int, lines[0].split()[1:])
    d_list = map(int, lines[1].split()[1:])

    for t, d in list(zip(t_list, d_list)):
        curr_ways = 0

        for hold_t in range(0, t + 1):
            speed = hold_t
            traveled_d = (t - hold_t) * speed

            if traveled_d > d:
                curr_ways += 1

        ways *= curr_ways

    return ways


def solution_p2(lines: list[str]) -> int:
    ways = 1

    t = int("".join(lines[0].split(":")[1].split()))
    d = int("".join(lines[1].split(":")[1].split()))

    curr_ways = 0

    for hold_t in range(0, t + 1):
        speed = hold_t
        traveled_d = (t - hold_t) * speed

        if traveled_d > d:
            curr_ways += 1

    ways *= curr_ways

    return ways


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent.joinpath("input.txt"), "r") as file:
        lines = [line.strip() for line in file]

    print(solution_p1(lines))
    print(solution_p2(lines))
