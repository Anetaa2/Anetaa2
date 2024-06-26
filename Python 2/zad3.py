# opis kroku




import math


#1 wczytaj  zmienne
a = int(input("podaj pierwsza zmiennna"))
b= int(input("podaj druga zmienna"))

#oblicz i wypisz ich sume
c=a+b
print("Suma a + b = ",c)

#2 oblicz i nnapisz ich ruznice
d=a-b
print("roznica a - b =",d )
#3 oblicz i napisz ich iloczyn
e=a*b
print("iloczyn  a* b = ",e)

#4 oblicz i napisz ich iloraz
f=a/b
print("iloczyn a / b",f)
#5 oblicz i napisz pierwiastek z a + b 
g=math.sqrt(c)
print("pierwiastek sumy a + b ",g)
#6 oblicz i napisz a do potegi b i b do potegi a
h = math.pow(a , b )
print("a do ptegi b ",h)
j=math.pow(b,a)
print("b do potegi a ",j)