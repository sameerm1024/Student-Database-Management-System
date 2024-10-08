def ForPass():
	import pickle
	import SignIn
	import SignUp
	import os
	UF = open("User Data.dat", "rb+")
	TF = open("Temp.dat", "ab+")
	print("Reset Your Password")
	Email = input("Enter your Email Address : ")
	flag = 0
	try:
		while True:
			L = pickle.load(UF)
			if L[4] == Email:
				print(L[0], "is your username")
				print("Make sure that your password must contain all types of characters.")
				Pass = input("New Password : ")
				CnfPass = input("Confirm your New password : ")
				if Pass != CnfPass:
					print("Password did not match\nTry Again")
				else:
					L[1] = Pass
					pickle.dump(L, TF)
					print("Congratulations!!!\nPassword created Successful")
					flag = 1

			else:
				flag = 0
				pickle.dump(L, TF)
	except EOFError or TypeError:
		pass
	if flag == 0:
		print("Email Not Found")
		print("SignUp to create an account")
		SignUp.SignUp()
	if flag == 1:
		SignIn.SignIn()
	TF.close()
	UF.close()
	os.remove("User Data.dat")
	os.rename("Temp.dat", "User Data")