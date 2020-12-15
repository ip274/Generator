import random
import os
import time
import itertools as t

#this colors from:(twiiter@Xcodeone1)
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray


chars = "qwertyuiopasdfghjklzxcvbnm1234567890"


def logo():
    os.system("clear")
    print(G+'''
   _____                           _             
  / ____|                         | |            
 | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                twitter:@ip_274                                                                                
    ''')
    time.sleep(0.4)

logo()
print(G+"Options:")
print(G + "[01]- Unlimited list")
print(G + "[02]- Limited list")
print(G + "[03]- File length")
print(G + "[00]- Exit")

print("\n")
Option = str(input(C+"The service you want is? "))

def Unlimited():
    os.system("rm Unlimited.txt ")
    logo()
    print(G+"for help: ")
    print("[asdfghjklqwertyuiopzxcvbnm]")
    print("[1234567890]")
    print("[!@#$%^&*()_\\<>-*/+=]")
    print("\n")

    chars=raw_input(G+"chars here: "+ W)

    logo()
    print(G+"chars here: " + W + chars)
    n1=int(raw_input(G+"starting length here: "+ W))
    n2=int(raw_input(G+"ending length here: "+ W))
    f=("Unlimited.txt")
    print("\n")

    logo()
    print(G+"----------------------------------")
    print(G+"[+]Start generating the list now.")
    print(G+"----------------------------------")
    print("\n")  

    if f=="" or f is None:
        if n1==n2:
            for l in t.product(chars,repeat=n1):
                s=''.join(l)
                print(s)
        elif n2>n1:
            for i in range(n1,n2+1):
                for l in t.product(chars,repeat=i):
                    s=''.join(l)
                    print(s)
        else:
            print("starting length is not greater than ending length ")
    else:
        with open(f,"w") as file:
            if n1==n2:
                for l in t.product(chars,repeat=n1):
                    s=''.join(l)
                    file.write(s+"\n")
            elif n2>n1:
                for i in range(n1,n2+1):
                    for l in t.product(chars,repeat=i):
                        s=''.join(l)
                        file.write(s+"\n")
            else:
                print("starting length is not greater than ending length ")     
    count = 0
    for line in open("Unlimited.txt"):
        count += 1
    print(G+"[+]list Length: "+W+ str(count))
    print(G+"[+]The list is saved at Unlimited.txt")
    print("\n")       

def Limited():
    os.system("rm Limited.txt ")
    logo()
    word_len = int(input(G+"What length would you like word to be: "+W))
    word_count = int(input(G+"how many word would you like: "+W))
    print("\n")

    logo()
    print(G+"----------------------------------")
    print(G+"[+]Start generating the list now.")
    print(G+"----------------------------------")
    print("\n")  
    for x in range(0,word_count):
        word = ""
        for x in range(0,word_len):
            word_char = random.choice(chars)
            word = word + word_char
        #print(word) 

        with open('Limited.txt', 'a') as x:
            x.write(word + '\n')
    
    count = 0
    for line in open("Limited.txt"):
        count += 1
    print(G+"[+]list Length: "+W+ str(count))
    print(G+"[+]The list is saved at Limited.txt")
    print("\n")

def length():
    logo()
    f=raw_input(G+"write a file name[with txt,text]: "+W)
    count = 0
    for line in open(f):
        count += 1
    
    logo()
    print(G+"--------------------------------------")
    print(G+"[+]Start the file length calculation.")
    print(G+"--------------------------------------")
    print("\n")  

    print(G+"Length of this file: "+W+str(count))
    print("\n")

if Option == "01" or Option == "1":
    print("\n")
    Unlimited()
elif  Option == "02" or Option == "2":
    print("\n")
    Limited()
elif  Option == "03" or Option == "3":
    print("\n")
    length()
elif  Option == "00" or Option == "0":
    print("\n")
    print("GoodBye")
    exit()
else:
    print("\n")
    print(R+"Sorry, there is a problem. Make sure to enter the correct number")
    exit()

print(G+"Done,Enjoy.")