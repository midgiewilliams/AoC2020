def process_input(input_name):
    with open(input_name) as f:
        input = f.readlines()
    input = [x.strip().split(' ') for x in input]

    for i in range(0, len(input)):
        input[i][0] = input[i][0].split('-')
        input[i][0] = [int(x) for x in input[i][0]]
        input[i][1] = input[i][1][0]

    return input

def part_1(input):
    valid = 0
    for inp in input:
        ran, lett, pw = inp
        min, max = ran
        count = 0
        for p in pw:
            if p == lett:
                count += 1

        if count >= min and count <= max:
            valid += 1
    return valid

def part_2(input):
    valid = 0
    for inp in input:
        ind, lett, pw = inp
        ind1, ind2 = ind
        if pw[ind1-1] == lett and pw[ind2-1] != lett:
            valid += 1
        elif pw[ind1-1] != lett and pw[ind2-1] == lett:
            valid += 1
    return valid


test = False

input_name = "day2testinput.txt" if test else "day2input.txt"
input = process_input(input_name)
print(part_1(input))
print(part_2(input))
