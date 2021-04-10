import os

for i in range(1,26):
    print(i)
    day = f"day{i}"
    os.mkdir(day)
    curpy = f"{day}/{day}.py"
    with open(curpy, 'w') as fp:
        pass

    curinput = f"{day}/{day}input.txt"
    with open(curinput, 'w') as fp:
        pass

    curtest = f"{day}/{day}testinput.txt"
    with open(curtest, 'w') as fp:
        pass
    print('\n')
