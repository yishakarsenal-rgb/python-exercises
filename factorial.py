num= int(input("enter number="))
if num < 0:
    print("invalid")
else :
    a = 1
    for i in range(1,num+1):
        a *= i
    print(a)