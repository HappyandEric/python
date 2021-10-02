total=0
a=0
h=0
l=100
scores=[]
s=int(input("student?>"))
for i in range(s):
    score=int(input("score?>"))
    scores.append(score)
for i in range(s):
    total=scores[i]+total
    if scores[i]>h:
        h=scores[i]
    if scores[i]<l:
        l=scores[i]
a=total/s
print(a)
print("hightest:",h)
print("losest:",l)
