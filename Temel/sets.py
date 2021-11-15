# -*- coding: utf-8 -*-
                            # setler index sırası yoktur kendisine göre sıralar.


studentsSet = {"Recep","Berat","Kadir","Mahmut"}  #listeyi değiştiremeyiz.
studentsSet2 = set("AA","BB","CC")          # set oluşturma farklı yöntem


print(studentsSet)


for student in studentsSet:           # Alt alta yazacaktır.
    print(student)
    

print("Recep" in studentsSet)   
print("recep" in studentsSet)         # key sens. olduğu için false döndürür.

if "Recep" in studentsSet:
    print("Giriş yapabilirsiniz.")
    
studentsSet.add("Ayşe")             # listeye ekleme yaptık.
print(studentsSet)

studentsSet.update(["Ali","Kerim","Behzat"])   # listeye update ile ekleme yaptık.
print (studentsSet)

studentsSet.remove("Kerim")                 # kerimi tablodan sildik ve 7 kişi kaldı
#studentsSet.remove("recep")                 # key sens olduğu için Recep olarak yazmamız gerekiyor HATA VERDİ
print(len(studentsSet))

studentsSet.discard("Kerim")                # Kerim tabloda yok ama HATA VERMEYECEK. (discard hata vermez)
print(len(studentsSet))

x = studentsSet.pop()                       # tablodan bir elemanı siler
print(len(studentsSet))
print(studentsSet)

x = studentsSet.clear()                       # tabloyu siler
del studentsSet                                 # HATA VERİR del ile tamamen sildik







