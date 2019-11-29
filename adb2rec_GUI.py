#!/usr/bin/python2
# V. 0.3 Beta
#20191129 h. 20.43

# by Antonio "Visi@n" Broi broi.antonio@gmail.com
# http://www.broi.it aNTbRO

# by Antonio "Visi@n" Broi broi.antonio@gmail.com
# http://www.broi.it aNTbRO

# 
# LICENSE M.I.T.              https://opensource.org/licenses/MIT
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
#OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
#OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from datetime import datetime
from os import listdir
from os.path import isdir, join, isfile, splitext
from  Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import Tkinter as tk
import sys
import os
import subprocess
import sys, signal
import time
from ppadb import *
import googletrans
from googletrans import Translator
import subprocess
import socket

if not os.path.exists('screenshot'):
		os.makedirs('screenshot')
if not os.path.exists('screenrecord'):
		os.makedirs('screenrecord')
if not os.path.exists('compressfiles'):
		os.makedirs('compressfiles')
if not os.path.exists('hashfiles'):
		os.makedirs('hashfiles')
			
translator =  Translator()
###interrupt all def or while cicle with CTRL-C

#def signal_handler(signal, frame):
#    print("\nprogram exiting gracefully")
#    sys.exit(0)

#signal.signal(signal.SIGINT, signal_handler)

#os.chdir(os.path.expanduser('~'))
#ok
def install_requirements():
	if not os.path.exists('screenshot'):
			os.makedirs('screenshot')
	if not os.path.exists('screenrecord'):
			os.makedirs('screenrecord')
	if not os.path.exists('compressfiles'):
			os.makedirs('compressfiles')
	if not os.path.exists('hashfiles'):
			os.makedirs('hashfiles')
	command = "sudo apt-get install adb figlet cowsay ruby-notify flite"
	subprocess.Popen(command, shell=True)		
#ok
def helpme():
	global helpme
	command = ('flite -t "Connect you Target Mobile with cable" & echo "Connect you Target Mobile with cable" & notify-send  "Connect you Target Mobile with cable"')
	subprocess.Popen(command, shell=True)
	time.sleep(3.0)
	command = ('flite -t "you must enable envelope type build number for 7" & echo "you must enable envelope type build number for 7" & notify-send "you must enable envelope type build number for 7"')
	subprocess.Popen(command, shell=True)
	time.sleep(3.0)
	command = ('flite -t "you must put ON envelope options" & echo "you must put ON envelope options" & notify-send "you must put ON envelope options"')
	subprocess.Popen(command, shell=True)
	time.sleep(3.0)
	command = ('flite -t "put Debug USB on" & echo "put Debug USB on" & notify-send "put Debug USB on"')
	subprocess.Popen(command, shell=True)
#ok
def adb_connect_cable():
	global adb_connect_cable
	command = ('echo "you chose Adb Connect cable ....stand by"')
	subprocess.Popen(command, shell=True)
	
	command = ('flite -t "you chose Adb Connect cable ....stand by"')
	subprocess.Popen(command, shell=True)
	
	command = ('notify-send "you chose Adb Connect cable ....stand by"')
	subprocess.Popen(command, shell=True)		
	time.sleep(3.0)

	command = ('adb devices -l')
	subprocess.Popen(command, shell=True)
	
	command = ('adb tcpip 7777')
	subprocess.Popen(command, shell=True)
	time.sleep(3.0)

	command = ('echo "now disconnect the cable from mobile phone and connect the to wifi"')
	subprocess.Popen(command, shell=True)
	
	command = ('flite -t "now disconnect the cable from mobile phone and connect the to wifi"')
	subprocess.Popen(command, shell=True)
	
	command = ('notify-send "now disconnect the cable from mobile phone and connect the to wifi"')
	subprocess.Popen(command, shell=True)
	
#ok
def adb_connect_ip_wifi():
	global adb_connect_ip_wifi
	
	command = ('echo "you chose Adb Connect wifi ....stand by"')
	subprocess.Popen(command, shell=True)
	command = ('flite -t "you chose Adb Connect wifi ....stand by"')
	subprocess.Popen(command, shell=True)
	command = ('notify-send "you chose Adb Connect wifi ....stand by"')
	subprocess.Popen(command, shell=True)
	time.sleep(3.0)
	
	command = ('echo "now connect your Mobile phone to the wifi and get the IP"')
	subprocess.Popen(command, shell=True)
	command = ('flite -t "now connect your Mobile phone to the wifi and get the IP"')
	subprocess.Popen(command, shell=True)
	command = ('notify-send "now connect your Mobile phone to the wifi and get the IP"')
	subprocess.Popen(command, shell=True)
	time.sleep(3.0)
	
	command = ('echo "insert the PRIVATE IP type 192.168.x.x "')
	subprocess.Popen(command, shell=True)
	command = ('flite -t "insert the PRIVATE IP type 192.168.x.x "')
	subprocess.Popen(command, shell=True)
	command = ('notify-send "insert the PRIVATE IP type 192.168.x.x "')
	subprocess.Popen(command, shell=True)
	time.sleep(10.0)
	
	#command = ('read ip')
	#subprocess.Popen(command, shell=True)
	#time.sleep(3.0)
	ip = input('Insert private IP of your Mobile Phone, like this \'192.168.43.1\' : ')
	try:
		socket.inet_aton(ip)
		print("Valid IP")
	except socket.error:
		print("Invalid IP")
	
	command = ('adb connect '+ip+':7777')
	subprocess.Popen(command, shell=True)
	time.sleep(1.0)
	
	command = ('echo "adb connect '+ip+':7777"')
	subprocess.Popen(command, shell=True)
	command = ('flite -t "adb connect '+ip+':7777"')
	subprocess.Popen(command, shell=True)
	command = ('notify-send "adb connect '+ip+':7777"')
	subprocess.Popen(command, shell=True)	
	time.sleep(3.0)
	
	command = ('echo "now you can make screenshot or screenrecord from Mobile Phone connect to your WIFI"')
	subprocess.Popen(command, shell=True)
	command = ('flite -t  "now you can make screenshot or screenrecord from Mobile Phone connect to your WIFI"')
	subprocess.Popen(command, shell=True)
	command = ('notify-send "now you can make screenshot or screenrecord from Mobile Phone connect to your WIFI"')
	subprocess.Popen(command, shell=True)

#ok	
def screenshot():
	global screenshot
	if not os.path.exists('screenshot'):
			os.makedirs('screenshot')	
	command = ('chmod 755 screenshot.sh')
	subprocess.Popen(command, shell=True)
	command = ('./screenshot.sh')
	subprocess.Popen(command, shell=True)
#ok	
def screenshot_up():
	global screenshot
	if not os.path.exists('screenshot'):
			os.makedirs('screenshot')	
	command = ('chmod 755 screenshot.sh')
	subprocess.Popen(command, shell=True)
	command = ('./screenshot_up.sh')
	subprocess.Popen(command, shell=True)
#ok	
def screenshot_down():
	global screenshot
	if not os.path.exists('screenshot'):
			os.makedirs('screenshot')	
	command = ('chmod 755 screenshot.sh')
	subprocess.Popen(command, shell=True)
	command = ('./screenshot_down.sh')
	subprocess.Popen(command, shell=True)		
#ok
def killscreenshot():
	global killscreenshot
	command = "kill `ps aux | grep 'screenshot.sh'|awk '{print $2}'`"
	subprocess.Popen(command, shell=True)	
	command = "kill `ps aux | grep 'screenshot_up.sh'|awk '{print $2}'`"
	subprocess.Popen(command, shell=True)	
	command = "kill `ps aux | grep 'screenshot_down.sh'|awk '{print $2}'`"
	subprocess.Popen(command, shell=True)		
#ok	
def screenrecord():
	global screenrecord
	if not os.path.exists('screenrecord'):
			os.makedirs('screenrecord')	
	command = ('chmod 755 screenrecord.sh')
	subprocess.Popen(command, shell=True)
	command = ('./screenrecord.sh')
	subprocess.Popen(command, shell=True)
#ok
def killscreenrecord():
	global killscreenrecord
	command = ("kill `ps aux | grep 'screenrecord.sh'|awk '{print $2}'`")
	subprocess.Popen(command, shell=True)	
#ok	
def compressandhash():
	global compressandhash
	command = ('echo "you chose Hash All .....ok... keep calm and get one Italian\'s coffee .... stand by"')
	subprocess.Popen(command, shell=True)	
	command = ('tgz compressfiles/screenrecord.tar.gz screenrecord/')
	subprocess.Popen(command, shell=True)	
	command = ('tgz compressfiles/screenshot.tar.gz screenshot/')
	subprocess.Popen(command, shell=True)	
	command = ('echo "md5sum"> hashfiles/hash_screenshot.txt')
	subprocess.Popen(command, shell=True)	
	command = ('md5sum compressfiles/screenshot.tar.gz >> hashfiles/hash_screenshot.txt')
	subprocess.Popen(command, shell=True)	
	command = ('echo "sha256sum">> hashfiles/hash_screenshot.txt')
	subprocess.Popen(command, shell=True)	
	command = ('sha256sum compressfiles/screenshot.tar.gz >> hashfiles/hash_screenshot.txt')
	subprocess.Popen(command, shell=True)	
	command = ('echo "md5sum">hashfiles/hash_screenrecord.txt')
	subprocess.Popen(command, shell=True)	
	command = ('md5sum compressfiles/screenrecord.tar.gz >> hashfiles/hash_screenrecord.txt')
	subprocess.Popen(command, shell=True)	
	command = ('echo "sha256sum">>hashfiles/hash_screenrecord.txt')
	subprocess.Popen(command, shell=True)	
	command = ('sha256sum compressfiles/screenrecord.tar.gz >> hashfiles/hash_screenrecord.txt')
	subprocess.Popen(command, shell=True)	
	command = ('echo "################"')
	subprocess.Popen(command, shell=True)	
	command = ('echo "hashfiles/hash_screenrecord.txt"')
	subprocess.Popen(command, shell=True)	
	command = ('cat hashfiles/hash_screenrecord.txt')
	subprocess.Popen(command, shell=True)	
	command = ('echo "################"')
	subprocess.Popen(command, shell=True)	
	command = ('echo "hashfiles/hash_screenshot.txt"')
	subprocess.Popen(command, shell=True)	
	command = ('cat hashfiles/hash_screenshot.txt')
	subprocess.Popen(command, shell=True)	

#ok	
def directoryocr():
	global directoryocr
	os.chdir(os.path.expanduser('~'))
	if not os.path.exists('02.computer_vision'):
			os.makedirs('02.computer_vision')

	os.chdir(os.path.expanduser('~/02.computer_vision/'))
	if not os.path.exists('04.video2ocr'):
			os.makedirs('04.video2ocr')
	if not os.path.exists('04.video2ocr/01.video'):
			os.makedirs('04.video2ocr/01.video')
	if not os.path.exists('04.video2ocr/02.images'):
			os.makedirs('04.video2ocr/02.images')
	if not os.path.exists('04.video2ocr/03.imagesgrey'):
			os.makedirs('04.video2ocr/03.imagesgrey')
	if not os.path.exists('04.video2ocr/04.ocr_output'):
			os.makedirs('04.video2ocr/04.ocr_output')			
def video2ocrcolor():
	lang = input('Insert language, example \"eng\" \"ita\" \"ara\" : ')
	command =('chmod 755 video2ocrColor')
	subprocess.Popen(command, shell=True)
	command =('./video2ocrColor '+lang)
	subprocess.Popen(command, shell=True)
#ok
def translateinenglish():
	global translateinenglish
	try:
		while True:
		
			#sentence = str(input('enter a sentence with \" example \"Ciao\": '))
			#sentence1 = str(sentence)
			sentence = raw_input('insert the phrase \n xxx to exit: ')
			sentence1 = str(sentence)
			
			rigatrans = translator.translate(sentence, dest="en")
			print(rigatrans)

	except KeyboardInterrupt:
		print('interrupted!')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.wm_title("adb2rec")
root.geometry("360x690")


	
label = tk.Label(text=".          Screen Shot       -       Screen Record",
				fg="red",
				font=("helvetica",12),
				
					)
label.pack(ipadx=15, ipady=4, pady=15, padx=10)
label.place(x=0, y=0)
#ok
button = tk.Button(frame, 
                   text="QUIT", 
                   fg="#ffffff",
                   bg="#000000",
                   command=quit)
button.pack(ipadx=128, ipady=4, pady=25)


#ok
slogan = tk.Button(frame,
                   text="INSTALL REQUIREMENTS",
                   fg="#ffffff",
                   bg="#ff0000",
                   command=install_requirements)
slogan.pack(ipadx=60, ipady=4, pady=1)
#ok
slogan = tk.Button(frame,
                   text="HELP",
                   fg="#ffffff",
                   bg="#ff0000",
                   command=helpme)
slogan.pack(ipadx=124, ipady=4, pady=1)

#ok
slogan = tk.Button(frame,
                   text="ADB CONNECT CABLE MOBILE FOR WIFI",
                   fg="#ffffff",
                   bg="#0000ff",
                   command=adb_connect_cable)
slogan.pack(ipadx=10, ipady=4, pady=1)

#ok
slogan = tk.Button(frame,
                   text="ADB CONNECT PRIVATE-IP MOBILE WIFI",
                   fg="#ffffff",
                   bg="#0000ff",
                   command=adb_connect_ip_wifi)
slogan.pack(ipadx=10, ipady=4, pady=1)

#ok
slogan = tk.Button(frame,
                   text="SCREEN SHOT",
                   fg="#0000ff",
                   bg="#00ff00",
                   command=screenshot)
slogan.pack(ipadx=94, ipady=4, pady=1)


#ok
slogan = tk.Button(frame,
                   text="SCREEN SHOT UP",
                   fg="#0000ff",
                   bg="#00ff00",
                   command=screenshot_up)
slogan.pack(ipadx=84, ipady=4, pady=1)

#ok
slogan = tk.Button(frame,
                   text="SCREEN SHOT_down",
                   fg="#0000ff",
                   bg="#00ff00",
                   command=screenshot_down)
slogan.pack(ipadx=74, ipady=4, pady=1)
#ok
slogan = tk.Button(frame,
                   text="KILL SCREEN SHOT",
                   fg="#ffffff",
                   bg="#000000",
                   command=killscreenshot)
slogan.pack(ipadx=79, ipady=4, pady=1)
#ok
slogan = tk.Button(frame,
                   text="SCREEN RECORD",
                   fg="#0000ff",
                   bg="#00ff00",
                   command=screenrecord)
slogan.pack(ipadx=84, ipady=4, pady=1)
#ok
slogan = tk.Button(frame,
                   text="KILL SCREEN RECORD",
                   fg="#ffffff",
                   bg="#000000",
                   command=killscreenrecord)
slogan.pack(ipadx=68, ipady=4, pady=1)
#ok
slogan = tk.Button(frame,
                   text="COMPRESS AND MAKE HASH TO ALL",
                   fg="#0000ff",
                   bg="#00ff00",
                   command=compressandhash)
slogan.pack(ipadx=19, ipady=4, pady=1)#ipadx=11
#ok
slogan = tk.Button(frame,
                   text="CREATE STRUCTURE DIRECTORY FOR OCR",
                   fg="#ffffff",
                   bg="#0000ff",
                   command=directoryocr)
slogan.pack(ipadx=0, ipady=4, pady=1)
#ok
slogan = tk.Button(frame,
                   text="VIDEO2OCR",
                   fg="#ffffff",
                   bg="#0000ff",
                   command=video2ocrcolor)
slogan.pack(ipadx=100, ipady=4, pady=1)

slogan = tk.Button(frame,
                   text="TRANSLATE FROM ALL LANGS TO ENGLISH",
                   fg="#000000",
                   bg="#ffcb05",
                   command=translateinenglish)
slogan.pack(ipadx=1, ipady=4, pady=1)

label = tk.Label(text="Visi@n",
				fg="red",
				font=("helvetica",12),
				
					)
label.pack(ipadx=15, ipady=4, pady=15, padx=10)
label.place(x=280, y=660)

root.mainloop()
