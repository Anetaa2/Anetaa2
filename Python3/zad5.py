
import math
 # Msc zer funkcji 

def calculate_delta(a,b,c):
    delta = 0
    b_pow_2 =  math.pow(b,2) 

    delta= b_pow_2-(4*a*c)
    print("delta to ",delta)

    if delta==0:
     print(" 1miejsce zerowe")
     return 0
    elif delta < 0:
        print("delta < nie ma rozwiazan") 
        return 0

    return delta

def calucate_x1(b,delta,a):
    delta_sqrt=math.sqrt(delta)
    x1=(-b- delta_sqrt)/2*a
    return x1

def calucate_x2(b,delta,a):
    delta_sqrt=math.sqrt(delta)
    x2=(-b+delta_sqrt)/2*a
    return x2 

def show_results(x1, x2):
    print("x1= ", x1)
    print("x2= ", x2)

#1podaj wspolczynniki ruwnania kwadratowego...
a=int(input("podaj parametr a \n"))
b=int(input("podaj parametr b \n"))
c=int(input("podaj paraetr c \n"))

#2 oblicz delte
delta = calculate_delta(a,b,c)

if delta != 0:
    #3 oblicz pierwsze miejsce zerowe e
    x1=calucate_x1(b, delta,a)

    #4 oblicz drugie miejsce zerow
    x2=calucate_x2(b,delta,a)
    #5 wypisz wyniki
    show_results(x1, x2)