# -*- coding: utf-8 -*-

sozluk = {
        "book" : "kitap",
        "table" : "masa"
    }

sozluk2 = dict(kitap = "book", masa = "table")

sozluk["book"] = "kitap 1"          # olan değeri değiştirmek
sozluk["pencil"] = "kalem"          #yeni değer eklemek
del(sozluk["book"])                 # sozluk'teki book'u silecek.
print(sozluk)
print("--------------------------------------------")
print(sozluk2)




