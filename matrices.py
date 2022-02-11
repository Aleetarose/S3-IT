"""**********************************************************************************
ALEETA ROSE                        ADDITION OF MATRIX
S3 IT
ROLL.NO:8
DATE:14/12/2021
************************************************************************************"""
rows = int(input(" enter the no of rows:"))
column = int(input("enter the no of columns:"))
print("enter the elements of first matrix:")
matrix_a = [[int(input()) for i in range(column)] for i in range(rows)]
print("first matrix is:")
for n in matrix_a:
	print(n)
print("enter the elements of second matrix:")
matrix_b = [[int(input()) for i in range(column)] for i in  range(rows)]
for n in matrix_b:
	print(n)
	result=[[0 for i in range(column)] for i in range(rows)]
for i in range (rows):
	for j in range(column):
		result[i][j] = matrix_a[i][j] + matrix_b[i][j]
print("the sum of the  two matrix is:")
for r in result:
	print(r)
"""*********************************************************************************
SAMPLE OUTPUT:

 enter the no of rows:3
enter the no of columns:3
enter the elements of first matrix:
1
2
3
4
5
6
2
1
0
first matrix is:
[1, 2, 3]
[4, 5, 6]
[2, 1, 0]
enter the elements of second matrix:
1
0
0
0
1
0
0
1
1
[1, 0, 0]
[0, 1, 0]
[0, 1, 1]
the sum of the  two matrix is:
[2, 2, 3]
[4, 6, 6]
[2, 2, 1]
********************************************************************************"""



