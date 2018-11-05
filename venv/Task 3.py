def largestnum(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
        print(num1)
    elif (num2 >= num1) and (num2 >= num3):
        print(num2)
    else:
        print(num3)

num1 = int(input("pick a number"))
num2 = int(input("pick a number"))
num3 = int(input("pick another number"))
print("the largest number is")
largestnum(num1, num2, num3)
