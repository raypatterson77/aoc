def enter_cellar(move_instruction):
    intstruction_pos = 0
    move_pos = 0
    for move in move_instruction:
        if move_pos == -1:
            return intstruction_pos
        intstruction_pos += 1
        if move == ("("):
            move_pos += 1
        else:
            move_pos -=1
    return intstruction_pos

def main():
    with open("input.txt", encoding="utf-8") as f:
        move_instruction =  f.readline().strip()
        move_ups = move_instruction.count("(")
        move_down = move_instruction.count(")")
        print(f"Solution Part1: {move_ups-move_down}")

        #part2
        print(f"Solution Part2: {enter_cellar(move_instruction)}")
if __name__ == '__main__':
    main()
