row1 = ['👮', '👮', '👮']
row2 = ['👮', '👮', '👮']
row3 = ['👮', '👮', '👮']

matrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
number = input("Enter the number where you want to hide money : ")
row_num = int(number[0])
col_num = int(number[1])

if not (row_num <= 3 and row_num >= -3 and row_num != 0):
    print("Invalid row number")
if not (col_num <= 3 and col_num >= -3 and col_num != 0):
    print("Invalid column number")

row_selected = row_num - 1;
col_selected = col_num - 1;

matrix[row_selected][col_selected] = 'X'

print(f"{row1}\n{row2}\n{row3}")

