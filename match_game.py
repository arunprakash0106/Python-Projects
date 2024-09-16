row1=["😀","😁","😆"]
row2=["😅","😂","🤣"]
row3=["😎","😍","😘"]
print(f"{row1}\n{row2}\n{row3}\n")
position=input("Entre the position ")
matrix=[row1,row2,row3]
row_number=int(position[0])
column_number=int(position[1])
x1=["100","0","10"]
x2=["0","20","0"]
x3=["500","0","1000"]
k=int(column_number)
y=int(row_number)
if row_number==1 and column_number==int(position[1]):
    a=matrix[row_number-1]
    a[column_number-1]=x1[k-1]
    print(f"{row1}\n{row2}\n{row3}\n")
elif row_number==2 and column_number==int(position[1]):
    a=matrix[row_number-1]
    a[column_number-1]=x2[k-1]
    print(f"{row1}\n{row2}\n{row3}\n")
elif row_number==3 and column_number==int(position[1]):
    a=matrix[row_number-1]
    a[column_number-1]=x3[k-1]
    print(f"{row1}\n{row2}\n{row3}\n")


