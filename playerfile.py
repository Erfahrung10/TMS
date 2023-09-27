#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 18:17:13 2023

@author: dai
"""

import re
with open("player.txt") as fh:
    for line in fh:
        line=line.rstrip("\n")
        m=re.match("2.*g$", line)
        if m!=None:
            print(line)
    