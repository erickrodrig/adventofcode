# code can be reduced into smaller fucntions 

def solution_p1(matrix: list[list[str]]) -> int:
  symbols = ['@', '#', '$', '%', '&', '*', '+', '-', '/', '=']
  total = 0

  for i, line in enumerate(matrix):
    for j, col in enumerate(line):
      if col in symbols:
        # left
        if j - 1 >= 0 and line[j - 1].isdigit():
          value = run_through(j - 1, i, matrix)
          if value:
            total += int(value)
        # right
        if j + 1 <= len(line) and line[j + 1].isdigit():
          value = run_through(j + 1, i, matrix, 'r')
          if value:
            total += int(value)

        # check up
        if i - 1 >= 0:
          check_up_corners = True

          # up straight
          if matrix[i - 1][j].isdigit():      
            value_up_left = ''
            value_up_right = ''
            if j - 1 >= 0:
              value_up_left = run_through(j - 1, i - 1, matrix)
            if j + 1 <= len(matrix[i - 1]):
              value_up_right = run_through(j + 1, i - 1, matrix, 'r')
            total += int(value_up_left + matrix[i - 1][j] + value_up_right)
            matrix[i - 1][j] = '.'
            check_up_corners = False

          # up left
          if j - 1 >= 0 and matrix[i - 1][j - 1].isdigit() and check_up_corners:
            value = run_through(j - 1, i - 1, matrix)
            if value:
              total += int(value)
          # up right
          if j + 1 <= len(matrix[i - 1]) and matrix[i - 1][j + 1].isdigit() and check_up_corners:
            total += int(run_through(j + 1, i - 1, matrix, 'r'))

        # check down
        if i + 1 <= len(matrix):
          check_down_corners = True

          # down straight
          if matrix[i + 1][j].isdigit():
            value_down =  matrix[i + 1][j]
            matrix[i + 1][j] = '.'
            value_down_left = ''
            value_down_right = ''
            if j - 1 >= 0:
              value_down_left = run_through(j - 1, i + 1, matrix)
            if j + 1 <= len(matrix[i + 1]):
              value_down_right = run_through(j + 1, i + 1, matrix, 'r')
            total += int(value_down_left + value_down + value_down_right)
            check_down_corners = False
          
          # down left
          if j - 1 >= 0 and matrix[i + 1][j - 1].isdigit() and check_down_corners:
            value = run_through(j - 1, i + 1, matrix)
            if value:
              total += int(value)
          # down right
          if j + 1 <= len(matrix[i + 1]) and matrix[i + 1][j + 1].isdigit() and check_down_corners:
            value = run_through(j + 1, i + 1, matrix, 'r')
            if value:
              total += int(value)
  # with open(Path(__file__).parent.joinpath('output_p1.txt'), 'w') as file:
  #   for row in matrix:
  #       file.write(''.join(row) + '\n')
  return total

def solution_p2(matrix: list[list[str]]) -> int:
  total = 0

  for i, line in enumerate(matrix):
    for j, col in enumerate(line):
      if col == '*':
        part_nums = []
        # left
        if j - 1 >= 0 and line[j - 1].isdigit():
          value = run_through(j - 1, i, matrix)
          if value:
            part_nums.append(int(value))
        # right
        if j + 1 <= len(line) and line[j + 1].isdigit():
          value = run_through(j + 1, i, matrix, 'r')
          if value:
            part_nums.append(int(value))

        # check up
        if i - 1 >= 0:
          check_up_corners = True

          # up straight
          if matrix[i - 1][j].isdigit():  
            value_up_left = ''
            value_up_right = ''
            if j - 1 >= 0:
              value_up_left = run_through(j - 1, i - 1, matrix)
            if j + 1 <= len(matrix[i - 1]):
              value_up_right = run_through(j + 1, i - 1, matrix, 'r')
            part_nums.append(int(value_up_left + matrix[i - 1][j] + value_up_right))
            matrix[i - 1][j] = '.'
            check_up_corners = False

          # up left
          if j - 1 >= 0 and matrix[i - 1][j - 1].isdigit() and check_up_corners:
            value = run_through(j - 1, i - 1, matrix)
            if value:
              part_nums.append(int(value))
          # up right
          if j + 1 <= len(matrix[i - 1]) and matrix[i - 1][j + 1].isdigit() and check_up_corners:
            value = run_through(j + 1, i - 1, matrix, 'r')
            if value:
              part_nums.append(int(value))

        # check down
        if i + 1 <= len(matrix):
          check_down_corners = True

          # down straight
          if matrix[i + 1][j].isdigit():
            value_down =  matrix[i + 1][j]
            matrix[i + 1][j] = '.'
            value_down_left = ''
            value_down_right = ''
            if j - 1 >= 0:
              value_down_left = run_through(j - 1, i + 1, matrix)
            if j + 1 <= len(matrix[i + 1]):
              value_down_right = run_through(j + 1, i + 1, matrix, 'r')
            part_nums.append(int(value_down_left + value_down + value_down_right))
            check_down_corners = False
          
          # down left
          if j - 1 >= 0 and matrix[i + 1][j - 1].isdigit() and check_down_corners:
            value = run_through(j - 1, i + 1, matrix)
            if value:
              part_nums.append(int(value))
          # down right
          if j + 1 <= len(matrix[i + 1]) and matrix[i + 1][j + 1].isdigit() and check_down_corners:
            value = run_through(j + 1, i + 1, matrix, 'r')
            if value:
              part_nums.append(int(value))
        
        if len(part_nums) == 2:
          total += part_nums[0] * part_nums[1]
  # with open(Path(__file__).parent.joinpath('output_p2.txt'), 'w') as file:
  #   for row in matrix:
  #       file.write(''.join(row) + '\n')
  return total

def run_through(start: int, line_index: int, matrix: list[list[str]], direction: str = '') -> str:
  stop = len(matrix[line_index]) if direction == 'r' else -1
  step = 1 if direction == 'r' else -1
  number = ''
  for i in range(start, stop, step):
    if matrix[line_index][i].isdigit():
      if direction == 'r':
        number += matrix[line_index][i]
      else:
        number = matrix[line_index][i] + number
      matrix[line_index][i] = '.'
    else:
      break
  return number

if __name__ == "__main__":
  from pathlib import Path

  def read_matrix_from_file() -> list[list[str]]:
    with open(Path(__file__).parent.joinpath('input.txt'), 'r') as file:
      return [list(line.strip()) for line in file]
  
  print(solution_p1(read_matrix_from_file()))
  print(solution_p2(read_matrix_from_file()))