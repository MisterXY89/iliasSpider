# -*- coding: utf-8 -*-

import os
import platform
import scrapy
from scrapy.selector import *
from scrapy.http.request import Request
from config import *
from privacy import *

class iliasSpider(scrapy.Spider):
	name = SPIDER_NAME

	start_urls = [
		ILIAS_LOGIN_URL
	]

	def __init__(self, username=None, iliasUrl=None, targetDir=None, assignmentsIdStr=None, slidesIdStr=None, assignmentsDir=None, slidesDir=None, *args, **kwargs):
		super(iliasSpider, self).__init__(*args, **kwargs)
		self.fDict = {}
		self.username = username
		self.ilias_url = iliasUrl
		self.target_dir = targetDir
		self.assignments_id_str = assignmentsIdStr
		self.slides_id_str = slidesIdStr
		self.assignments_dir = assignmentsDir
		self.slides_dir = slidesDir

		setAuth(self.username)


	def parse(self, response):
		return scrapy.FormRequest.from_response(
			response,
			formdata={'username': self.username, 'password': getPassword()},
			callback=self.after_login
		)


	def after_login(self, response):
		# check login succeed before going on
		if b"authentication failed" in response.body:
			self.logger.error("Login failed")
			print("authentication failed")
			resetPassword(self.username)
			print("The password has been reset. Please restart the program and enter your password again.")
			return
		else:
			print("Login succeesful")
			yield Request(
				url= self.ilias_url,
				callback=self.findDownloadLinksAndNames
			)


	def findDownloadLinksAndNames(self,response):
		sel = Selector(response)
		fnames = sel.css("h4.il_ContainerItemTitle a::text").extract()
		links = sel.css("div.il_ContainerItemTitle a::attr(href)").extract()
		self.fDict = dict(zip(links,fnames))
		for href in links:
			yield Request(
				url = href,
				callback = self.download
			)


	# verify if file should be downloaded
	def verify(self, link):
		if "download" in link:
			return True
		return False


	# save file
	def store(self, filename, content):
		storeDir = self.getStoreDir(filename)

		print("Downloading %s to %s" %(filename, storeDir))
		if PLATFORM == "Linux":
			# in linux files has to be stored first in the tmp folder
			with open(TMP_DIR + filename, "wb") as f:
				f.write(content)
			os.system("mv " + TMP_DIR + filename + " " + storeDir + filename)
		elif PLATFORM == "Windows":
			with open(storeDir + filename, "wb") as f:
				f.write(content)


	# prep filename for easier handling
	def prepFileName(self, filename):
		filename = filename.replace("/","_")
		filename = filename.replace(" ","_")
		filename = filename.replace("(","_")
		filename = filename.replace(")","_")
		return filename + ".pdf"


	# where to move file to
	def getStoreDir(self, filename):
		if self.slides_id_str in filename:
			return self.slides_dir
		elif self.assignments_id_str in filename:
			return self.assignments_dir
		return self.target_dir


	# download controller
	def download(self, response):
		url = str(response.url)

		# determine if should be downloaded
		if self.verify(url):
			filename = self.prepFileName(self.fDict[url])
			self.store(filename, response.body)
