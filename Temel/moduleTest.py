# -*- coding: utf-8 -*-

# import matematikModule 

# matematikModule.topla(1, 2)
# matematikModule.carp(2, 3)

#                               KISALTMA YAPABİLİRİZ
import matematikModule as mm

mm.topla(2, 3)
mm.carp(4, 4)

#----------------------------------------------------------

print(mm.customer["firstName"])
print(mm.customer["lastName"])

#----------------------------------------------------------

from matematikModule import topla

topla(2,3)

#----------------------------------------------------------
from matematikModule import customer

print(customer["firstName"])