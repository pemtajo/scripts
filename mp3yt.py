#!/usr/bin/python
# coding=UTF-8

import youtube_dl
import os

import sys
sys.path.append("../..")

arquivo = open('/home/pedro/baixar.txt','r')

command = 'youtube-dl --extract-audio --audio-format mp3 -o "~/Música/%(title)s.%(ext)s" '

texto = arquivo.readlines()
for linha in texto :
    print(linha)
    os.system(command+linha)
arquivo.close()

print("Todos os "+size(texto)+" foram baixados e convertidos com sucesso")