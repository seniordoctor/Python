#       km'yi mile çevirmek için yapılan bir programdır
#       1 km = 0,621371192 mil 

donusumOrani = 0.621371192
km = int (input("Kaç km?  "))

mil = km * donusumOrani

print(str(km) + " Km = " +str(mil)+ " eder")
