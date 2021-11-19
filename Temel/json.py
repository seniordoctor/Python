# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 21:35:31 2021

@author: docto
"""

import json

data = '{"firstName":"Recep","lastName":"Mert"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
        "firstName":"Recep",
        "email":"recepmert@gmail.com"
        
    }

customerJson = json.dumps(customer)                    # customer'ı json'a dönüştürür.
print(customer)

print(json.dumps("Recep"))                              # json'a dönüştürdük.