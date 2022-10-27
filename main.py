import colorama
from multiprocessing.connection import wait
from optparse import Option
import os, time, json, random, base64, threading, re, sys
from socket import timeout
from tkinter import N
try: import requests, colorama, cursor; from capmonster_python import HCaptchaTask
except: os.system('pip install -q capmonster-python websocket requests colorama cursor')
import requests, colorama, cursor; from capmonster_python import HCaptchaTask
from colorama import *
from pystyle import Colors, Colorate
import hashlib
import time, os
import os
import re
import json
import requests
import os
import requests
from tkinter import *
from tkinter.filedialog import *
from urllib.request import Request, urlopen
import discord


print(Fore.BLUE + """
 ██▓ ███▄    █ ██▒   █▓ ██▓▄▄▄█████▓▓█████     ▄▄▄██▀▀▀▒█████   ██▓ ███▄    █ ▓█████  ██▀███  
▓██▒ ██ ▀█   █▓██░   █▒▓██▒▓  ██▒ ▓▒▓█   ▀       ▒██  ▒██▒  ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██  ▀█ ██▒▓██  █▒░▒██▒▒ ▓██░ ▒░▒███         ░██  ▒██░  ██▒▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
░██░▓██▒  ▐▌██▒ ▒██ █░░░██░░ ▓██▓ ░ ▒▓█  ▄    ▓██▄██▓ ▒██   ██░░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
░██░▒██░   ▓██░  ▒▀█░  ░██░  ▒██▒ ░ ░▒████▒    ▓███▒  ░ ████▓▒░░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
░▓  ░ ▒░   ▒ ▒   ░ ▐░  ░▓    ▒ ░░   ░░ ▒░ ░    ▒▓▒▒░  ░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░ ░░   ░ ▒░  ░ ░░   ▒ ░    ░     ░ ░  ░    ▒ ░▒░    ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ░   ░   ░ ░     ░░   ▒ ░  ░         ░       ░ ░ ░  ░ ░ ░ ▒   ▒ ░   ░   ░ ░    ░     ░░   ░ 
 ░           ░      ░   ░              ░  ░    ░   ░      ░ ░   ░           ░    ░  ░   ░     
                   ░                                                                          
""")
confir = Write.Input(
        "© Copyright                 › Press Enter...",
        Colors.blue_to_red,
        interval=0.05)

print("1 - Token Joiner")
print("2 - Spammer")
print("3 - Leaver")
option = input('What is your choise ? > ')

if option == '1':

    link = input('Ton lien d\'invitation > ')
    if len(link) > 6:
        link = link[19:]
        apilink = "https://discordapp.com/api/v6/invite/" + str(link)
    print (link)
    with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("Tous les tokens valides ont join !")





if option == '2':
    id = input("Entrer l'id du channel  : ")
    token = input("Entrer le token  : ")
    message = input("Entrer le message : ")

    Payload = {
    'content': message

    }

    header = {
    'authorization' : token
    }

    spam = input("spam mod ( y / n )  : ")
    if spam == "y" or spam == "Y":
        while True:
            r = requests.post("https://discord.com/api/v9/channels/" + id + "/messages" , data=Payload , headers=header)
        else:
            r = requests.post("https://discord.com/api/v9/channels/" + id + "/messages" , data=Payload , headers=header)


if option == '3':
  print ("Open Token .txt file...")
  Tk().withdraw()
  token = askopenfilename()
  with open(token) as handle:
      txtf = handle.read()

  f = open("tokens.txt","w+")
  f.write(txtf)
  f.close()
  
  ID = input('Discord Server ID to leave: ')
  
  apilink = "https://discordapp.com/api/v6/users/@me/guilds/" + str(ID)
  
  with open('tokens.txt','r') as handle:
          tokens = handle.readlines()
          for x in tokens:
              token = x.rstrip()
              headers={
                  'Authorization': token
                  }
              requests.delete(apilink, headers=headers)
          print ("All valid tokens have left that server.")
  input()
