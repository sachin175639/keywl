#!/bin/bash

if [ ! -d $HOME/.wine ]
then
        clear
        echo ""
        echo "  wine is not detected in your device "
        echo "please install wine and then run sh setup.sh"
        echo ""
	exit
else
	echo ""
	echo "wine detected"
	echo ""
	sleep 3
fi
sudo apt-get install python -y
sudo pip install pyinstaller 
sudo pip install pynput
wine msiexec /i python-2.7.16.msi
wine $HOME/.wine/drive_c/Python27/python.exe -m pip install --upgrade pip
wine $HOME/.wine/drive_c/Python27/Scripts/pip.exe install pyinstaller
wine $HOME/.wine/drive_c/Python27/Scripts/pip.exe install pynput


