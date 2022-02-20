# day2_data_file = open('AOC_3.txt', 'r')
# day2_data_list = day2_data_file.read().splitlines()
# day2_data_list = list(map(str, day2_data_list))
bit_0 = 0
bit_1 = 0


day2_data_list = ["001001", "110110", "010100"]
for item in day2_data_list:

    if item[0] == "0":
        bit_0 += 1
    else:
        bit_1 += 1

print(bit_1)
print(bit_0)

# if bit_1 > bit
