#!/bin/bash
cp -R /media/cdrom/ /tmp/
tar zxpf /tmp/cdrom/

./tmp/cdrom/vmware-tools-distrib/vmware-install.pl
rm -R /tmp/cdrom

