#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:20:02 2023

@author: dai
"""

from teamservices import *
ch=0
while ch!=6:
    ch=int(input("""
    1. Display Total Charges Teamwise
    2. Add a new Team
    3. Delete the Team
    4. Modify charges of Player by ID
    5. Display All
    6. Exit
    Choice: """))
    match ch:
        case 1:
            d=totalcharges()
            for k,v in d.items():
                print(f"{k}  :  {v}")
        case 2:
            tname=input("Enter a Team Name: ")
            addnewteam(tname)
            
        case 3:
            tname=input("Enter a Team Name: ")
            status=deletebyteam(tname)
            if status==1:
                print("Team Deleted Successfully")
            elif status==2:
                print("Team Found but not Deleted")
            else:
                print("Team Not Found")
        case 4:
            pid=int(input("Enter a Player ID: "))
            charg=int(input("Enter charges: "))
            status=modifybyid(pid,charg)
            if status==1:
                print("Player charges Modify Successfully")
            elif status==2:
                print("Player Found but charges not Modified")
            else:
                print("Player Not Found")
        case 5:
            displayall()
        case 6:
            with open("player.txt",'w') as fh:
                for v in playerinfo.values():
                    line=str(v.get_pid())+"|"+v.get_pname()+"|"+v.get_special()+"|"+str(v.get_charges())+"|"+v.get_tname()+"\n"
                    fh.write(line)
        
            
            
            