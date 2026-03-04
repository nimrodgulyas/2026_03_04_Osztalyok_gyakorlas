from auto import Auto
import random

auto1 = Auto("Toyota", "Corolla", 2015)
auto2 = Auto("Ford", "Focus", 2018)
auto3 = Auto("Audi", "E-Tron GT", 2021)
auto4 = Auto("Ford", "Mustang", 2005)

# print(auto1)
# print(auto2)

# auto1.gyorsit(150)
# print(auto1)
# auto1.gyorsit(150)
# print(auto1)
# auto1.fekez(100)
# print(auto1)
# auto1.fekez(150)
# print(auto1)

autok = [auto1, auto2, auto3, auto4]
for auto in autok:
    print(auto)

print("Gyorsít\n")
for auto in autok:
    auto.gyorsit(random.randint(30, 150))
    print(auto)

#4. atlageletkor
autok_szama = len(autok)
ossz_eletkor = 0
for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    ossz_eletkor += kor

atlag_eletkor = ossz_eletkor / autok_szama
print(f"Az autók átlagéletkora: {atlag_eletkor} év")

#5. legoregebb auto
#A version: FAVÁGÓ
legidosebb_auto = None
legidosebb_auto_kora = 0

for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    if kor > legidosebb_auto_kora:
        legidosebb_auto_kora = kor
        legidosebb_auto = auto

print(f"A legidősebb autó kora: {legidosebb_auto_kora}, adatai: {legidosebb_auto}")
