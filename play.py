x = int(input("輸入英文成績>"))
v = int(input("輸入數學成績>"))
if x <90 and v <90:
    print("受罰")
elif x >90 and v >90:
    print("獎勵")
else:
    print("加油")