#!/usr/bin/python
# coding=UTF-8
# encoding=UTF-8
import eyed3
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("../..")
import glob

default='/home/pedro/Música/'

None_artist='Unknown'

def changeNoneArtistAndCreateFolders(defaultFolder, artistDefault):
    for arquivo in glob.glob(defaultFolder+'*.mp3'):
        audio = eyed3.load(arquivo)
        if audio.tag.artist is None:
            audio.tag.artist=unicode(artistDefault, "UTF-8")
            audio.tag.save()
            print("Artist Name is changed to "+artistDefault+" in Arquive "+ os.path.basename(arquivo)+"!")
        folder=defaultFolder+str(audio.tag.artist)  
        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Create folder "+ folder)
        
        os.rename(arquivo, folder+'/'+os.path.basename(arquivo))
        
        print("Arquive "+ os.path.basename(arquivo)+ " Changed!")

    print("All arquives are Update!")

def verifyAndCreateAlbuns():
    print
def resetArquivesInFolders():
    print


changeNoneArtistAndCreateFolders(default, None_artist)