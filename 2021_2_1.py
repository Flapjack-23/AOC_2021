day2_data_file = open('2021_2.txt', 'r')
day2_data_list = day2_data_file.read().splitlines()

h_count = 0
d_count = 0
#
for item in day2_data_list:
    # find number index, should always be last character
    num = int(item[-1])

    if 'forward' in item:
        h_count += num

    elif 'down' in item:
        d_count += num

    elif 'up' in item:
        d_count -= num

print(h_count)
print(d_count)
print(d_count * h_count)

print(day2_data_list)
