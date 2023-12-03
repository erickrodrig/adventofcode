def read_input_file(path: str) -> list[str]:
  with open(path, 'r') as file:
    return [line.strip('\n') for line in file]

def solution_p1(document: list[str]) -> int:
  sum = 0
  
  for line in document:
    remaining = [char for char in line if char.isdigit()]
    sum += int(remaining[0] + remaining[-1])
  return sum

def solution_p2(document: list[str]) -> int:
  sum = 0

  num_keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
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
  document = read_input_file(Path(__file__).parent.joinpath('input.txt'))
  answer1 = solution_p1(document)
  answer2 = solution_p2(document)

  print(answer1)
  print(answer2)

  # test

  # for i, char in enumerate(linha):
  #   l = linha[i:]
  #     if l.startswith(number):
  #       linha = linha.replace(number, str(num_values[number]))
  #     print(linha)
  # print(linha)
    

    
    # if num in linha:
    #   found_nums = found_nums + [num]
  
  # for num in found_nums:
  #   linha_split = linha.split(num)
  #   print(linha_split)
  #   print(linha_split[0] + str(numbers[num]) + linha_split[-1])
      # split = linha.rsplit(num)
      # print(linha.split(num))
      # print(linha.rsplit(num))
      # linha = split[0] + str(numbers[num]) + split[-1]
      # print(linha)
  # print(found_nums)
  # linha_split = linha.split(found_nums[0])
  # print(linha_split[0] + str(numbers[num]) + linha_split[-1])
      # print(split[0] + str(numbers[num]) + split[-1])
  # print(linha)