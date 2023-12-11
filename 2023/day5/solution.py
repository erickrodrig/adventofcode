def solution_p1(lines: list[str]) -> int:
  # seeds as initial value
  source_values = list(map(int, lines[0].split(':')[1].split()))

  maps_attribs = {}
  key = None
  
  for line in lines[1:]:
    if not line:
      continue

    if line.endswith('map:'):
      key = line.split(' map')[0]
      maps_attribs[key] = []
      continue

    d, s, l = map(int, line.split())

    diff = s - d
    source_range = range(s, s+ l)

    maps_attribs[key].append((diff, source_range))

  for i, _ in enumerate(source_values):
    for map_values in maps_attribs.values():
      for diff, source_range in map_values:
        if source_values[i] in source_range:
          source_values[i] = source_values[i] - diff
          break
  return min(source_values)


def solution_p2(lines: list[str]) -> int:
  seeds = list(map(int, lines[0].split(':')[1].split()))

  source_values = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

  maps_attribs = {}
  key = None
  
  for line in lines[1:]:
    if not line:
      continue

    if line.endswith('map:'):
      key = line.split(' map')[0]
      maps_attribs[key] = []
      continue

    d, s, l = map(int, line.split())
    diff = s - d
    source_range = (s, s + l)

    maps_attribs[key].append((diff, source_range))

  # inverts first approach loop sequence to update source values
  for map_values in maps_attribs.values():
    new_source_values = []
    for src_start, src_end in source_values[:]:
      overlap = False

      # checks for overlap
      for diff, (range_start, range_end) in map_values:
        last_start = max(src_start, range_start)
        first_end = min(src_end, range_end)

        if first_end > last_start:
          new_source_values.append((last_start - diff, first_end - diff))

          # add back remaining gaps
          if src_start < range_start:
            new_source_values.append((src_start, range_start))
          if src_end > range_end:
            new_source_values.append((range_end, src_end))
          overlap = True
          break
      
      if not overlap:
        new_source_values.append((src_start, src_end))
      
    source_values = new_source_values
  return min(min(source_values))

if __name__ == "__main__":
  from pathlib import Path
  with open(Path(__file__).parent.joinpath('input.txt'), 'r') as file:
    lines = [line.strip() for line in file]

  print(solution_p1(lines))
  print(solution_p2(lines))
