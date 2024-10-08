def UpStu():
	import pickle
	import os
	import mysql.connector as db

	con = db.connect(host="localhost", user="root", password="shriram", database="shriram")
	cur = con.cursor()

	SF = open("Student.dat", "rb")
	TF = open("Temp.dat", "ab+")
	AdmnNo = int(input("Enter the Admission Number of Student whose details are to be updated : "))
	flag = 0
	try:
		while True:
			L = pickle.load(SF)
			if L[0] == AdmnNo:
				L = pickle.load(SF)
				print("Admission Number : ", L[0])
				print("Name : ", L[1])
				print("Class : ", L[2])
				print("Section : ", L[3])
				print("Gender : ", L[4])
				print("DOB : ", L[5])
				print("DOJ : ", L[6])
				print("Stream :", L[7])
				print("Phone Number : ", L[8])
				print("Address : ", L[9])
				D = L
				print(D)
	except EOFError or TypeError:
		pass
	searchq = "select * from student where AdmnNO={}".format(AdmnNo)
	cur.execute(searchq)
	rs = cur.fetchall()
	if not rs:
		print("No such Admission Number in the table!!")
	else:
		Name = input("Enter the correct student's name:")
		DOB = input("Enter the correct date of birth:")
		Address = input("Enter the correct Designation:")

		query = "update student set Name='{}',DOB='{}',Address='{}' where AdmnNO={}".format(Name, DOB, Address, AdmnNo)
		cur.execute(query)
		print("Updation successful!")
		con.commit()

	con.close()
	SF.close()
	TF.close()
	os.remove("Student.dat")
	os.rename("Temp.dat", "Student.dat")


"""
if choice == "A" or choice == "a":
	SF.seek(0)
	while True:
		L = pickle.load(SF)
		if L[0] == AdmnNo:
			Sec = input("Enter new Section : ")
			L[3] = Sec.upper()
			print(L)
			pickle.dump(L, US)
			flag = 1
		else:
			pickle.dump(L, US)
elif choice == "B" or choice == "b":
	SF.seek(0)
	while True:
		L = pickle.load(SF)
		if L[0] == AdmnNo:
			PhNo = int(input("Enter New Phone Number : "))
			L[6] = PhNo
			pickle.dump(L, US)
			flag = 1
		else:
			pickle.dump(L, US)
else:
	print("Invalid Choice")"""

UpStu()
