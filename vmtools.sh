#!/bin/bash

#incomplete script for configure vmtools in vmware
cp -R /media/cdrom/ /tmp/
cd /tmp/cdrom
tar zxpf

cd vmware-tools-distrib
./vmware-install.pl
cd
rm -R /tmp/cdrom
