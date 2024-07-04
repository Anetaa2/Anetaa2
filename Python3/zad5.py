
import math
 # Msc zer funkcji 

def calculate_delta(a,b,c):
    delta = 0
    b_pow_2 =  math.pow(b,2) 


    delta= b_pow_2-(4*a*c)
    print("delta to ",delta)
    return delta

def calucate_x1(b,delta,a):
    pass

def calucate_x2(b,delta,a):
    pass

def show_results(x1, x2):
    pass


#1podaj wspolczynniki ruwnania kwadratowego...
a=int(input("podaj parametr a \n"))
b=int(input("podaj parametr b \n"))
c=int(input("podaj paraetr c \n"))

#2 oblicz delte
delta = calculate_delta(a,b,c)

#3 oblicz pierwsze miejsce zerowe e
x1=calucate_x1(b, delta,a)

#4 oblicz drugie miejsce zerow
x2=calucate_x2(b,delta,a)
#5 wypisz wyniki
show_results(x1, x2)
