a=int(input("enter any number"))
factorial = 1

if a<0:
    print("sorry, no factorial for negative no.")
elif a==0:
    print("its factorial is 1")
else:
    for i in range(1,a+1):
      factorial=factorial*i
    print("the factorial is", factorial)