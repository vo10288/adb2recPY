#!/bin/bash
 
echo "you chose Screenshot"
echo "press ctrl-c to interrrupt" 
screenshot=$(date +%Y%m%d%H%M%S)


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
	adb shell screencap /sdcard/${x}.png
	adb pull /sdcard/${x}.png screenshot/$screenshot/${x}.png
	cp screenshot/$screenshot/${x}.png temp.png
	ls screenshot/$screenshot/${x}.png
	cp temp.png temp1.png
	adb shell rm /sdcard/${x}.png
	x=$[$x+1]
				
    done
exit
