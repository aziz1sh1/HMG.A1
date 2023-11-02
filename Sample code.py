#romve this sign (##) after download the code file
# Create a text file
file = open ("1.txt",'w+')
# Time function
import time
from datetime import date
print ("              ")
# Genar random number
import random
n = random.randint(10,900)
print ("\n")
print("\tRef no.",n,"HMG    .Date",date.today())
# write in file
print  ("\n", file =file)
print("Ref no", n,"HMG        .Date",date.today(), file = file)
print  ("******************************************\n", file =file)
print("This pogram is used to calculate  ", file = file)
print("chemical properties based on your entry",file = file)
print ("__________________________________________________",file =file)
# Write on main console
print("*************************************************")
print("*\tThis pogram is used to calculate        *")
print("*\tchemical properties based on your entry *")
z ="_________________________________________________"
print (z)
print ("                  *WARANING*\n" )
print ("\tyou can Enter a numeric value")
print ("\twithout entering alphabet or unit ")
print ("\tdo not enter blank or 0 value ")
print ("\tsame value may give zero results ")
print (z,'\n')
va1 = 12
va2 =4

# Return on empty entery
##while True:
##    va1 = (input('Enter HOMO  '))
##    if va1.strip() != '':
##        print(va1)
##        break
# warning Caution for zero

##if va1 == '0':
##    print ('inoperative value of HOMO')
##else:
##       print ("")

# Return on empty entery
##while True:
##    va2 = (input('Enter LUMO  '))
##    if va2.strip() != '':
##        print(va2)
##        break
# warning Caution for zero

##if va2 == '0':
##    print ('inoperative value LUMO')
##else:
##         print ("")
# Waring for same value
##if va1 == va2:
##    print ("Homo and lumo must not be same ")
    

# calculation of first energy gap
va1 = float(va1)
va2 = float(va2)
va3 = (va1-va2)
print("Homo Value",va1, file =file)
print("Lumo Value",va2, file =file)
print ("__________________________________________________",file =file)

print ("\t1.First energy gap",va3, "\n")
print("\t1.First energy gap",va3, file =file)
vai = (-va1)
# calculation of Ionization energy gap
print ("\t2.Ionization energy", vai, "\n")
print("\t2.Ionization energy",vai, file =file)
ea = (-va2)
print ("\t3.Electron affinity",ea, "\n")
print ("\t3.Electron affinity",ea, file =file)
h = (vai-ea)/2
print ("\t4.Hardness","\t",h, "\n")
print ("\t4.Hardness","\t",h, file =file)
cp = -(vai+ea)/2
print ("\t5.Chemical potential",cp, "\n")
print ("\t5.Chemical potential",cp, file = file)
s = 1/h
print ("\t6.Softness",s, "\n")
print ("\t6.Softness",s, file =file)
e = (cp*cp)/(2*h)
print ("\t7.Electrophilicity index",e, "\n")
print ("\t7.Electrophilicity index",e, file =file)
en =0.5*(vai+ea)
print ("\t8.Electronegativity",en,"eV")
print ("\t8.Electronegativity",en, "eV", file =file)
print ("__________________________________________________",file =file)
print("The package name is HMG.A1, is developed in Python.",file =file)
print ("**************************************************",file =file)

# calculation end
file.write ("HMG.A1")
file.write (" results depends on your input\n")
file.write ("credit goes to Muhammad Aziz\t et.al ")
print(file.readline())

print (z)

##input("Save your file ,Enter to exit")
print ("__________________________________________________")
print("The package name is HMG.A1, is developed in Python.")
print ("**************************************************")

file.close()
# define path
import os
p = path = ("1.txt")
os.system(path)
# prompt file
file = open ("1.txt")
# code written by Muhammad Aziz
#email aziz1sh@hotmail.com
