nev = ["Martin","Géza","Niki","Csilla"]

szul_ev = [2000,321234,500,0]

kor = []

for i,j in zip (nev,szul_ev):
    print(i," ",j)
    print(i," ",2022-j)
    kor.append(2022-j)
print(kor)

legoregebb = kor[0]
for i in kor:
    if i > legoregebb:
        legoregebb = i

print(legoregebb)

legfiatalabb = kor[0]
for i in kor:
    if i < legfiatalabb:
        legfiatalabb = i

print(legfiatalabb)

oregek = []
fiatalok = []
for i,j in zip(nev,kor):
    if j == legoregebb:
        print(i,j)
        oregek.append(i)

for i,j in zip(nev,kor):
    if j == legfiatalabb:
        print(i,j)
        fiatalok.append(i)

print(oregek)
print(fiatalok)

#len a lista hossazáig len(lista) lista hossza
#max(lista neve)

t = [5,3,6,2,1]
maxElem = t[0]
for i in range(1,len(t)):
    if t[i] > maxElem:          #minimumra csak a kacsacsőrt kell átírni <-re
        maxElem = t[i]
        maxhely = i

print(maxElem,maxhely)

t = [3,8,2,4,5,1,6]
osszeg = 0
for num in t:
    osszeg = osszeg +num

print("Összeg:",osszeg)

t = [3,-8,-2,-4,5,11,6]

count = 0
for num in t:
    if num < 0:
        count = count+1

print("Negatív számok:",count)

#eldöntés hogy van e a listában a ker (itt pl 7)
t = [3,8,2,4,5,1,6]

n = len(t)
ker = 7
i = 0
while i < n and t[i] != ker:
    i = i+1

if i < n:
    print("Van ilyen:", ker)

else:
    print("Nincs ilyen elem:",ker)

#kiválasztás keresés = ker

t = [3,8,2,4,5,1,6]
n = len(t)
ker = 1

i = 0
while t[i] != ker:
    i = i+1

print("Hányadik helyen van:", i+1)

#kiválogatás
#szétválogatás

a = [3,8,2,4,5,1,6]
b = []
#c = []

for elem in a:
    if elem < 5:
        b.append(elem)

    #else:
        #c.append(elem)

print(b)
#print(c)
















































