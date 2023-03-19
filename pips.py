# Date: 19/03/2023
# Author: Dmytro Kolodnyanskyi
# Description: Install pips to main.py

import os

pips = input("1) pip\n2) pip3\n?:  ")

while True:
	try:
		if pips == "1":
			os.system("pip install free-proxy --progress-bar off")
			os.system("pip install colorama --progress-bar off")
			os.system("pip install instabot --progress-bar off")
			break
		elif pips == "2":
			os.system("pip3 install free-proxy --progress-bar off")
			os.system("pip3 install colorama --progress-bar off")
			os.system("pip3 install instabot --progress-bar off")
			break
		else:
			print("Restart!")
	except:
		print("Error pip(3) install!")
		break
