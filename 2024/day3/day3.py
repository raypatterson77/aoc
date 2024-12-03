import re

def compute_part_1(instruction_list: list) -> int:
    part_solution = 0
    for i in instruction_list:
        numbers = re.findall(r'\d+',i)
        part_solution = part_solution + (int(numbers[0]) * int(numbers[1]))
    return part_solution

def get_instruction_part_one(corrupted_input: str) -> list:
    return re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", corrupted_input)

def get_instructions_part_two(corrupted_input: str) -> list:
    return re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", corrupted_input)

def compute_part_2(instruction_list: list, calc: bool) -> list | bool:
    part_solution = 0
    for i in instruction_list:
        if i == "don't()":
            calc = False
        if i == "do()":
            calc = True
        if calc and i != "don't()" and i != "do()":
            part_solution = part_solution + compute_part_1([i])
    return part_solution,calc

def main():
    solution_part_one = 0
    solution_part_two = 0
    go_mode = True
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            instructions_part_one = get_instruction_part_one(line)
            instructions_part_two = get_instructions_part_two(line)
            line_solution_part_one = compute_part_1(instructions_part_one)
            line_solution_part_two, go_mode = compute_part_2(instructions_part_two, go_mode)
            solution_part_one = solution_part_one + line_solution_part_one
            solution_part_two = solution_part_two + line_solution_part_two
    print(f"solution part1 is {solution_part_one}")
    print(f"solution part2 is {solution_part_two}")

if __name__ == '__main__':
    main()
