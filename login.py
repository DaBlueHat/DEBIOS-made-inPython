import time
import os

with open('./OS/password.DEBI') as B:
    passRead = B.read()
    if passRead == "0":
        print("Please set a password")
        os.startfile('Setup.py')
        exit()

with open('./OS/password.DEBI') as A:
    rightPass = A.read()
    enterPassword = input("Please enter your password you set: ")
        
    if enterPassword == rightPass:
        print("Logged in")
        os.startfile('kernel.py')

    if enterPassword != rightPass:
        print("Wrong password")
        os.startfile('DEBIOS.py')
