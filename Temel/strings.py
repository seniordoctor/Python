text1 = "Hello World" #string

print(text1[0])             # 0. indexi alır.
print("--------")

print(text1[2:5])           # 2'den 5'e kadar (5 dahil değil)
print("--------")

newText = text1[:2]         # baştan başla 2'ye kadar

print(newText)
print("--------")
print("--------")


# len
print(len(text1))           # len metin kaç karakterden oluşuyorsa onu verir.

newText2 = text1[len(text1)-1:len(text1)]

print(newText2)
print("--------")
print("--------")


# Lower Upper
print(text1.upper())
print(text1.lower())
print("--------")
print("--------")


# replace
print(text1.replace("o", "ö"))          # harf değiştirmek için kullanılır.
print("--------")
print("--------")


# split ve strip
info = "     Recep Mert 20 Istanbul".strip()
print(info.split())                 # Girilen bilgileri boşluğa göre ayırır.
print(info.split(" "))              # Girilen bilgileri bir boşluğa göre ayırır
                                    # .strip ile gereksiz boşlukları temizledi.
 

# input
ad = input("Adınız?")               # Klavyeden girdi yapmak için input kullan
