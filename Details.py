def StuDet():
	import pickle
	SF = open("Student.dat", "rb")
	try:
		while True:
			L = pickle.load(SF)
			print("Admission Number : ", L[0])
			print("Name : ", L[1])
			print("Class : ", L[2])
			print("Section : ", L[3])
			print("Gender : ", L[4])
			print("Stream :", L[5])
			print("DOB : ", L[6])
			print("DOJ : ", L[7])
			print("Phone Number : ", L[8])
			print("Address : ", L[9])
			print("\n")
	except EOFError:
		pass
	SF.close()


StuDet()
