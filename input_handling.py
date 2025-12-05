"""a=input("Enter num 1:")
b=input("Enter num 2:")
print(a+b)
#input always take input as strings so always use typecast
c=int(input("Enter num 1:"))
d=int(input("Enter num 2:"))
print(c+d)"""
import sys
fullname = " ".join(sys.argv[1:])
email=fullname.lower().replace(" ",".")+ "@gmail.com"
print("Your profile")
print("Full name:",fullname)
print("Email:",email)
