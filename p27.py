from p26 import add,sub,div,rem,mul,pow
a=float(input("enter the 1st number"))
b=float(input("enter the 2nd number"))
c=str(input("enter the operation"))

if (c=="+"):
    r=add(a,b)
    print(r)

elif (c=="-"):
    r=sub(a,b)
    print(r)

elif (c=="/"):
    r=div(a,b)
    print(r)

elif (c=="*"):
    r=mul(a,b)
    print(r)

elif (c=="%"):
    r=rem(a,b)
    print(r)

elif (c=="^"):
    r=pow(a,b)
    print(r)

