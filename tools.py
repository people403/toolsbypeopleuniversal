import os, sys, time
    
def menu():
    os.system("clear")
    time.sleep(4)
    print("")
    print("#################################")
    print("## Tools By @magiskpeople      ##")
    print("## Instagram @magiskpeople     ##")
    print("## Copyright@github.com        ##")
    print("#################################")
    time.sleep(3)
    print("")
    print("[1] Sharelock Location")
    print("[2] LITEDDOS")
    print("[3] SpiderBot")
    print("[4] LITETOOLS")
    print("[0] Exit")
    time.sleep(2)
    print("")
    tools = input("Input Number : ")
    if tools =="1":
        print("Please wait for second!")
        time.sleep(3)
        os.system("clear")
        time.sleep(3)
        os.system("git clone https://github.com/sherlock-project/sherlock.git")
        print("𝙳𝚘𝚗𝚎 𝙸𝚗𝚜𝚝𝚊𝚕𝚕 >>>>>>> 𝟷𝟶𝟶%")
        time.sleep(3)
    
    if tools =="2":
        os.system("apt update && apt upgrade")
        os.system("pkg install git")
        os.system("pkg install python2")
        os.system("git clone https://github.com/4L13199/LITEDDOS")
        time.sleep(4)
        os.system("clear")
        os.system("python tools.py")

    if tools =="3":
        os.system("apt update && apt upgrade")
        os.system("apt install php")
        os.system("apt install git")
        os.system("git clone https://github.com/Cvar1984/SpiderBot.git")
        os.system("cd SpiderBot")
        time.sleep(3)
        os.system("clear")
        time.sleep(3)
        print("Tinggal Dijalankan Saja, Seperti Hubunganmu Dengan Dia, Eaaa!:)")
        time.sleep(2)
        print("Contoh Saya Ingin Pakai Botkomen")
        time.sleep(2)
        print("Ketik: php botkoment.php")
        time.sleep(1)
        os.system("clear")
        os.system("python tools.py")

    if tools =="4":
        os.system("pkg update && pkg upgrade")
        os.system("pkg install git")
        os.system("git clone https://github.com/4L13199/LITETOOLS")
        os.system("clear")
        os.system("python tools.py")

    elif tools =="0":
        os.system("clear")
        print("Please Wait 3s...!!!")
        time.sleep(3)
        print("Bye Don't Forget Follow Media Social")
        time.sleep(2)
        os.system("exit")

    else:
        print("Pls Input Number Valid...!!!")
        time.sleep(4)
        os.system("clear")
        os.system("python tools.py")
        
menu()
