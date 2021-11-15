# -*- coding: utf-8 -*-

# ogrenci1 = "Recep"
# ogrenci2 = "Berat"
# ogrenci3 = "Onur"

# print(ogrenci1)
# print(ogrenci2)
# print(ogrenci3)
# print("---------")

ogrenciler = ["Ahmet","Mehmet","Veli"]

print(ogrenciler[1])
ogrenciler[0] = "Balık"
#ogrenciler.append("Ahmet")              # Yeni bir değer ekler.
#ogrenciler.remove("Ahmet")              # Ahmet ismi olanların kaydını siler.
print(ogrenciler)
print("--------------------------------------------------------")

# list constructor
sehirler = list(("Ankara","İstanbul","İzmir"))
print(sehirler)
print(len(sehirler))                     # sehirler listesi kaç elemandan oluşur?
print("--------------------------------------------------------")

# diğer fonksiyonlar
# print(sehirler.clear())                  # sehirler listesini temizler
# print("Ankara sayısı = " + str(sehirler.count("Ankara")))
# print("Ankara indexi = " + str(sehirler.count("Ankara")))
sehirler.pop(1)                         # 1. indexi sildi
sehirler.insert(0, "Çorum")             # 0. indexe veri ekledik
# sehirler.reverse()                    # listeyi ters çevirdik
print(sehirler)
print("--------------------------------------------------------")

sehirler2 = sehirler                    # data eşitlenir ve herhangi birisi değişse bile diğeri de değişir.
sehirler2[0] = "İzmir"
print(sehirler2)
print(sehirler)
print("--------------------------------------------------------")




sehirler3 = sehirler.copy()             # eşitlemez sadece kopyalar.

sehirler2 = sehirler
sehirler2[0] = "Sivas"



print(sehirler2)
print(sehirler)
print(sehirler3)
print("--------------------------------------------------------")

sehirler.extend(sehirler3)                       # 2 listeyi birbirine ekler.
sehirler.sort()                                  # verileri a-z sırasına göre sıralar. (z-a için sehirler.reverse yaparız)
print(sehirler)














































