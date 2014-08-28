#!/bin/bash
DIR=$(echo "$1"|ack "(imgur\.com\/a\/)([^\?]*)" --output='$2')
echo "Current name of the gallery is: $DIR"
echo -n "Enter new name (enter to use $DIR): "
read CUSTOM_DIR

case "$CUSTOM_DIR" in
	"") ;;
	*)	DIR="$CUSTOM_DIR ($DIR)"
		echo "Using new name of gallery: $DIR"
		;;
esac

if [ -e "$DIR" ]
then
	if [ -d "$DIR" ]
	then
		echo "Directory already exists"
	else
		echo "There is a file by that name. Get rid of it"
		exit	
	fi
else	
	if [ -w "$DIR" ]
	then
		mkdir "$DIR"
	else
		echo "Don't have permission to write to $DIR"
		exit
	fi
fi
wget "$1" -O - -o /dev/null|ack "(<a href=\"\/\/)(i\.imgur\.com\/.{7}\.(jpg|png|jpeg))" --output='$2'|sed 's/^/http:\/\//'|aria2c -x 16 -s 16 -i - -d "$DIR"
