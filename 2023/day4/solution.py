def solution_p1(lines: list[str]) -> int:
  total = 0

  for line in lines:
    win_nums, my_nums = line.split('|')
    win_nums = win_nums.split(':')[1].split()
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
    win_nums, my_nums = line.split('|')
    win_nums = win_nums.split(':')[1].split()
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
  with open(Path(__file__).parent.joinpath('input.txt'), 'r') as file:
    lines = [line.strip() for line in file]
  
  # lines = [
  #   'Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53',
  #   'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
  #   'Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1',
  #   'Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83',
  #   'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
  #   'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
  # ]
  print(solution_p1(lines))
  print(solution_p2(lines))
