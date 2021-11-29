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

print('Информатика:')
inf=vv(inf)
inf1=set(inf)

print('Физика:')
ph=vv(ph)
ph1=set(ph)

print(math1)
print(inf1)
print(ph1)

