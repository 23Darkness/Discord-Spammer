import shutil
import os
import time
import json
import random
import base64
import threading
import re
import subprocess
import sys
import colorama
import cursor
import re
import json
from socket import timeout
from multiprocessing.connection import wait
from optparse import Option
import requests, colorama, shutil, subprocess, cursor, os, time, json, random, base64, threading, re, sys;
from capmonster_python import HCaptchaTask
from colorama import Fore, Style, init
from pystyle import *
from urllib.request import Request, urlopen


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
