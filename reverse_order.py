num= int(input("Enter a number:"))
if num == 0:
    print("There is 1 digit")
else:
    i=0
    while num >= 1:
        num= num//10
        i= i+1
    print("There are", i,"digits")
