# -*- coding: utf-8 -*-

# create spider for a ilias course
# ask user at init for param to create file to call spider with args
# in this file the config gets stored via the config class
# the exec_file calls scrapy via: scrapy crawl ilias -a username=tilman.kerl -a targetdir = 

import os
import sys
from config import *


# c = Config("tilman.kerl", "https://ilias.uni-konstanz.de/ilias/goto_ilias_uni_crs_873238.html", "~/Documents/Uni/SS19/AlgoDat/", "Übung", "slides", "ubs/", "slides/")
# call = "scrapy crawl ilias -s LOG_ENABLED=False -a username=%s -a iliasUrl=%s -a targetDir=%s -a assignmentsIdStr=%s -a slidesIdStr=%s -a assignmentsDir=%s -a slidesDir=%s"%(c.USERNAME, c.ILIAS_URL, c.TARGET_DIR, c.ASSIGNMENTS_ID_STR, c.SLIDES_ID_STR, c.ASSIGNMENTS_DIR, c.SLIDES_DIR)
# os.system(call)

# change dir?
DIR = ""

def createFile():
	print("Since all files are downloaded with a .pdf extension there might occur an error downloading files of another file format.")
	print("In most cases, it is sufficient to just change the .pdf extension to the correct one.")

	print("Enter a name for your spider (e.g. the name of the course): ")
	name = str(sys.stdin.readline()[:-1])
	print("Your ilias username: ")
	username = str(sys.stdin.readline()[:-1])
	print("The Url of the ilias course: ")
	iliasUrl = str(sys.stdin.readline()[:-1])
	print("Where do you store all your university materials for this course? ")
	targetDir = str(sys.stdin.readline()[:-1])
	print("If you do not need to download assignments/slides just leave the field emtpy.")
	print("How can assignments be identified? (e.g. assignment_01_Course.pdf -> assignment) ")
	ubsId = str(sys.stdin.readline()[:-1])
	print("How can slides be identified? (e.g. ADS_slides_W1.pdf -> assignment) ")
	slidesId = str(sys.stdin.readline()[:-1])
	print("Where should your assignment files be stored? ")
	ubsDir = str(sys.stdin.readline()[:-1])
	print("Where should your slide files be stored? ")
	slidesDir = str(sys.stdin.readline()[:-1])
	filename = name + ".py"

	content = "# -*- coding: utf-8 -*- \n"
	content += "############################################################# \n"
	content += "# iliasSpider is a web scraper which downloads your materials \n"
	content += "# from an ilias course (Uni Constance) \n"
	content += "# \n"
	content += "# If there are errors or questions: \n"
	content += "# -> Open a new issue at github[https://github.com/MisterXY89/iliasSpider/issues/] \n"
	content += "# @author Tilman Kerl \n"
	content += "# @version 2019.05.19\n\n"
	content += "import os\n"
	content += "from config import *\n"
	content += "c = Config('%s', '%s', '%s', '%s', '%s', '%s', '%s')\n"%(username, iliasUrl, targetDir, ubsId, slidesId, ubsDir, slidesDir)
	content += 'call = "scrapy crawl ilias -s LOG_ENABLED=False -a username=%s -a iliasUrl=%s -a targetDir=%s -a assignmentsIdStr=%s -a slidesIdStr=%s -a assignmentsDir=%s -a slidesDir=%s"%(c.USERNAME, c.ILIAS_URL, c.TARGET_DIR, c.ASSIGNMENTS_ID_STR, c.SLIDES_ID_STR, c.ASSIGNMENTS_DIR, c.SLIDES_DIR)\n'
	content += "os.system(call)"

	with open(DIR + filename, "w") as f:
		f.write(content)

	print("Your downloader has been configured. You can call it via:\n> python <NAME>.py")


createFile()