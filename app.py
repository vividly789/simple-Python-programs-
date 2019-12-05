#program to calculate the factorial of a given number
a=int(input("enter any number"))
factorial =1
if a < 0 :
    print("sorry, factorial donot exists")
elif a == 0:
    print("the factorial of 0 is 1")
else :
for i in range(1,a+1):
factorial=factorial*1
print("the factorial of the given number :" + a + "is" + factorial)



