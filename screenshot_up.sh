#!/bin/bash
 
echo "you chose Screenshot"
echo "press ctrl-c to interrrupt" 
screenshot=$(date +%Y%m%d%H%M%S)
#WORKING_DIRECTORY="$HOME/02.computer_vision/04.video2ocr"

if [ -d screenshot ];
	then 
		echo "the directory exists";
		
	else
		echo "the directory does not exists"
		mkdir screenshot
fi
			

if [ -d screenshot/$screenshot ];
	then 
		echo "the directory exists";
		
	else
		echo "the directory does not exists"
		mkdir screenshot/$screenshot
fi

x=1
while [ $x -lt 1000000000 ]
	do
	adb exec-out screencap -p > screenshot/$screenshot/${x}.png
	adb shell input touchscreen swipe 300 300 500 1000
	cp screenshot/$screenshot/${x}.png temp.png
	ls screenshot/$screenshot/${x}.png
	cp temp.png temp1.png
	x=$[$x+1]
				
    done
exit
