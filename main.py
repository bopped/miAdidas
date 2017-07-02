# miAdidas Enter Script
# Dev: Simmy (bopped) Twitter: @Backdoorcook
import time, json, random, colorama, threading, os
from time import sleep
from colorama import *

if os.name == 'nt':
	init()


from classes.logger import logger
log = logger().log

from classes.GmailDotGen import GmailDotEmailGenerator


from classes.miAdidas import Enter

if not os.path.exists("config.json"):
	log("%sConfig.json not Found!!!"  %  (Fore.RED))
	exit()

with open('config.json') as json_data_file:
	config = json.load(json_data_file)

log("-------------------------------")
log("%s%sConfiguration loaded.%s" % (Style.BRIGHT, Fore.GREEN, Style.RESET_ALL))
log("%s%sMade by Simmy.%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL))
log("-------------------------------")

miAdidasEnter = Enter(config)


print miAdidasEnter.startEntry()