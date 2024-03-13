import argparse
import sys
from pathlib import Path
import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("day_number", help="Day number")
    parser.add_argument("-y", "--year", help="Year")

    args = parser.parse_args()

    year = args.year
    if args.year is None:
        year = datetime.datetime.now().year

    path = Path.cwd().joinpath(str(year), str(args.day_number))
    path.mkdir(exist_ok=True, parents=True)

    for f_name in ["input.txt", "solution.py", "statement.md"]:
        with open(path.joinpath(f_name), "w") as f:
            pass


if __name__ == "__main__":
    main()
