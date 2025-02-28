# try and except
x=int(input("enter the 1st number :"))
y=int(input("enter the 2nd number :"))
try:
    z=x/y
    print("result", z)
except Exception as a:
    print("invalid attempt of devision",a)
print("hello this line is last line")