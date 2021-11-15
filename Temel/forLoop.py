

sehirler = ["Ankara","İstanbul","İzmir"]
# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])

#%% For Intro
for sehir in sehirler:              # sehir takma isim olacak mesela i gibi
    if sehir != "Ankara":
        print(sehir ,"için kod = ", sehir[0:3])
    print("*****************")
    
#%% For range
for x in range(100):                # range 0'dan 100'e kadar çalışır fakat 100 dahil değil.
    print(x+1) 
    

for x in range(1,10,2):             # 1'den başla 10'a kadar 2'şey artış
    print(x)
    

