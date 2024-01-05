def move_position(position, instruction):
    if instruction == "^":
        position = (position[0]+1, position[1])
    elif instruction == "v":
        position = (position[0]-1, position[1])
    elif instruction == "<":
        position = (position[0], position[1]-1)
    elif instruction == ">":
        position = (position[0], position[1]+1)
    return position

def main():
    with open("input.txt", encoding="utf-8") as f:
        postion_part1 = (0,0)
        position_santa = (0,0)
        postion_robot_santa = (0,0)
        move_counter = 1
        visited_houses_part1 = []
        visited_houses_part2 = []
        instructions = f.readline()
        for instruction in instructions:
            postion_part1 = move_position(postion_part1, instruction)
            visited_houses_part1.append(postion_part1)
            if move_counter %2 == 0:
                postion_robot_santa = move_position(postion_robot_santa, instruction)
                visited_houses_part2.append(postion_robot_santa)
            else:
                position_santa = move_position(position_santa, instruction)
                visited_houses_part2.append(position_santa)
            move_counter += 1
        print(f"Solution Part1: {len(set(visited_houses_part1))}")
        print(f"Solution Part2: {len(set(visited_houses_part2))}")

if __name__ == "__main__":
    main()
