row1=["😀","😁","😆"]
row2=["😅","😂","🤣"]
row3=["😎","😍","😘"]
print(f"{row1}\n{row2}\n{row3}\n")
position=input("Entre the position ")
matrix=[row1,row2,row3]
row_number=int(position[0])
column_number=int(position[1])
a=matrix[row_number-1]
a[column_number-1]="arun"
print(f"{row1}\n{row2}\n{row3}\n")



