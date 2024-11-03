def is_same_color(cell1_row, cell1_col, cell2_row, cell2_col):
    return (cell1_row + cell1_col) % 2 == (cell2_row + cell2_col) % 2
cell1_row = int(input())
cell1_col = int(input())
cell2_row = int(input())
cell2_col = int(input())
if is_same_color(cell1_row, cell1_col, cell2_row, cell2_col):
    print("Да")
else:
    print("Нет")
