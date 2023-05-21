#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 17:52:55 2023

@author: rajsah
"""

"""
This code open the files OSZICAR file in subdirectoris in the list 2. The directories
in the list two are subdirectories of the list1
Then code finds the line that has E0 in it
Splits the line and append the required value to the temp list
Then finally writes the values to a txt file for each directories in the list1
"""
# list1 is the directory that has subdirectories in the list2
#list1=['grid-m222','grid-m333','grid-m444','grid-m555','grid-m666']
list1=['Encut-test']
list2=['400','450','500','550','600','650','700','750','800']
#list2=['400']
data=[]
temp=[]
pattern='E0'
for xyz in list1:
        for abc in list2:
                with open("./"+str(xyz)+"/"+str(abc)+"/OSZICAR") as filetemp:
                        for line in filetemp:
                                if pattern in line:
                                        a=line.split()
                                        #temp.append(str(xyz))
                                        temp.append(str(abc))
                                        temp.append(str(a[4]))

                data.append(temp)
                temp=[]
                filetemp.close()
        with open("./"+str(xyz)+".txt",'w') as f1:
                f1.write(str('Encut'))
                f1.write("\t")
                f1.write(str('E0'))
                f1.write("\n")
                for x in data:
                        f1.write(str(x[0]))
                        f1.write("\t")
                        f1.write(str(x[1]))
                        f1.write("\n")
        f1.close()
        data=[]