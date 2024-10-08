def StuCnt():
	import pickle
	SF = open("Student.dat", "rb")
	cnt = 0
	try:
		while True:
			Det = pickle.load(SF)
			cnt += 1
	except EOFError:
		pass
	print("There are a total of", cnt, "records")
	SF.close()
