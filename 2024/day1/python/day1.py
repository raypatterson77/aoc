def build_dict(l: list) -> dict:
    sl = set(l)
    dl = dict.fromkeys(sl, 0)
    for k, _ in dl.items():
        dl[k] = l.count(k)
    return dl

def main():
    left_list = list()
    right_list = list()
    solution_part1 = 0
    solution_part2 = 0
    #prepare input
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            line_elems = line.split(" ")
            line_elems = [int(i) for i in line_elems if i]
            left_list.append(line_elems[0])
            right_list.append(line_elems[1])
    left_list.sort()
    right_list.sort()

    #part2
    dict_left = build_dict(left_list)
    dict_right = build_dict(right_list)
    for k, v in dict_left.items():
        solution_part2 = solution_part2 + (k * v * dict_right.get(k, 0))

    #part1
    for x,y in zip(left_list, right_list):
        if (x - y) < 0:
            solution_part1 = solution_part1 + abs(x-y)
        else:
            solution_part1 = solution_part1 + (x-y)
    #output
    print(f"solution part1 is {solution_part1}")
    print(f"solution part2 is {solution_part2}")

if __name__ == '__main__':
    main()
