import os
import random
print("Dünya'nın en adaletli zarına hazır mısın?")
repeat = True                           # programın tekrar edebilmesi için repeat kullanıyoruz
from random import randint

while repeat:
    print("Zarlar yuvarlanıyor!\n")
    number2 = int(randint(1,6))
    print("--------------->", number2 ,"<---------------")
    print("\nTekrar oynamak için e veya evet yazın.")
    repeat = ("e" or "evet") in input().lower()