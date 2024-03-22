def solution_p1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        win_nums, my_nums = line.split("|")
        win_nums = win_nums.split(":")[1].split()
        matches = 0

        for num in my_nums.split():
            if num in win_nums:
                matches += 1

        if matches:
            n = 1
            for _ in range(matches - 1):
                n *= 2
            total += n
    return total


def solution_p2(lines: list[str]) -> int:
    total = 0
    cards = {}

    for i, line in enumerate(lines):
        win_nums, my_nums = line.split("|")
        win_nums = win_nums.split(":")[1].split()
        matches = 0

        cards.setdefault(i, 0)
        cards[i] += 1

        for num in my_nums.split():
            if num in win_nums:
                matches += 1

        for m in range(matches):
            cards.setdefault(m + i + 1, 0)
            cards[m + i + 1] += cards[i]
    total += sum(cards.values())
    return total


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent.joinpath("input.txt"), "r") as file:
        lines = [line.strip() for line in file]

    print(solution_p1(lines))
    print(solution_p2(lines))
