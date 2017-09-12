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

from optparse import OptionParser


parser = OptionParser("usage: %prog [options] folder")
parser.add_option("-n", "--noAlbum", dest="createAlbum", action="store_false", default=True, help="No create Albuns")
parser.add_option("-r", "--reset", dest="reset", action="store_true",default=False, help="reset the files to default directory")
parser.add_option("-o", "--onlyReset", dest="onlyReset", action="store_true",default=False, help="Only reset the files to default directory, and done")
parser.add_option("-v", "--verbose", dest="verbose", action="store_true",default=False, help="Show all steps")
parser.add_option("-a", "--artistUnknown", dest="artist", action="store",default='Unknown', help="Set the name of artist in files with artist None")

(options, args) = parser.parse_args()

default = args[0]

None_artist=options.artist

def changeNoneArtistAndCreateFolders(defaultFolder, artistDefault):
    for arquivo in glob.glob(defaultFolder+'*.mp3'):
        audio = eyed3.load(arquivo)
        if audio is None:
            raise Error(arquivo + " Is not valid!!!")
            continue
        if audio.tag is None:
            audio.tag = eyed3.id3.Tag()
            audio.tag.file_info = eyed3.id3.FileInfo("foo.id3")
            print(arquivo + " as a invalid Tag!!!")
        if audio.tag.artist is None:
            audio.tag.artist=unicode(artistDefault, "UTF-8")
            audio.tag.save()
            if(options.verbose):
                print("Artist Name is changed to "+artistDefault+" in Arquive "+ os.path.basename(arquivo)+"!")
        folder=defaultFolder+str(audio.tag.artist)  
        if not os.path.exists(folder):
            os.makedirs(folder)
            if(options.verbose):
                print("Create folder artist "+ folder)
        
        os.rename(arquivo, folder+'/'+os.path.basename(arquivo))
        if(options.verbose):
            print("Arquive "+ os.path.basename(arquivo)+ " Changed!")

    print("All arquives are Update!")

def verifyAndCreateAlbuns(defaultFolder):
    folders = glob.glob(defaultFolder+'*/') 
    for folder in folders:
        createAlbum(folder)

def resetArquivesInFolders(root, folderFather):
    for folder in glob.glob(folderFather+'*/'):
        resetArquivesInFolders(root, folder)
    for arquive in glob.glob(folderFather+'*.*'):      
        os.rename(arquive, root+'/'+ os.path.basename(arquive))
    if(root!=folderFather):
        os.rmdir(folderFather)

def createAlbum(folder):
    arquives=glob.glob(folder+'*.mp3')
    for arquive in arquives:
        audio = eyed3.load(arquive)
        if audio.tag is None:
            audio.tag = eyed3.id3.Tag()
            audio.tag.file_info = eyed3.id3.FileInfo("foo.id3")
        if audio.tag.album is None:
            continue

        create=folder+str(audio.tag.album)  
        if not os.path.exists(create):
            os.makedirs(create)
            if(options.verbose):
                print("Create folder album "+ folder)
        
        os.rename(arquive, create+'/'+os.path.basename(arquive))

if(options.onlyReset or options.reset):
    resetArquivesInFolders(default, default)

if not options.onlyReset:
    changeNoneArtistAndCreateFolders(default, None_artist)
    if options.createAlbum:
        verifyAndCreateAlbuns(default)
