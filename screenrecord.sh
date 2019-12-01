#!/bin/bash
 
echo "you chose Screenrecord"
echo "press ctrl-c to interrrupt" 
screenrecord=$(date +%Y%m%d%H%M%S)
#WORKING_DIRECTORY="$HOME/02.computer_vision/04.video2ocr"

if [ -d screenrecord ];
	then 
		echo "the directory exists";
		
	else
		echo "the directory does not exists"
		mkdir screenrecord
fi
			

if [ -d screenrecord/$screenrecord ];
	then 
		echo "the directory exists";
		
	else
		echo "the directory does not exists"
		mkdir screenrecord/$screenrecord
		
fi

x=1
while [ $x -lt 1000000000 ]
do
	adb shell screenrecord /sdcard/${x}.mp4
	adb pull /sdcard/${x}.mp4 screenrecord/$screenrecord/${x}.mp4
	ls screenrecord/$screenrecord/${x}.mp4
	adb shell rm /sdcard/${x}.mp4
	x=$[$x+1]
done
exit	
