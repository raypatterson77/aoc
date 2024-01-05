def main():
    solution_part1 = 0
    solution_part2 = 0 
    with open('input.txt', encoding='utf-8') as f:
        for line in f:
            values = [int(x) for x  in line.strip().split("x")]
            dimesions = []
            dimesions.append(values[0]*values[1])
            dimesions.append(values[1]*values[2])
            dimesions.append(values[0]*values[2])
            solution_part1 = solution_part1 + (2*dimesions[0] + 2*dimesions[1] + 2*dimesions[2] + min(dimesions))
            
            #part2
            values.sort()
            ribbon_wrap = 2*values[0]+2*values[1]
            ribbon_bow = values[0] * values[1] * values[2]
            solution_part2 = solution_part2 + ribbon_bow + ribbon_wrap
    print(f"Solution Part1 is {solution_part1}")
    print(f"Solution Part2 is {solution_part2}")

if __name__ == '__main__':
    main()
