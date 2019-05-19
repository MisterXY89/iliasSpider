# -*- coding: utf-8 -*-

# create spider for a ilias course
# ask user at init for param to create file to call spider with args
# in this file the config gets stored via the config class
# the exec_file calls scrapy via: scrapy crawl ilias -a username=tilman.kerl -a targetdir = 

import os
from config import *


# c = Config("tilman.kerl", "https://ilias.uni-konstanz.de/ilias/goto_ilias_uni_crs_873238.html", "~/Documents/Uni/SS19/AlgoDat/", "Übung", "slides", "ubs/", "slides/")
# call = "scrapy crawl ilias -s LOG_ENABLED=False -a username=%s -a iliasUrl=%s -a targetDir=%s -a assignmentsIdStr=%s -a slidesIdStr=%s -a assignmentsDir=%s -a slidesDir=%s"%(c.USERNAME, c.ILIAS_URL, c.TARGET_DIR, c.ASSIGNMENTS_ID_STR, c.SLIDES_ID_STR, c.ASSIGNMENTS_DIR, c.SLIDES_DIR)
# os.system(call)

# change dir?
DIR = ""

def createFile():
	name = input("Enter a name for your spider (e.g. the name of the course):\n> ")
	username = input("Your ilias username:\n> ")
	iliasUrl = input("The Url of the ilias course:\n> ")
	targetDir = input("Where do you store all your university materials for this course?\n> ")
	print("\nIf you do not need to download assignments/slides just leave the field emtpy.")
	ubsId = input("How can assignments be identified? (e.g. assignment_01_Course.pdf -> assignment)\n> ")
	slidesId = input("How can slides be identified? (e.g. ADS_slides_W1.pdf -> assignment)\n> ")
	ubsDir = input("Where should your assignment files be stored?\n> ")
	slidesDir = input("Where should your slide files be stored?\n> ")
	filename = name + ".py"

	content = ""
	content += "# iliasSpider is a web scraper which downloads your materials from a ilias course (Uni Constance) \n\n"
	content += "# Bei Fehlern oder Fragen: \n"
	content += "# -> Eröffne einen neuen Issue auf github[https://github.com/MisterXY89/iliasSpider] "
	content += "# @author Tilman Kerl"
	content += "# @version 2019.05.19"
	content += "import os\n"
	content += "from config import *\n"
	content += "c = Config('%s', '%s', '%s', '%s', '%s', '%s', '%s')\n"%(username, iliasUrl, targetDir, ubsId, slidesId, ubsDir, slidesDir)
	content += 'call = "scrapy crawl ilias -s LOG_ENABLED=False -a username=%s -a iliasUrl=%s -a targetDir=%s -a assignmentsIdStr=%s -a slidesIdStr=%s -a assignmentsDir=%s -a slidesDir=%s"%(c.USERNAME, c.ILIAS_URL, c.TARGET_DIR, c.ASSIGNMENTS_ID_STR, c.SLIDES_ID_STR, c.ASSIGNMENTS_DIR, c.SLIDES_DIR)\n'
	content += "os.system(call)"

	with open(DIR + filename, "w") as f:
		f.write(content)

	print("Your downloader has been configured. You can call it via:\n> python <NAME>.py")


createFile()