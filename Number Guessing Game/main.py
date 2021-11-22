import os
import time
from random import randint

print("Merhaba dostum, rastgele sayı üretmeye hazır mısın?")
number2 = int(randint(0,100))

while True:
    try:
        number1 = int(input("Lütfen 0 ile 100 arasında bir sayı seçiniz : "))
        if number1 not in range (0,100):
            print("Hey dostum sana dediğim aralıkta bir sayı seçmelisin!")
        if number1 == number2:
            print("\nBULDUN DOSTUM BRAVO SANA!")
            break
        elif number1 < number2:
            print("\nBiraz daha büyük rakamlar denemelisin :)")
        elif number1 > number2:
            print("\nBiraz daha küçük rakamlar denemelisin :)")
    except (ValueError, NameError, SyntaxError):
        print("\n\nDostum sayının ne olduğunu bilmiyor musun?!?!")

time.sleep(5)
os.system("exit")