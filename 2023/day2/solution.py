def read_input_file(path: str) -> list[str]:
    with open(path, "r") as file:
        return [line.strip("\n") for line in file]


def solution_p1(document: list[str]) -> int:
    sum = 0

    red_max = 12
    green_max = 13
    blue_max = 14

    for i, line in enumerate(document):
        games_possible = True
        games = line.split(";")

        for cube_set in games:
            red = get_cubes_number("red", cube_set)
            green = get_cubes_number("green", cube_set)
            blue = get_cubes_number("blue", cube_set)

            if red > red_max or green > green_max or blue > blue_max:
                games_possible = False

        if games_possible:
            sum += i + 1  # or line.split(':')[0][-1]
    return sum


def get_cubes_number(color: str, cube_set: str) -> int:
    number = cube_set.split(f" {color}")[0][-2:].replace(" ", "")
    return int(number) if number.isdigit() else 0


def solution_p2(document: list[str]) -> int:
    sum = 0

    for line in document:
        games = line.split(";")

        red_cubes = []
        green_cubes = []
        blue_cubes = []

        for cube_set in games:
            red_cubes.append(get_cubes_number("red", cube_set))
            green_cubes.append(get_cubes_number("green", cube_set))
            blue_cubes.append(get_cubes_number("blue", cube_set))

        sum += max(red_cubes) * max(green_cubes) * max(blue_cubes)
    return sum


if __name__ == "__main__":
    from pathlib import Path

    document = read_input_file(Path(__file__).parent.joinpath("input.txt"))

    print(solution_p1(document))
    print(solution_p2(document))
