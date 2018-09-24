import pymysql
import codecs
ip="localhost"
U="root"
db=pymysql.connect(ip,U,"","last words")
last=""
e1=""
e2=""
e3=""
e4=""
e5=""
e6=""
e7=""


n=1

file1=codecs.open("LASTREAL.txt", "r+" , "utf-8")

for L1 in file1:
	x=L1
	break
for L1 in file1:
	#print(L1)
	
	if (L1 == x):
		print("a")
		c=db.cursor()
		SQL= f"Insert into last values('{last}','{e1}','{e2}','{e3}','{e4}','{e5}','{e6}','{e7}')"
		print(SQL)
		c.execute(SQL)
		db.commit()
		n=1
		e1=""
		e2=""
		e3=""
		e4=""
		e5=""
		e6=""
		e7=""
		
	elif (n==1):
		n=2
		last=L1
		print(last)
		
	elif (n==2):
		n=3
		e1=L1
		print(e1)
	elif (n==3):
		n=4
		e2=L1
		print(e2)
	elif (n==4):
		n=5
		e3=L1
	elif (n==5):
		n=6
		e4=L1
	elif (n==6):
		n=7
		e5=L1
	elif (n==7):
		n=8
		e6=L1
	elif (n==8):
		n=9
		e7=L1
	elif (n==9):
		print("something went wrong")
		print (L1)
		input=("test")
		
		