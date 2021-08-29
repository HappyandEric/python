# coding:utf-8
import random

a = random.randint(1, 20)
isok = False
i=0
while isok == False:
    print(a)
    b=int(input("數字>"))

    if a == b:
        print("good")
        break
    elif i == 4:
        print("again")
        break
    elif b>a:
        print("小一點")
        i=i+1
    elif b<a:
        print("大一點")
        i=i+1

    else:
        isok = True
