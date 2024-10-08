def Main():
	import New
	import Details
	import Count
	import Export
	import Search
	import os
	import Remove
	import Update
	import Profile
	import Login
	print("\t\t\t\t\t\tWelcome to Students Database")
	print("--------------------------------------------------------------------------------------------------------------")
	Code = input("Enter the secret code to authenticate : ")
	if Code.lower() == "20081507":
		while True:
			print("Menu: ")
			print("1. Add New Students")
			print("2. Display Students Details")
			print("3. Search Student")
			print("4. Export Student Data")
			print("5. No Of Students")
			print("6. Update Student Details")
			print("7. Remove Student")
			print("8. View Your Account")
			print("Enter your choice : ", end=" ")
			choice = int(input())
			if choice == 1:
				New.NewStu()
				Count.StuCnt()
			elif choice == 2:
				Details.StuDet()
				Count.StuCnt()
			elif choice == 3:
				Search.SerStu()
			elif choice == 4:
				Export.ExpDet()
			elif choice == 5:
				Count.StuCnt()
			elif choice == 6:
				Update.UpStu()
			elif choice == 7:
				Remove.ReStu()
			elif choice == 8:
				print("A) Profile\nB) Logout\nC) Delete Account")
				choice = input("Enter your choice : ")
				if choice == "A" or choice == "a":
					Profile.Pro()
				elif choice == "B" or choice == "b":
					os.system('cls')
					Login.Log()
				elif choice == "C" or choice == "c":
					Remove.ReUser()
			else:
				print("Invalid Choice")
			check = input("Do you want to return to the main menu(Y/N) : ")
			if check not in ("YES", "Yes", "Y", "yes", "y"):
				os.system('cls')
				break
	else:
		print("Incorrect Code Entered\nContact Admin")
	print("THANKS FOR VISITING STUDENT DATABASE :)\nHAVE A GOOD DAY AHEAD!")
