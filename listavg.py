"""******************************************************************************
ALEETA ROSE                    LIST AVERAGE
S3 IT
ROLL.NO:8
DATE:17/12/2021
*******************************************************************************"""
list=[]
slist=[]
n = int(input("enter the size of the list"))
print("enter the elements of the list")
for i in range(0,n):
	c=int(input(" "))
	list.append(c)
print("list")
count=0
for y in list:
	count=count+y
for y in list:
	square=y**2
	slist.append(square)
print("the sum of the elements are:",count)
print("the average of the elements are:",count)
print("the square of the list is:",slist)
"""********************************************************************************
SAMPLE OUTPUT: 

enter the size of the list5
enter the elements of the list
 1
 2
 3
 4
 5
[1, 2, 3, 4, 5]
the sum of the elements are: 15
the average of the elements are: 15
the square of list is: [1, 4, 9, 16, 25]

*******************************************************************************"""
	