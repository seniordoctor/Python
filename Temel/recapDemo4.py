# -*- coding: utf-8 -*-

ogrenciler = ["Recep","Kürsat","Eren","Enes","Kerem"]

fileToAppend = open("ogrenciler","a") # a--> append

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")

fileToAppend.close()
    