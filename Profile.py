def Pro():
	import pickle
	import os
	SF = open("User Data.dat", "rb")
	Email = input("Confirm your E-mail Address : ")
	while True:
		print("A) View Profile\nB) Update Profile")
		choice = input("Enter your choice : ")
		if choice == "A" or choice == "a":
			try:
				while True:
					print("\n")
					L = pickle.load(SF)
					print("Username: ", L[0])
					print("Password : ", L[1])
					print("First Name : ", L[2])
					print("Last Name : ", L[3])
					print("Email Address : ", L[5])
					print("Gender : ", L[6])
					print("DOB : ", L[0])
			except EOFError:
				pass
		elif choice == "B" or choice == "b":
			print("\n")
			TF = open("Temp.dat", "ab+")
			print("If you want to update any of the field enter the new one\nOtherwise press enter")
			print("\n")
			try:
				while True:
					print("\n")
					L = pickle.load(SF)
					print("Username: ", L[0])
					print("Password : ", L[1])
					print("First Name : ", L[2])
					print("Last Name : ", L[3])
					print("Email Address : ", L[5])
					print("Gender : ", L[6])
					print("DOB : ", L[0])
					if L[4] == Email:
						FName = input("Update your First Name : ")
						LName = input("Update your Last Name : ")
						Email = input("Update your Email Address : ")
						DOB = input("Update your Date Of Birth : ")
						Gender = input("Update your gender (M/F) : ")
						User = input("Update Your Username : ")
						Pass = input("Update Strong Password : ")
						CnfPass = input("Confirm your password : ")
						if Pass != CnfPass:
							print("Password did not match\nTry Again")
							Pass = input("Update Strong Password : ")
							CnfPass = input("Confirm your password : ")
							if Pass != CnfPass:
								print("Password did not match\nTry Again")
							else:
								if User == "":
									L[0] = L[0]
								else:
									L[0] = User.title()
								if Pass == "":
									L[1] = L[1]
								else:
									L[1] = Pass
								if FName == "":
									L[2] = L[2]
								else:
									L[2] = FName.title()
								if LName == "":
									L[3] = L[3]
								else:
									L[3] = LName.title()
								if Email == "":
									L[4] = L[4]
								else:
									L[4] = Email
								if Gender == "":
									L[5] = L[5]
								else:
									L[5] = Gender.title()
								if DOB == "":
									L[6] = L[6]
								else:
									L[6] = DOB
								pickle.dump(L, TF)
								print("Congratulations!!!\nProfile Updated Successful")
						else:
							if User == "":
								L[0] = L[0]
							else:
								L[0] = User.title()
							if Pass == "":
								L[1] = L[1]
							else:
								L[1] = Pass
							if FName == "":
								L[2] = L[2]
							else:
								L[2] = FName.title()
							if LName == "":
								L[3] = L[3]
							else:
								L[3] = LName.title()
							if Email == "":
								L[4] = L[4]
							else:
								L[4] = Email
							if Gender == "":
								L[5] = L[5]
							else:
								L[5] = Gender.title()
							if DOB == "":
								L[6] = L[6]
							else:
								L[6] = DOB
							pickle.dump(L, TF)
							print("Congratulations!!!\nProfile Updated Successful")
					else:
						pickle.dump(L, TF)
			except EOFError or TypeError:
				pass
			SF.close()
			TF.close()
			os.remove("User Data.dat")
			os.rename("Temp.dat", "User Data.dat")
			check = input("Do you want to return to the menu(Y/N) : ")
			if check not in ("YES", "Yes", "Y", "yes", "y"):
				break
