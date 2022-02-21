dict = {num:0 for num in range(0, 1001)}
dict[0] = 0
dict[1] = 3
dict[2] = 3
dict[3] = 5
dict[4] = 4
dict[5] = 4
dict[6] = 3
dict[7] = 5
dict[8] = 5
dict[9] = 4
dict[10] = 3
dict[11] = 6
dict[12] = 6
dict[13] = 8
dict[14] = 8
dict[15] = 7
dict[16] = 7
dict[17] = 9
dict[18] = 8
dict[19] = 8
dict[20] = 6
dict[30] = 6
dict[40] = 5
dict[50] = 5
dict[60] = 5
dict[70] = 7
dict[80] = 6
dict[90] = 6
dict[1000] = 11

for i in range(21, 100):
    tens = int(i / 10) *10
    ones = i - tens
    dict[i] = dict[tens] + dict[ones]

for i in range(100, 1000):
	hundreds = int(i/100)
	tens_ones = i - hundreds*100
	if tens_ones == 0:
		dict[i] = dict[hundreds] + 7
	else:
		dict[i] = dict[hundreds] + 10 + dict[tens_ones]

print(sum(dict.values()))