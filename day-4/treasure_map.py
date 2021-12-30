row1 = ["😎", "😎", "😎"]
row2 = ["😎", "😎", "😎"]
row3 = ["😎", "😎", "😎"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n")
# column 2, row 3 would be entered as: 23
horizontal = int(position[0]) #2
vertical = int(position[1])   #3

#selected_row = map[vertical - 1]
#selected_row[horizontal - 1] = " X"

map[vertical - 1][horizontal - 1] = " X"

print(f"{row1}\n{row2}\n{row3}")