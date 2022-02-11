"""******************************************************
ALEETA ROSE                 FIBONACCI SERIES
S3 IT
ROLL.NO:8
DATE:
******************************************************"""
n=int(input("enter the num"))
n1,n2 =0,1
count=0
if(n<=0):
   print("please enter positive integer")
elif n==1:
     print("fibonacci series upto",n,":")
     print(n1)
else:
     print("fibonacci series:")
while count<n:
      print(n1)
      nth=n1+n2
      n1=n2
      n2=nth
      count+=1
"""******************************************************
SAMPLE OUTPUT:  

enter the num7
fibonacci series:
0
1
1
2
3
5
8
******************************************************"""

      