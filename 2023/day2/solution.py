def read_input_file(path: str) -> list[str]:
  with open(path, 'r') as file:
    return [line.strip('\n') for line in file]

def solution_p1(document: list[str]) -> int:
  sum = 0

  red_max = 12
  green_max = 13
  blue_max = 14

  for i, line in enumerate(document):
    games_possible = True
    games = line.split(';')

    for cube_set in games:
      red = get_cubes_number('red', cube_set)
      green = get_cubes_number('green', cube_set)
      blue = get_cubes_number('blue', cube_set)

      # print(f'{red=}', f'{green=}', f'{blue=}')
      # print('-----')
      # met conditions
      if (red > red_max or 
          green > green_max or 
          blue > blue_max):
        games_possible = False;
    
    if games_possible:
      sum += i + 1 # or line.split(':')[0][-1]
  return sum

def get_cubes_number(color: str, cube_set: str) -> int:
  number = cube_set.split(f' {color}')[0][-2:].replace(' ', '')
  return int(number) if number.isdigit() else 0

def solution_p2(document: list[str]) -> int:
  sum = 0

  for line in document:
    games = line.split(';')

    red_cubes = []
    green_cubes = []
    blue_cubes = []

    for cube_set in games:
      red_cubes.append(get_cubes_number('red', cube_set))
      green_cubes.append(get_cubes_number('green', cube_set))
      blue_cubes.append(get_cubes_number('blue', cube_set))

    sum += max(red_cubes) * max(green_cubes) * max(blue_cubes)
  return sum

if __name__ == "__main__":
  from pathlib import Path
  document = read_input_file(Path(__file__).parent.joinpath('input.txt'))
  # answer = solution([
  #   'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
  #   'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
  #   'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
  #   'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
  #   'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
  # ])
  answer1 = solution_p1(document)
  print(answer1)

  answer2 = solution_p2(document)
  print(answer2)

  # game = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
  # games = game.split(';')

  # for g in games:
  #   red = g.split(' red')[0][-2:]
  #   green = g.split(' green')[0][-1]
  #   blue = g.split(' blue')[0][-1]

  #   red = int(red) if red.isdigit() else 0
  #   green = int(green) if green.isdigit() else 0
  #   blue = int(blue) if blue.isdigit() else 0

  #   if not (red > 12 and 
  #       green > 13 and 
  #       blue > 14):
      
  #     print('----')
  #     print(red)
  #     print(green)
  #     print(blue)
  #     print(g)
