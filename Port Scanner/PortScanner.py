import socket, os
from sys import path_importer_cache



Server = input("IP ADRESI : ")
ServerIp = socket.gethostbyname(Server)
tip = int(input("Otomatik icin 1, Manuel icin 2 : "))

if tip == 1:
    for port in range(1,65536):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((ServerIp,port))
        if result == 0:
            print("DIKKAT PORT {} ACIK!".format(port))
    sock.close()
if tip == 2:
    manualPort = int(input("Port numarasi girin : "))
    manualSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    manualResult = manualSock.connect_ex((ServerIp, manualPort))
    if manualResult == 0:
        print("DIKKAT ACIK PORT!")
    else:
        print("PORT KAPALİ ")
    manualSock.close()
    
    
#           Recep MERT PortScanner 