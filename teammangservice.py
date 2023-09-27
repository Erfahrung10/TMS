#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:51:50 2023

@author: dai
"""

'''To accept playerid, player name, specialization, charges, team name from user and store it 
in a list of Player objects,
Display total charges teamwise.
add a new team, delete the team, modify charges by id 
At the time of exit store, it in a file player. txt 
(Write Player class to store details of each Player)
200 Virat kohali Betsman 4000000 Mumbai Indians
402 DhoniBatsman|4300000/Chennai super king
303 UndejalBowler3500000 Mumbai Indians
204 Ashwin Batsman| 300000 Chennai super king
(note; Use Player.txt created at the time of exit) 
accept pattern from user to find all 
lines starts with 2 and ending with "g" and diaply detils
of all the players with the given skill, otherwise display Not found'''

class Player:
    cnt=0
    def __init__(self,pname="",special="",charg=1000,tname=""):
        Player.cnt=Player.cnt+1
        self.__pid=Player.cnt
        self.__pname=pname
        self.__special=special
        self.__charges=charg
        self.__tname=tname
        
    def __str__(self):
        return f"ID: {self.__pid} Name: {self.__pname} Specialization: {self.__special} Charges: {self.__charges} Team Name: {self.__tname}"

    #Setter Methods
    def set_pid(self,pid):
        self.__pid=pid
    def set_pname(self,pname):
        self.__pname=pname
    def set_special(self,special):
        self.__special=special
    def set_charges(self,charges):
        self.__charges=charges
    def set_tname(self,tname):
        self.__tname=tname    
        
    #Getter Methods
    def get_pid(self):
        return self.__pid
    def get_pname(self):
        return self.__pname
    def get_special(self):
        return self.__special
    def get_charges(self):
        return self.__charges
    def get_tname(self):
        return self.__tname
    
  

    
    
    
    
    

