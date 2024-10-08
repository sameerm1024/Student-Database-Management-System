def Log():
	import SignIn
	import SignUp
	import os
	print("\t\t\t\t\t\tSignIn To Your Account")
	print("--------------------------------------------------------------------------------------------------------------")
	print("1. Existing User\n2. New User ")
	choice = int(input("Enter your choice : "))
	if choice == 1:
		SignIn.SignIn()
		os.system('cls')
	elif choice == 2:
		SignUp.SignUp()
		os.system('cls')
	else:
		print("Invalid Choice")
