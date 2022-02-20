puzzle_input = open('2015_1.txt', 'r')
data = puzzle_input.read()

floor = 0

for i in range(0, len(data)):
    if(data[i] == '('):
        floor = floor + 1
    if(data[i] == ')'):
        floor = floor - 1
    if floor == -1:
        print(range(i))

print(floor)
