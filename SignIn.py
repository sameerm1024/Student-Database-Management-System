def SignIn():
    import pickle
    import MainPage
    import Forgot
    import SignUp
    import os
    import Login
    UF = open("User Data.dat", "rb")
    User = input("Enter your Username : ")
    Pass = input("Enter your password : ")
    flag = 0
    try:
        while True:
            L = pickle.load(UF)
            if (L[0] == User) and (L[1] == Pass):
                print("SignIn Successful")
                os.system('cls')
                MainPage.Main()
            """else:
                print("Try Again")
                for _ in L:
                    User = input("Enter your Username : ")
                    Pass = input("Enter your password : ")
                    if L[0] == User and L[1] == Pass:
                        os.system('cls')
                        print("SignIn Successful")
                        MainPage.Main()
                    elif (User or Pass) not in L:
                        Forgot.ForPass()
                    else:
                        flag = 1
                        break"""
    except EOFError or TypeError:
        pass
    if flag == 1:
        print("Invalid Credentials")
        print("Try Again")
        print("SignUp To Create An Account")
        print("Want to create an account?(YES/NO)")
        choice = input("Enter your choice")
        if choice in ("YES", "NO", "Yes", "No", "Y", "N", "yes", "no", "y", "n"):
            os.system('cls')
            SignUp.SignUp()
        else:
            Login.Log()
    UF.close()
