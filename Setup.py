import time
import os

with open('./OS/username.DEBI', 'r+') as A:
    global setUser
    setUser =input("Please enter the username you want to use: ")
    # Write Username
    A.writelines(setUser)

with open('./OS/password.DEBI', 'r+') as B:
    global setPass
    setPass =input("Please enter the password you want to use: ")
    # Write password
    B.writelines(setPass)

with open('./OS/Bootloader.DEBI', 'r+') as C:
    C.writelines('1')

print("Setup Complete")
os.startfile('DEBIOS.py')