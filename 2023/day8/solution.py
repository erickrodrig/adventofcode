from pathlib import Path

def node_list_to_hashmap(node_list: list[str]):
    m = {}
    for n in node_list:
        key, nodes = n.split(' = ')
        m[key] = tuple([nodes[1:4], nodes[6:9]])
    return m

def solution_p1(instructions: str, node_list: list[str]) -> int:
    steps = 0

    node_map = node_list_to_hashmap(node_list)

    initial_element = 'AAA'
    last_element = 'ZZZ'
    last_element_found = False

    dirs = {'L': 0, 'R': 1}

    previous_element = initial_element

    while not last_element_found:
        for i in instructions:
            steps += 1

            next_element = node_map[previous_element][dirs[i]]

            if next_element == last_element:
                last_element_found = True
                break
            previous_element = next_element
    return steps


# doesnt work. couldnt do it. need lcm.
def solution_p2(instructions: str, node_list: list[str]) -> int:
    steps = 0

    node_map = node_list_to_hashmap(node_list)

    initial_elements = [e for e in node_map.keys() if e.endswith('A')]

    last_element_found = False

    dirs = {'L': 0, 'R': 1}

    previous_elements = initial_elements

    while not last_element_found:
        for i in instructions:
            steps += 1

            next_elements = [node_map[e][dirs[i]] for e in previous_elements]

            if len([e for e in next_elements if e.endswith('Z')]) == len(next_elements):
                last_element_found = True
                break
            previous_elements = next_elements
    return steps
    
if __name__ == "__main__":
    with open(Path(__file__).parent.joinpath("input.txt"), "r") as file:
        input = [
            l.strip()
            for l in file
        ]
        instructions = input[0]
        nodes = input[2:]

    print(solution_p1(instructions, nodes))
    # print(solution_p2(instructions, nodes))
