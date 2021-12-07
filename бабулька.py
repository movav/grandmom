def vv(a):
    i=True
    while i:
        i=input()
        if i: a.append(i)
    return a

print('Списки олимпиадников(Физика, Информатика, Математика):')
ph=[]
inf=[]
math=[]

print('Математика:')
math=vv(math)
math1=set(math)
m=list(math1)
sm=len(m)

print('Информатика:')
inf=vv(inf)
inf1=set(inf)
i=list(inf1)
si=len(i)

print('Физика:')
ph=vv(ph)
ph1=set(ph)
p=list(ph1)
sp=len(p)


print('Математика:',math1)
print('Кол-во участников:',sm)
print('Информатика',inf1)
print('Кол-во участников:',si)
print('Физика',ph1)
print('Кол-во участников:',sp)

povt=math1&inf1&ph1
print('Кол-во участников, участвующих во сех трёх олимпиадах:',len(povt))