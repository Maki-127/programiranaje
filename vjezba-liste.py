"""
moja_lista = [10,20,30]

prvi_element = moja_lista[0]

print (prvi_element)

moja_lista.append(40)

print (moja_lista)

dio_liste = moja_lista[1:3]

print (dio_liste)


#zadatak 2
voce =["jabuka", "banana", "kruska"]

prvi_element = voce[0]

voce.append("naranca")

print(voce)

"""

# 2D liste
# Ovo eje 2D lista (3 retka, 3 stupca)
ormar = [
    ["majica", "hlače", "suknja"],   # 0. redak (polica)
    ["hlace", "carape", "remen"],    # 1. redak 
    ["jakna", "cipele", "cizme"]     # 2. redak
] 

print(f"Hlače ? {ormar[0][1]}")

print(ormar [1][0])
print(ormar [1][1])
print(ormar [2][1])


for odjeca in ormar:
    print(odjeca[1])

for redak in ormar:
    print (f"Sadržaj retka: {redak}")

    for element in redak:
        print (f"Elemnt:  {element}")


def pronadji_broj (lista, broj):
    print(f"Tražim broj {broj} u listi {lista}")
    
    prelkidac = False

    for element in lista:
        if element == trazeni_broj:
            prelkidac = True
            break
    else:
        prelkidac = False


    if prelkidac:
        print (f"Broj {broj} je na listi.")
    else:
        print (f"Broj {broj} nije na listi.")


lista = [10, 20, 30, 40, 50]
trazeni_broj = 30
pronadji_broj (lista, trazeni_broj)

print("\n--- Bonus Izazov: Priprema za projekt ---")
# Ovo je struktura koju smo dobili u Fazi 3
rezultati = [('hlapić', 15), ('gita', 12), ('majstor', 10)]

# 1. Kreiramo novu listu. Njen prvi element je lista koja predstavlja zaglavlje.
tablica = [['Riječ', 'Frekvencija']]
print(f"Tablica na početku (samo zaglavlje): {tablica}")

for rezultat in rezultati:
    lista_elementa = list(rezultat) # Ovo će stvoriti ['hlapić', 15]
    tablica.append(lista_elementa)

print(f"Tablica nakon dodavanja rezultata: {tablica}")

for red in tablica:
    print(red)
