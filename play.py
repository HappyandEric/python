a=["吐司,50元"]
b=["布丁,15元"]
c=["apple,40元"]
d=["ice cream,65元"]
print("""1號餐:吐司,40元
2號餐:布丁,15元
3號餐:apple,40元
4號餐:ice cream,65元""")

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
