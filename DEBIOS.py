import time
import os

with open('./OS/Bootloader.DEBI')as A:
    bootloader = A.read()

    if bootloader == "0":
        print("Loading Setup")
        os.startfile('Setup.py')

    if bootloader == "1":
        print("Loading login")
        os.startfile('login.py')
