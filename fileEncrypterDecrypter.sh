#!/bin/bash

echo "This is a simple file encrypter/decrypter"
echo "Please choose what you want to do"

choice="Encrypt Decrypt"

select option in $choice; do
        if [ $REPLY = 1 ];
then
        gpg -c $1
	echo "File encrypted"
	exit 0
else
        gpg -d $1
	echo "File decrypted"
	exit 0 
fi

done
