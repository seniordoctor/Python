# -*- coding: utf-8 -*-

f = open("musteriler2.txt")          # w --> eğer dosya yoksa oluşturur      x --> dosya oluştur demek,varsa hata verir
print(f.read())   # ilk 10 karakteri okur
print("-----------------------------------------------------")
print(f.readline())     # satır satır okur (1.satır)
print(f.readline())     # 2. satır
# r Read, a append, w write, x create

for l in f:
    print(l)
    
f.close()


fileToAppend = open("ogrenciler.txt","w")   # yoksa dosyayı benim için oluşturdu.
fileToAppend.write("Hasan")                 # w --> üzerine yazar eskisi silinir.
fileToAppend.write("\n")
fileToAppend.close()


#%%
import os                       

if os.path.exists("ogrenciler.txt"):            # eğer ogrenciler.txt varsa sil.
    os.remove("ogrenciler.txt")

else:
    print("Dosya yok")
    
# os.remove("ogrenciler.txt")                 # ogrenciler.txt'yi siler.


os.rmdir("empty")                   # empty klasörü var ise siler.











































