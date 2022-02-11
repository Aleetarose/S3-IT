
"""*******************************************************************
ALEETA ROSE                           FACTORIAL
S3 IT
ROLL.NO:8
DATE:
*******************************************************************"""
def factorial(n):
	if n < 0:
	   return 0
	elif n == 0:
	   return 1
	else:
           return(n*fact(n-1))
n=int(input("input a number to compute the factorial:"))
print(factorial(n))
"""******************************************************************
SAMLE OUTPUT:

input a number to compute the factorial:4
24
*******************************************************************"""