num= int(input("Enter a number: "))
cal= ""
print("Converting", num, "to binary")
while num > 0:
  bin_num= num%2
  num= num//2
  cal+= str(bin_num)
  print(bin_num)
cal = cal[::-1]
print("Your number has been converted to binary:", cal,)
