import os
import re
print 'Inhereting from fileCore!'
class FileCore():
    def __init__(self, debug=1):
        self.debug = debug

        if self.debug: print 'FileCore init'

        
    def query(self, path):
        if os.path.exists(path):
            return 1
        else:
            return 0

    def bundle(self):
        pass
    
    #get the file name from a path. ##jum## ##pyapor##
    def fileCoreFileName(self):
        fileName = os.path.split(self.filePath)
        fileName = str(fileName)
        if self.debug: print 'the fileName : ' + fileName[1]
        return fileName
        
    #get the path without the file name. ##jum##
    #Moves one branch up the file path. ##pyapor## ##jum##  
    def fileCoreLoc(self):
        fileLoc = os.path.split(self.filePath)
        locDir = fileLoc[0]
        fileName = fileLoc[1]
        if self.debug: print 'The location of' + fileName + 'is: ' + locDir
        return locDir
    
    def fileCorePathCreator(self, dir=[]):
        path=''
        for item in dir:
            path = os.path.join(path, item)
        path = '/' + path
        if  self.debug: print path
        return path
            
    #make a folder. ##jum## ##pyapor##
    def fileCoreMakeFolder(self, folderPath, folderName):
        fPath = os.path.join(folderPath, folderName)

	if self.query(fPath):
            if self.debug: print 'the folder' + folderName + ' already exists.'
            pass
	else:
            os.mkdir(folderPath + "/" + folderName)
	    if self.debug: print 'the folder' + folderName + ' has been created under : ' + folderPath
            
    #makes folders automatically inside the project folder. ##jum## ##pyapor##
    def fileCoreMakeProjFolder(self, path, projFolder, folders=[]):
	projFolderPath = os.path.join(path, projFolder)
	if self.debug: print "Project folder path : " +  projFolderPath

	if self.query(projFolderPath):
	    if self.debug: print 'the project folder ' + projFolderPath + 'already exists.'
	else:
            os.mkdir(projFolderPath)
            for item in folders:
                folder = projFolderPath + "/" + item
                if self.query(folder):
                    if self.debug: print folder + ' alreday exists.'
                    continue
                else:
                    createFolder =  os.mkdir(folder + '/' + item)
                    return createFolder
                
	    if self.debug: print 'the project folder ' + projFolderName + ' has been created under : ' + projFolderPath

    def parseUnWanted(self, fileList):
        
        if self.debug: print fileList
        parseList = []
        excluded = []
        for parse in fileList:
            if re.match('_', parse):
                excluded.append(parse)
            elif re.match('\.', parse):
                excluded.append(parse)
            else:
                parseList.append(parse)
        
        parseList.sort()        
        if self.debug: print parseList
        if self.debug: print ' is the list of parsed names.'
        if self.debug: print excluded
        if self.debug: print ' is the list of excluded names.'
        
        return parseList

    #Returns whether a folder is empty or not. ##pyapor##
    def fileCoreQueryDir(self, folderPath):
        if self.debug: print folderPath + ' is the folder path queried.'
        parseList = os.listdir(folderPath)
        dirList = self.parseUnWanted(parseList)
        if self.debug: print dirList
        if self.debug: print ' is a list of files of the folder path.'
        if dirList == [] :
            if self.debug: folderPath + " is empty."
            return True
        else:
            dirList = os.listdir(folderPath)
            dirList = str(dirList)
            if self.debug: print ('The list of files in ' + folderPath + ' is ' + dirList + '.')
            return False
    
    #Brings back a list of all of the files in a folder... this could probably be used later on to check if any files are missing. ##pyapor##  
    def fileCoreQueryDirList(self, folderPath):
        parseList = os.listdir(folderPath)
        dirList = self.parseUnWanted(parseList)
        if dirList == [] :
            return False
        else:
            dirList.sort()
            if self.debug: print dirList
            return dirList