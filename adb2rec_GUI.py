#!/usr/bin/python2
# V. 0.3 Beta
#20191129 h. 23.50

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
import argparse
import locale

os.environ["PYTHONIOENCODING"] = "utf-8" 
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8") 

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--daemon", default="d",
	help="you can change the first languange, default en")
ap.add_argument("-1", "--lang1", default="en",
	help="you can change the first languange, default en")
ap.add_argument("-2", "--lang2", default="fr",
	help="you can change the first languange, default fr")
ap.add_argument("-3", "--lang3", default="it",
	help="you can change the first languange, default it")
ap.add_argument("-4", "--lang4", default="es",
	help="you can change the first languange, default es")
ap.add_argument("-t", "--time", default=int(3),
	help="Time between one language and another, example in secondo 6.0 or 7.0 or 8.0 etc")			

args = vars(ap.parse_args())				

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
	os.getcwd()
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
	if not os.path.exists('audio'):
		os.makedirs('audio')
	
	if not os.path.exists('text'):
		os.makedirs('text')	
	
		###################################################################
	print(("""\

	_____________________________________
	( TRANSLATE IN PYTHON BY              )
	( VISION                              )
	-------------------------------------
		""").encode('utf-8'))
     
	print(("""\
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	;;;;;;;;;;;;;;;;;;;;l0Oo;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	;;;;;;;;;;;;;;;;;;;;:0WW0d:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	;;;;;;;;;;;;;;;;;;;;:OMMMWk;;;;;;;;;;;;;;;;;;:lldolc:;;;;;;;
	;;;;;;;;;;;;;;;;;;;;kMMMMM0;;;;;;;;;;;;;;;;;cOWMMMMWk;;;;;;;
	;;;;;;;;;;;;;;;;;;;cXMMMMMk;;;;;;;;;;;;;;;;dXMNNMMMMO;;;;;;;
	;;;;;;;;;;;;;;;;;;oKMMMMW0c;;;;;;;;;;;;;;;oNM0ckMMMWd;;;;;;;
	;;;;;;;;;;;;;;;;;oNMMMMXo:;;;;;;;;;;;;;;;;OMMocOMMMO:;;;;;;;
	;;;;;;;;;;;;;;;;lXMMMMXo:cllollll:;;;;;;;oXN0cxWMMMk;;;;;;;;
	;;;;;;;;;;;;;;;dXMMMMMXKKNWWMMMMMKxo:;;;;kWx:;kMMMNx;;;;;;;;
	;;;;;;;;;;;;;;oXMMMM0olldxk0KNMMMMMWKl;;c0O:;;kMMMO:;;;;;;;;
	;;;;;;;;;;;;:oXMMMKd:;;;;;;;;dNMMMMMNd;cKMd;;:OMMMk:;;;;;;;;
	;;;;;;;;;;:d0WMMM0c;:odOKKO0K0kkk0KOl;c0MNo;;oNMMNx:;;;;;;;;
	;;;;;;;:okKWMMMNOkO0KMMMMMMMXo;;:d0K0k0MWk:;;dMMM0c:;;;;;;;;
	;;;;dKKXWMMMMMKo:OMMMMMMMMMMKkxolx0NMMMMO:;;;dMMMO:;;;;;;;;;
	;;;;:odOXXK0xxdx0N0kXMMMMMMMMMMMNl;kMMMKc;;;;dMMMk;;;;;;;;;;
	;;;;;;;:c:;:xXWX00O0NMMMX0k0WMMMXl;kMMM0;;;;;dMMMk;;;;;;;;;;
	;;;;;;;;;;;dMM0OKWMMWMMMN0OKWWX0l;lKMMM0;;;;;dMMMk;;;;;;;;;;
	;;;;;;;;;;;lXMMMMMMN0MMMMMXOkl:;;;dNMMM0;;;;;dMMMk;;;;;;;;;;
	;;;;;;;;;;;;xWMMMXONMMMMMMMWOc;;;;:kMMM0;;;;;dMMMk;;;;;;;;;;
	;;;;;;;;;;;;:kWMMk;kWMMN00koc;;;::;cXMWk;;;;;oMMMk;;;;;;;;;;
	;;;;;;;;;;;;;:lll:cOMMMO;;;;;;;dKo;;xWO:;;;;;dMMMk;;;;;;;;;;
	;;;;;;;;;;;;;;;;;cKWMMNxlc;;;:dKXl;;:lc;;;;;;OMMMk;;;;;;;;;;
	;;;;;;;;;;;;;cokOXMMMMWWWNXOk0MMO:;;;;cdllc:lKMMMk;;;;;;;;;;
	;;;;;;;;;;;;oXMMMMMMXxodk0NMMMMMO:;;;;:0MWXXWMMMNd;;;;;;;;;;
	;;;;;;;;;;;;kMMMMMMNd;;;;;oXMMMMNo;;;;;lKMMMMMMM0:;;;;;;;;;;
	;;;;;;;;;;;c0MMMMWOl;;;;;;;cxNMW0c;;;;;;:kWMMMMMx;;;;;;;;;;;
	;;;;;;;;;;;;kMMMNd;;;;;;;;;;;dKk:;;;;;;;;;0MMMWXl;;;;;;;;;;;
	;;;;;;;;;;;;lOOdc;;;;;;;;;;;;;:;;;;;;;;;;;xNMXo:;;;;;;;;;;;;
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;lko;;;;;;;;;;;;;;

		""").encode('utf-8'))
    
	print(("""\
	'af':'afrikaans','sq':'albanian','am':'amharic','ar':'arabic','hy':'armenian','az':'azerbaijani',
	'eu': 'basque','be':'belarusian','bn':'bengali','bs':'bosnian','bg':'bulgarian','ca':'catalan',
	'ceb':'cebuano','ny':'chichewa','zh-cn':'chinese(simplified)','zh-tw':'chinese(traditional)',
	'co':'corsican','hr':'croatian','cs':'czech','da':'danish','nl':'dutch','en':'english',
	'eo':'esperanto','et':'estonian','tl':'filipino','fi':'finnish','fr':'french','fy':'frisian',
	'gl':'galician','ka':'georgian','de':'german','el':'greek','gu': 'gujarati','ht':'haitian creole',
	'ha':'hausa','haw':'hawaiian','iw':'hebrew','hi':'hindi','hmn':'hmong','hu':'hungarian',
	'is':'icelandic','ig':'igbo','id':'indonesian','ga':'irish','it': 'italian','ja': 'japanese',
	'jw':'javanese','kn':'kannada','kk':'kazakh','km':'khmer','ko':'korean','ku': 'kurdish (kurmanji)',
	'ky':'kyrgyz','lo':'lao','la':'latin','lv':'latvian','lt':'lithuanian','lb':'luxembourgish',
	'mk':'macedonian','mg':'malagasy','ms':'malay','ml':'malayalam','mt':'maltese','mi':'maori',
	'mr':'marathi','mn':'mongolian',  'my':'myanmar (burmese)','ne':'nepali','no':'norwegian','ps':'pashto',
	'fa':'persian','pl':'polish',     'pt':'portuguese','pa':'punjabi','ro':'romanian','ru': 'russian',
	'sm':'samoan','gd':scots gaelic','sr':'serbian','st':'sesotho','sn':'shona','sd':'sindhi',
	'si':'sinhala','sk':'slovak','sl':'slovenian','so':'somali','es':'spanish','su':'sundanese',    
	'sw':swahili','sv':'swedish','tg':'tajik','ta':'tamil','te':'telugu','th': 'thai',
	'tr':'turkish','uk':'ukrainian','ur':'urdu','uz':'uzbek','vi':'vietnamese','cy':'welsh',
	'xh':'xhosa','yi':'yiddish','yo':'yoruba','zu':'zulu','fil':'Filipino','he':'Hebrew'
   
		""").encode('utf-8'))
    
		###################################################################

	translator =  Translator()
	###interrupt all def or while cicle with CTRL-C

	def signal_handler(signal, frame):
		print("\nprogram exiting gracefully")
		sys.exit(0)

	signal.signal(signal.SIGINT, signal_handler)


	sentence = ""
	sentence1 = ""

	try:
		while (sentence != "xxx"):
		
			sentence = raw_input('insert the phrase \n xxx to exit: ')
			sentence1 = str(sentence)
			rigatransEN = translator.translate(sentence1, dest=str(args["lang1"]))
			rigatransFR = translator.translate(sentence1, dest=str(args["lang2"]))
			rigatransIT = translator.translate(sentence1, dest=str(args["lang3"]))
			rigatransES = translator.translate(sentence1, dest=str(args["lang4"]))
		
			print("traduct origin: "+sentence1)
			print("             ")		
			print("traduct destination: "+rigatransEN.text)
		
			filenameEN = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+"_"+str(args["lang1"])+".csv"
			filenameEN = open("text"+"/"+filenameEN, "w")
			rigatransENencod = rigatransEN.text.encode('utf8', 'replace')
			filenameEN.write(str(rigatransENencod)+"\n" )
			filenameEN.close()
		
			filenameEN1 = open("text/translate_"+str(args["lang1"])+".txt", "a")
			filenameEN1.write(str(rigatransENencod)+"\n" )
			filenameEN1.close()
		
			print("             ")
		
			print("traduct destination: "+rigatransFR.text)
		
			filenameFR = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+"_"+str(args["lang2"])+".csv"
			filenameFR = open("text"+"/"+filenameFR, "w")
			rigatransFRencod = rigatransFR.text.encode('utf8', 'replace')
			filenameFR.write(str(rigatransFRencod)+"\n")
			filenameFR.close()
						
			filenameFR1 = open("text/translate_"+str(args["lang2"])+".txt", "a")
			filenameFR1.write(str(rigatransFRencod)+"\n" )
			filenameFR1.close()
		
			print("             ")
			print("traduct destination: "+rigatransIT.text)
		
			filenameIT = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+"_"+str(args["lang3"])+".csv"
			filenameIT = open("text"+"/"+filenameIT, "w")
			rigatransITencod = rigatransIT.text.encode('utf8', 'replace')
			filenameIT.write(str(rigatransITencod)+"\n")
			filenameIT.close()
				
			filenameIT1 = open("text/translate_"+str(args["lang3"])+".txt", "a")
			filenameIT1.write(str(rigatransITencod)+"\n" )
			filenameIT1.close()
				
			print("             ")
			print("traduct destination: "+rigatransES.text)
		
			filenameES = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+"_"+str(args["lang4"])+".csv"
			filenameES = open("text"+"/"+filenameES, "w")
			rigatransESencod = rigatransES.text.encode('utf8', 'replace')
			filenameES.write(str(rigatransESencod)+"\n")
			filenameES.close()
		
				
			filenameES1 = open("text/translate_"+str(args["lang4"])+".txt", "a")
			filenameES1.write(str(rigatransESencod)+"\n" )
			filenameES1.close()
		

			filename = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") +'_eng.mp3'
			command = "flite -o "+"audio/"+filename+" -t "+"\""+(rigatransEN.text)+"\""
			subprocess.Popen(command, shell=True)
		


	except KeyboardInterrupt:

		print('interrupted!')
		
	command = "cowthink -f daemon 'CHECKMATE TO TRANSLATE IN PYTHON By Visi@n'"
	subprocess.Popen(command, shell=True)	
	

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
