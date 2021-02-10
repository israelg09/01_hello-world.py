# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:43:42 2021

@author: idga-
"""
lista1=['R1','R2','R3',"S1","S2","S3"]
swicthes=[ ]
routers=[ ]
for i in lista1:
    if "R" in i:
        routers.append(i)
    if "S" in i:
        swicthes.append(i)
for i in lista1:
    if "S" in i:
        print(i)
    elif "R" in i:
        print(i)
    else:
        print ("error")

