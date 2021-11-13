# coding:utf-8

print("歡迎來到英文字典")
i=0
while True:
    print("""1.目錄
2.英文字典
3.學習成果測驗(非常難，老師你應該不行[我建議貴老師您不要嘗試])
4.列出單字
5.離開系統""")
    abc=int(input("?>"))
    if abc == 1:
        print("a~z")
    elif abc == 2:
        dictionary={
                'a':'(airport,機場),(airplant,飛機),(away,永遠),(Africa,非洲),(African,非洲的\人)',
                'b':'(bomb,炸彈),(biography,傳(念ㄓㄨㄢˋ)),(beat,打敗),(bee,蜜蜂),(battery,電池)',
                'c':'(CC+,一種程式),(car,車)',
                'd':'(dictionary,字典),(decide,決定)',
                'e':'(eat/ate,吃),(eary,早)',
                'f':'(feet/foot,腳),(fight,打架)',
                'g':'(great,讚),(good,好棒，通"great")',
                'h':'(hot,熱),(hello,你好)',
                'i':'(ice-cream,冰淇淋),(ice,冰)',
                'j':'(Java,一種程式),(Jess,一種名子)',
                'k':'(kayak,獨木舟),(key,鑰史)',
                'l':'(learn,學),(low,低)',
                'm':'(me/mine,我),(May,五月)',
                'n':'(none,沒有),(need,需要)',
                'o':'(owl,貓頭鷹),(own,自己的)',
                'p':'(person/people,人),(pig,豬)',
                'q':'(queen,女王(記得家"陛下"二字)),(quick,快)',
                'r':'(rooster,哦偷拜),(road,馬路(動物界、節肢動物們(才不是)))',
                's':'(soaked,溼),(save,安全)',
                't':'(tweezers,鑷子),(talk,講話)',
                'u':'(United State America(USA),美國),(use,用)',
                'v':'(vote,投票),(very,很(會搭配形容詞EX:very good))',
                'w':'(wood,木頭),(weary,疲倦)',
                'x':'(xylophone,木琴),(xoxo,嗖(狀聲詞))',
                'y':['yoyo:溜溜球','you:你'],
                'z':'(zip code,郵政編碼),(zoom,飛漲)',}
        a=input("(a~z)?>")
        n=dictionary.get(a)
        print(n)
        if a not in dictionary:
            print("小鬼，查別的字典or")
            new=input('是否新增此單字??(yes or no)')
            if new == 'yes':
                item=input('name(第一個字)>')
                money=input('要這樣放"(英文字,中文意思)"')
                food2={n:[item,money],}
                dictionary.update(food2)
                print(dictionary)
    elif abc == 3:
        apron=input("apron?>")
        if apron == "停機坪":
            i=0
            print("yes,good job")
            i+10
            bomb=input("bomb?>")
            if bomb == "炸彈":
                print("yes,good job")
                i+10
                cc=input("CC+?>")
                if cc == "一種程式":
                    print("yes,good job")
                    i+10
                    dic=input("dictionary?>")
                    if dic == "字典":
                        print("yes,good job")
                        i+10
                        eat=input("ate?>")
                        if eat == "吃":
                            print("yes,good job")
                            i+10
                            feet=input("foot?>")
                            if feet == "腳":
                                print("yes,good job")
                                i+10
                                good=input("good(英文字)?>")
                                if good == "great":
                                    print("yes,good job")
                                    i+10
                                    hot=input("hot?>")
                                    if hot == "熱":
                                        print("yes,good job")
                                        i+10
                                        ice=input("ice-cream?>")
                                        if ice == "冰淇淋":
                                            print("yes,good job")
                                            i+10
                                            java=input("java?>")
                                            if java == "一種程式":
                                                i+10
                                                print("yes,good job",i,"分")
                                            else:
                                                print("no,德",i,"分")

    elif abc == 4:
        for i in dictionary.keys():
            print(i)
    
        for i in dictionary.values():
            print(i)
    
        for i in dictionary.items():
            print(i)
    elif abc == 5:
        break
    else:
        print("輸入錯誤，重新輸入(1~6)")
