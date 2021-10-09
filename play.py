a=["吐司,50"]
b=["布丁,15"]
c=["apple,40"]
d=["ice cream,65"]
print("""1號餐:吐司,40
2號餐:布丁,15
3號餐:apple,40
4號餐:ice cream,65""")


isok = False
while isok == False:
        need=int(input("need?>"))
        if need < 1 or need > 4:
            print("1~4號餐")
        else:
            if need == 1:
                print(a)
            elif need == 2:
                print(b)
            elif need == 3:
                print(c)
            else:
                print(d)
            isok == True
            break
