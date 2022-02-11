"""**************************************************
ALEETA ROSE           NCR
S3 IT
ROLL NO:8
DATE:6/12/2021
***************************************************"""
def nCr(n,r):
	return(fact(n)/(fact(r)*fact(n-r)))
def fact(n):
	res=1
	for i in range(2,n+1):
		res=res*i
	return res
n=int(input("enter the first number"))
r=int(input("enter the second number"))
print(int(nCr(n,r)))
"""*************************************************
SAMPLE OUTPUT:
enter the first number9
enter the second number3
84
*************************************************"""