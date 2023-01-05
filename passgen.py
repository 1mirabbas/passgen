#!/usr/bin/env python3
# Version: v1.0.0 @2023

###########################################
#    Author: Mirabbas Aghalarov           #
#    Youtube: mirabbasaghalarov           #
#    Instagram: 1mirabbas                 #
#    Linkedin: mirabbasagalarov           #
#    Email: mirabbasagalarov0@gmail.com   #
###########################################

import argparse
import os
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("-o", help="output file", dest='output')



args = parser.parse_args()
output = args.output

def prRed(skk):print("\033[91m{}\033[00m".format(skk))
def prCyan(skk):print("\033[96m{}\033[00m".format(skk))
def prGreen(skk):print("\033[92m{}\033[00m".format(skk))
def prMagenta(skk):print("\033[35m{}\033[00m".format(skk))
def prBlue(skk):print("\033[34m{}\033[00m".format(skk))





prCyan('''
 _ __   __ _ ___ ___  __ _  ___ _ __  
| '_ \ / _` / __/ __|/ _` |/ _ \ '_ \ 
| |_) | (_| \__ \__ \ (_| |  __/ | | |
| .__/ \__,_|___/___/\__, |\___|_| |_|
|_|                  |___/            
   Author: Mirabbas Aghalarov                           
''')
prGreen('''
1)Normal
2)Special
3)Simple
''')
try:
    value = input('Please select the mode: ')
    value=int(value)
except ValueError:
    prRed('Error')

if value ==1:
   mini=int(input('min length: '))
   maxi=int(input('max length: '))
   
   if mini > maxi:
      print('min length must smaller or same as with max length')
      os.sys.exit()
   if output is None:
      chrr=input('characters: ')
      for n in range(mini, maxi + 1):
         for xs in itertools.product(chrr, repeat=n):
               chars = ''.join(xs)
               print(chars)
   else:
      with open(output, "a") as f:
         chrr=input('characters: ')
         for n in range(mini, maxi + 1):
            for xs in itertools.product(chrr, repeat=n):
               chars = ''.join(xs)
               f.write(chars + '\n')

elif value ==2:
   
   print("Please enter 5 string, 5 number information about the target")
   s1=input('string-1: ')
   s2=input('string-2: ')
   s3=input('string-3: ')
   s4=input('string-4: ')
   s5=input('string-5: ')

   lst1=[s1,s2,s3,s4,s5]

   n1=input('number-1: ')
   n2=input('number-2: ')
   n3=input('number-3: ')
   n4=input('number-4: ')
   n5=input('number-5: ')

   lst2=[n1,n2,n3,n4,n5]
   if output is None:

      for i in lst1:
         for j in lst2:
            print(i+j)

      for i in lst2:
         for j in lst1:
            print(i+j)

      for i in lst1:
         for j in lst2:
            for k in lst1:
                  print(i+j+k)

      for i in lst1:
         for j in lst1:
            for k in lst2:
                  print(i+j+k)

      for i in lst2:
         for j in lst1:
            for k in lst2:
                  print(i+j+k)

      for i in lst2:
         for j in lst1:
            for k in lst1:
                  print(i+j+k)


      for i in lst1:
         for j in lst2:
            print(i.capitalize()+j)

      for i in lst2:
         for j in lst1:
            print(i+j.capitalize())

      for i in lst1:
         for j in lst2:
            for k in lst1:
                  print(i.capitalize()+j+k)

      for i in lst1:
         for j in lst1:
            for k in lst2:
                  print(i.capitalize()+j+k)

      for i in lst2:
         for j in lst1:
            for k in lst2:
                  print(i+j.capitalize()+k)

      for i in lst2:
         for j in lst1:
            for k in lst1:
                  print(i+j.capitalize()+k)
   else:
      with open(output, "a") as f:

         for i in lst1:
            for j in lst2:
               f.write(i+j+'\n')

         for i in lst2:
            for j in lst1:
               f.write(i+j+'\n')

         for i in lst1:
            for j in lst2:
               for k in lst1:
                  f.write(i+j+k+'\n')

         for i in lst1:
            for j in lst1:
               for k in lst2:
                  f.write(i+j+k+'\n')

         for i in lst2:
            for j in lst1:
               for k in lst2:
                  f.write(i+j+k+'\n')

         for i in lst2:
            for j in lst1:
               for k in lst1:
                  f.write(i+j+k+'\n')

         for i in lst1:
            for j in lst2:
               m=i.capitalize()
               f.write(m+j+'\n')

         for i in lst2:
            for j in lst1:
               m=j.capitalize()
               f.write(i+m+'\n')

         for i in lst1:
            for j in lst2:
               for k in lst1:
                  m=i.capitalize()
                  f.write(m+j+k+'\n')

         for i in lst1:
            for j in lst1:
               for k in lst2:
                  m=i.capitalize()
                  f.write(m+j+k+'\n')

         for i in lst2:
            for j in lst1:
               for k in lst2:
                  m=j.capitalize()
                  f.write(i+m+k+'\n')

         for i in lst2:
            for j in lst1:
               for k in lst1:
                  m=j.capitalize()
                  f.write(i+m+k+'\n')
         
elif value ==3:
   name=input('string: ')
   number=int(input('max number length (ex-4404): '))
   if output is None:

      for i in range(1,number+1):
         a=i
         a=str(a)
         print(name+a)
   else:
      with open(output, "a") as f:
         for i in range(1,number+1):
            a=i
            a=str(a)
            f.write(name+a+'\n')
else:
   print('Please choose the mode properly ')