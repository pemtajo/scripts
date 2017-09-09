#!/bin/bash
<<<<<<< HEAD
cp -R /media/cdrom/ /tmp/
tar zxpf /tmp/cdrom/
=======

#incomplete script for configure vmtools in vmware
cp -R /media/cdrom/ /tmp/
cd /tmp/cdrom
tar zxpf
>>>>>>> a8340dafdbb60b93e7f43eddcadcebcb79a7d560

./tmp/cdrom/vmware-tools-distrib/vmware-install.pl
rm -R /tmp/cdrom
