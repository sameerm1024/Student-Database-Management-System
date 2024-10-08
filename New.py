def NewStu():
	import pickle
	import mysql.connector as db

	con = db.connect(host="localhost", user="root", password="shriram", database="shriram")
	cur = con.cursor()

	L = []
	SF = open("Student.dat", "ab+")
	Admn = int(input("Enter admission number of the student : "))
	SF.seek(0)
	chk = True

	try:
		while True:
			S = pickle.load(SF)
			for _ in range(len(S)):
				if S[0] == Admn:
					chk = False
	except EOFError or TypeError:
		pass

	if not chk:
		print("Student with Admission Number", Admn, "already present\nTry Again")
	else:
		Name = input("Enter name of the student : ")
		Class = input("Enter the student is currently studying : ")
		Section = input("Enter the section : ")
		Gender = input("Gender of the student?(M/F) : ")
		DOB = input("Enter date of birth (YYYY-MM-DD) : ")
		Stream = input("Enter Stream chosen : ")
		PhoneNo = int(input("Enter phone number of the student : "))

		L.append(Admn)
		L.append(Name.title())
		L.append(Class)
		L.append(Section.title())
		L.append(Gender.title())
		L.append(DOB)
		L.append(Stream.title())
		L.append(PhoneNo)

		query = f"insert into Student values ({Admn}, '{Name}','{Class}','{Section}','{Gender}','{DOB}','{Stream}',{PhoneNo})"
		cur.execute(query)
		print("Row inserted successfully!")
		con.commit()
		con.close()

		pickle.dump(L, SF)
		print("Thank You")
	SF.close()
