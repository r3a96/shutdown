#!/usr/bin/python3



import os
from time import *
print('\033[94m')
r = input("Do yo Want to shutdown your system ? y/N ")
secend = 0 ;
cunt = 0 ;

if (r == "y" ):
    io = input("HOw many time befor shut down / secend  example 3000 == 50 minute ------ > ")
    io = int(io)
    print("time is ",io)
    while secend != io:
        io -= 1 ;
        print('\033[91m',io,"\033[94mTo shutdown ")
        sleep(1)
        cunt += 1 ;
        if cunt < 10:
            os.system("clear")
            cunt = 0 ; 
        
    a = os.system("shutdown -P")
    print()
    print()
    sleep(3)
    print ("Your Sytem Shuting down in 2 minuts  by by ")
    print ()
    can = input("if you cancell shutdown please press key c ")
    if (can == "c"):
        os.system("shutdown -c")
        print("cancelled shuting down your system ... ")

    print()
    
else:
    sleep(2)
    print ("Ok sir good by")

 
