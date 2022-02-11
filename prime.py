"""****************************************************
ALEETA ROSE               PRIME NUMBER
S3 IT
ROLL.NO:8
DATE:17/12/2021
*****************************************************"""
lower = int(input("enter the lower value:"))
upper = int(input("enter the upper value:"))
for number in range(lower,upper+1):
    if number>1:
      for i in range(2,number):
          if(number%i)==0:
             break
      else:
          print(number)
"""******************************************************
SAMPLE OUTPUT:

enter the lower value:1
enter the upper value:10
2
3
5
7
*****************************************************"""