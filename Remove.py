def ReStu():
	import pickle
	import os
	SF = open("Student.dat", "rb")
	UF = open("Temp.dat", "wb")
	Admn = int(input("Enter the Admission Number of Student whose details are to be removed : "))
	flag = 0
	try:
		while True:
			L = pickle.load(SF)
			if Admn in L:
				flag = 1
				continue
			else:
				pickle.dump(L, UF)
	except EOFError or TypeError:
		pass
	if flag == 1:
		print("Successful Removed")
	else:
		print("No such Admission number present")
	UF.close()
	SF.close()
	os.remove("Student.dat")
	os.rename("Temp.dat", "Student.dat")


def ReUser():
	import pickle
	import os
	SF = open("User.dat", "rb")
	UF = open("Temp.dat", "wb")
	UN = input("Enter Your Username : ")
	Pass = input("Enter Your Password : ")
	flag = 0
	try:
		while True:
			L = pickle.load(SF)
			if (UN and Pass) in L:
				flag = 1
				continue
			else:
				pickle.dump(L, UF)
	except EOFError or TypeError:
		pass
	if flag == 1:
		print("Successful Removed")
	else:
		print("No such User number present")
	UF.close()
	SF.close()
	os.remove("User.dat")
	os.rename("Temp.dat", "User.dat")
