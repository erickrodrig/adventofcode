def read_input_file(path: str) -> list[str]:
    with open(path, "r") as file:
        return [line.strip("\n") for line in file]


def solution_p1(document: list[str]) -> int:
    sum = 0

    for line in document:
        remaining = [char for char in line if char.isdigit()]
        sum += int(remaining[0] + remaining[-1])
    return sum


def solution_p2(document: list[str]) -> int:
    sum = 0

    num_keys = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_values = dict(zip(num_keys, range(1, 10)))

    for line in document:
        remaining = []
        for i, char in enumerate(line):
            if char.isdigit():
                remaining.append(char)
            for number in num_keys:
                if line[i:].startswith(number):
                    remaining.append(str(num_values[number]))
        sum += int(remaining[0] + remaining[-1])
    return sum


if __name__ == "__main__":
    from pathlib import Path

    document = read_input_file(Path(__file__).parent.joinpath("input.txt"))

    print(solution_p1(document))
    print(solution_p2(document))
