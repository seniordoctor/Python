# -*- coding: utf-8 -*-


#%%
sehir = "Ankara"

sonuc = sehir.upper()
print(sehir.endswith("a"))                  # a ile mi bitiyor --> True
               
#%%                      # fonksiyon kullanımı
def selamVer(isim = "Ziyaretçi"):                             # isim = "Ziyaretçi" ile default parametre giriyoruz.
    print("Merhaba", isim)

selamVer("Recep")
selamVer("Enes")
selamVer("Kürşat")
selamVer("Eren")
selamVer()


def selamVer2(isim = "Ziyaretçi", soyIsim = "Arkadaş"):     # eğer bir değişken veriyorsak default değer belirtmek zorundayız.
    print("Merhaba", isim, soyIsim)

selamVer2()
selamVer2("Recep")
selamVer2("Recep", "Mert")


#%%
def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2,3)

print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2                      # fonksiyon yapmış olduk.

print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2 

print(x(4,5))













