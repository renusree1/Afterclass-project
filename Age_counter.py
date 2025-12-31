age=int(input("Enter your age:- "))
cal= age%2
try:
    if cal == 0:
        print("Your age is", age, ".It is a even number")
    else:
        print("Your age is", age, ".It is and odd number")
except:
    print("Invalid response... Pls try again!")
