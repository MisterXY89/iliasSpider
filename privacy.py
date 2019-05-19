# -*- coding: utf-8 -*-

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
		should_store = input("Would you like to store the password encrpyted for the future? [y/N] ")
		if should_store == "y":
			storePwd(PASSWORD, username)

def resetPassword(username):
	keyring.delete_password(SPIDER_NAME, username)

def getPassword():
	return PASSWORD