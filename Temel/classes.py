# -*- coding: utf-8 -*-
#%%
class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
                                            # self = class'ın kendisini referans ediyor.
matematik = Matematik(2,78)
matematik2 = Matematik(3,76) 
print("Toplam = " + str(matematik.topla()))
print("Toplam = " + str(matematik2.topla()))
   
#%%     PROPERTY

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age 
        
        
person1 = Person("Recep","Mert",20)
print(person1.firstName)       



class Worker(Person):
    def __init__(self,salary):
        self.salary = salary 

        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
        
ahmet = Worker()

mehmet = Customer()
     
        
