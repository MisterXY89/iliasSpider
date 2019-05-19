# -*- coding: utf-8 -*-

import sys
import getpass
import keyring
from config import *

PASSWORD = ""

def storePwd(pwd,username):
	keyring.set_password(SPIDER_NAME, username, pwd)

def readPwd(username):
	return keyring.get_password(SPIDER_NAME, username)
	
def setAuth(username):
	global PASSWORD

	if readPwd(username) != None:
		PASSWORD = readPwd(username)
	else:
		print("Please enter your password: ")
		PASSWORD = getpass.getpass()
		print("Would you like to store the password encrpyted for the future? [y/N]")
		should_store = str(sys.stdin.readline()[:-1])
		if should_store == "y":
			storePwd(PASSWORD, username)

def resetPassword(username):
	keyring.delete_password(SPIDER_NAME, username)

def getPassword():
	return PASSWORD