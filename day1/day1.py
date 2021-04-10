def input_to_list(input_name):
    with open(input_name) as f:
        input = f.readlines()
    return [int(x.strip()) for x in input]

def part_1(input):
    for i in range (0, len(input)):
        for j in range (i+1, len(input)):
            if input[i] + input[j] == 2020:
                return input[i]*input[j]

def part_2(input):
    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            for k in range(i+2, len(input)):
                if input[i] + input[j] + input[k] == 2020:
                    return input[i] * input[j] * input[k]

test = False

input_name = "day1testinput.txt" if test else "day1input.txt"
input = input_to_list(input_name)
print(part_1(input))
print(part_2(input))
