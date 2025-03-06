input_str = input("Nhập X, Y :")
dimensions = [int(x) for x in input_str.split(',')]  # Correct list comprehension syntax
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

print(multilist)
