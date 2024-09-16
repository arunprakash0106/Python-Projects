a=input("enter the numbers to get average seprated by comma : ")
number_list=a.split(",")
length_list=len(number_list)
for i in range(0,length_list):
    number_list[i]=int(number_list[i])
sum=0
for j in number_list:
    sum=sum+j
average=sum/length_list
print(int(average))
