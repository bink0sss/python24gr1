# def suma(x,y):
    # return(x+7)
# print(suma(2,3))
# 
# PI = 3.14
# Oblicz pole koła pi*r^2  // pi*r*r
# def pole_kola(r:float) -> float:
    # """
    # Funkcja licząca pole koła
    # """
    # x=15
    # return PI *r**2
# print(f"Pole koła wynosi :  {pole_kola(5)}")
# print(f"Pole koła wynosi :  {pole_kola(5.1)}")
# print(f"Pole koła wynosi :  {pole_kola(5.2)}")
# 
# def witaj(imie:str, powitanie:str = "Cześć")->str:
    # return f"{powitanie}, {imie} jestes na PW."
# print(witaj(powitanie = "Cześć", imie = "Kuba"))
# 
# def silnia(n:int)->int:
    # if n==0:
        # return 1
    # return n * silnia(n-1)
# print(silnia(5))
# 
# def pi()->float:
    # return 3.14
# print(pi())
# 
# def suma_wielu(*args)->int:
    # return sum(args)
# 
# print(suma_wielu(1,23,312,312,213,432))
# 
# Funkcja filtrujaca liczby patrzyste
# 
# def parzyste(*lista):
    # return [x for x in lista if x % 2 == 0]
# print(parzyste(1,2,3,4,5,6,7,8,9,10))
# 
def filtruj_parzyste(Liczby:list[int]) -> list[int]:
    return [num for num in Liczby if num%2 == 0]
print(filtruj_parzyste([10,11,12,13,14,15]))