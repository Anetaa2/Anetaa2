import math
 #1 napisz program ktury obliczy pole kola
r=int(input("promien kola"))

# sprawdzanie czy podany projekt jest dodatni
if r>0:
    print("promien jest dodatni")
    pi = math.pi
    print("to jest pi z math ", pi)
    obw=2* pi*r
    pole= math.pow( pi*r,2)
    print("pole to ", pole)
    print("obw to ", obw)
else:
    print("promien jest nie poprawny")

# jakas zmiana

#2 napisz program ktury obliczy obwud kola

