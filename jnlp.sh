#!/bin/bash

#script for resolve jnpl files problem with various java versions

if [ "$1" == "" ];
then
	echo "Usage ./jnlp.sh [-noclear][local arquive]"
	echo "Example: ./jnpl.sh [-noclear] ~/Downloads/teste.jnpl"
	echo "-noclear : No open windows process of clear java temps"
else
	if [ "$1" == "-noclear" ];
	then
		#execute .jnpl file
		$JAVA_HOME/bin/javaws $2
	else
	  #clear temp java
	  $JAVA_HOME/bin/javaws -viewer
		#execute .jnpl file
	  $JAVA_HOME/bin/javaws $1
	fi
fi
