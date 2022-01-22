import time
import os

def Kernel():
    print("-----------------------------------------------------------------")
    print("Type file to list directory")
    print("Type gamelist to list games")
    print("Type shutdown to shutdown the kernel")
    print("Type clear or cls to clear the screen")
    print("Type reboot to restart the system")
    print("-----------------------------------------------------------------")
    KC =input("")    

    if KC == "file":
        print("---------------------------------------------")
        os.system("dir")
        print("---------------------------------------------")
        Kernel()

    if KC == "gamelist":
        print("No games avalible")
        Kernel()

    if KC == "shutdown":
        print("Goodbye")
        time.sleep(2)
        exit()

    if KC == "clear":
        os.system("cls") 
        Kernel()
    
    if KC == "cls":
        os.system("cls")
        Kernel()

    if KC == "reboot":
        os.startfile('DEBIOS.py')

    if KC != "file":
        if KC != "gamelist":
            if KC != "shutdown":
                if KC != "clear":
                    if KC != "cls":
                        print("Invalid command")
                        Kernel()

Kernel()