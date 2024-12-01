def main():
    left_list = list()
    right_list = list()
    solution_day1 = 0
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            line_elems = line.split(" ")
            line_elems = [int(i) for i in line_elems if i]
            left_list.append(line_elems[0])
            right_list.append(line_elems[1])
    left_list.sort()
    right_list.sort()

    for x,y in zip(left_list, right_list):
        if (x - y) < 0:
            solution_day1 = solution_day1 + abs(x-y)
        else:
            solution_day1 = solution_day1 + (x-y)
    print(solution_day1)

if __name__ == '__main__':
    main()