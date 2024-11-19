# ### 1. Wyświetlanie aktualnego stanu rezerwacji miejsc
# - **Typ danych:** lista (`seats`)
# - **Opis:** Używamy listy `seats`, która przechowuje informacje o rezerwacjach miejsc. Jeśli miejsce jest wolne, w liście znajduje się wartość `None`. Jeśli miejsce jest zarezerwowane, w liście przechowywane jest imię osoby, która je zarezerwowała.
# - **Funkcja:** `print_seats(seats)` wyświetla aktualny stan wszystkich miejsc, informując, które z nich są wolne, a które są zarezerwowane oraz przez kogo.

def print_seats(seats):
    for index, seat in enumerate(seats):
        if seat is None:
            print(f"Miejsce {index +1 }: Wolne")
        else:
            print(f"Miejsce {index+1}: Zarezerwowane prez: {seat}")
seat = [None, "Damian",None,"Jacek","Kuba",None]
print(print_seats(seat))


