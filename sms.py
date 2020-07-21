import os,sys,time
import requests
import subprocess
from requests import post

#SpamSms Derz Grub
#Tools ini sekarang not free 
#jika mau silahkan chat ke nomer ini 08812425716
#tekan ctrl + z untuk keluar


























def bersih():
    os.system("clear")

def balik():
    d = input("\033[1;97mKeluar? (y/t): ")
    if d == "y":
       subprocess.call("python call.py",shell=True)
    elif d == "t":
         print ("\033[1;91mExit")
         os.system("exit")

bersih()
