***************************************************************
ALEETA ROSE             VOWELS,CONSTONANTS,WORDS,QM
S3 IT
ROLL.NO:8
DATE:9/12/2021
****************************************************************
string = input("enter a string")
c=0
v=0
qm=0
w=1
for i in string:
	if(i=='a' or i=='i' or i=='o' or i=='u'):
		v=v+1
	elif(i==" "):
		w=w+1
	elif(i=="?"):
		qm=qm+1
	else:
		c=c+1
print('vowels=',v)
print('words=',w)
print('consonents=',c)
print('qm=',qm)
***************************************************************
SAMPLE OUTPUT:
enter a string hi i am aleeta rose
vowels= 6
words= 6
consonents= 9
qm= 0

***************************************************************