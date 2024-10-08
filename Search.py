def SerStu():
	import pickle
	SF = open("Student.dat", "rb")
	print("How do you want to search ? ")
	while True:
		print("A) Search by Name\nB) Search by Admission Number")
		choice = input("Enter your choice : ")
		if choice in ("A", "a"):
			SF.seek(0)
			count = 0
			Name = input("Enter the Student Name :")
			try:
				while True:
					L = pickle.load(SF)
					for no in L:
						if no == Name.title():
							count += 1
							print("Admission Number : ", L[0])
							print("Name : ", L[1])
							print("Class : ", L[2])
							print("Section : ", L[3])
							print("Gender : ", L[4])
							print("Stream : ", L[5])
							print("Phone Number : ", L[6])
							print("\n")
			except EOFError or TypeError:
				pass
			if count > 1:
				print("There exists", count, "records with the name", Name.title())
			if count == 0:
				print("There exists no record with the name", Name.title())
				continue
		elif choice in ("B", "b"):
			Admn = int(input("Enter the Student Admission number :"))
			SF.seek(0)
			try:
				while True:
					L = pickle.load(SF)
					for _ in L:
						if L[0] == Admn:
							print("Admission Number : ", L[0])
							print("Name : ", L[1])
							print("Class : ", L[2])
							print("Section : ", L[3])
							print("Gender : ", L[4])
							print("Stream : ", L[5])
							print("Phone Number : ", L[6])
							break
			except EOFError or TypeError:
				pass
		else:
			print("INVALID CHOICE!!!")
		check = input("Do you want to return to the menu(Y/N) : ")
		if check not in ("YES", "Yes", "Y", "yes", "y"):
			break
	SF.close()
