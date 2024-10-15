# Zadanie 1: Napisz program, ktory przypisze do zmiennych liczbę całkowitą i tekst, a następnie wypisze te dane na ekran

liczba = 10
tekst = "Hello, Python"

print(liczba, tekst)

# Zadanie 2: zadeklaruj zmienną z liczbą zmiennoprzecinkową i tekstem, a następnie wypisz oba elementy w jednym ciągu zdaniowym.

liczba2 = 3.14
tekst2 = "Wartość liczby pi to:" 
print(f"{tekst2} {liczba2}")
 
# Zadanie 3: Wypisz na ekranie sumę dwóch liczb oraz komunikat z wynikiem w formie: „Suma liczb 5 i 10 wynosi 15”.
liczba3 = 5
liczba4 = 10
suma = liczba3 + liczba4
print(f"Suma liczba {liczba3} i {liczba4} wynosi {suma}")
# Zadanie 4: Wczytaj od użytkownika dwie liczby i oblicz ich iloczyn, różnicę oraz iloraz.

number1 = float(input("Input first number: "))
number2 = float(input("Input second number: "))
product = number1 * number2
difference = number1 - number2
quotient = number1 / number2 if number2 != 0 else "Cannot divide by zero"
print(f"Product: {product}")
print(f"Difference: {difference}")
print(f"Quotient: {quotient}")
# Zadanie 5: Wczytaj ciąg znaków, który reprezentuje liczbę zmiennoprzecinkową, przekonwertuj go i oblicz pierwiastek kwadratowy z tej liczby.
import math
liczba_zmiennoprzecinkowa = 3.1414141


# Zadanie: Napisz program, który wczyta od użytkownika tekst, a następnie wypisze długość tego tekstu.