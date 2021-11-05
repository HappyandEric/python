# coding:utf-8

print("歡迎來到英文字典")
while True:
    print("""1.目錄
2.英文字典
3.學習成果測驗(非常難，老師你應該不行[我建議貴老師您不要嘗試])
4.列出單字
5.離開系統""")
    abc=int(input(">"))
    if abc == 1:
        print("a~z")
    elif abc == 2:
        dictionary={
        'a':'(airport,機場),(airplant,飛機),(away,永遠),(Africa,非洲),(African,非洲的\人)',
        'b':'(bomb,炸彈),(biography,傳(念ㄓㄨㄢˋ)),(beat,打敗),(bee,蜜蜂),(battery,電池)'}
        a=input("(a~z)?>")
        n=dictionary.get(a)
        print(n)
    elif abc == 3:
        apron=input("apron=?>")
        if apron == ("停機坪"):
            print("yes,good job")
        else:
            print("no,answer:停機坪")
    elif abc == 4:
        for i in dictionary.keys():
            print(i)
    
        for i in dictionary.values():
            print(i)
    
        for i in dictionary.items():
            print(i)
    elif abc == 5:
        break
