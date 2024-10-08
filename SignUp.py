def SignUp():
    import random
    import pickle
    import os
    import Login
    L = []
    UF = open("User Data.dat ", "ab+")
    print("\t\t\t\t\t\tWelcome to Registration Window")
    print("***********************************************************************************************************")
    FName = input("Enter your First Name : ")
    LName = input("Enter your Last Name : ")
    Email = input("Enter your Email Address : ")
    flag = 0
    chk = True
    try:
        while True:
            L = pickle.load(UF)
            for _ in range(len(L)):
                if L[4] == Email:
                    chk = False
    except EOFError or TypeError:
        pass
    if not chk:
        print("User with Email Address", Email, "already present\nTry Again")
    else:
        DOB = input("Enter your Date Of Birth : ")
        Gender = input("Enter your gender (M/F) : ")
        UN = FName+str(random.randint(1000, 9999))
        print(UN, "will be used as your Username\nNote it down quickly")
        while True:
            print("Make sure that your password contains all types of characters.")
            Pass = input("Create a Strong Password : ")
            CnfPass = input("Confirm your password : ")
            if Pass != CnfPass:
                print("Password did not match\n"
                      "Try Again")
            else:
                print("Congratulations!!!\n"
                      "Registration Successful")
                flag = 1
                break
        L.append(UN.title())
        L.append(Pass)
        L.append(FName.title())
        L.append(LName.title())
        L.append(Email)
        L.append(Gender.title())
        L.append(DOB)
        pickle.dump(L, UF)
        UF.close()
    if flag == 1:
        os.system('cls')
        Login.Log()
