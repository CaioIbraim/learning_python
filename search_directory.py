import os

def getExtension(name):
   fileName, fileExtension = os.path.splitext(name)
   return fileExtension

def isExtensionPermited(extension):
   extensions = ['mp3']
   for x in extensions:
       if extension[:1] == '.':
           if extension[1:].lower() == x:
               return True
       elif extension.lower() == x:
           return True
   return False


def lookupDirectory(path):
   if os.path.isdir(path):
       files = os.listdir(path)
       for i in files:
           if i + '/' != 'windows/':
               if os.path.isdir(path + i + '/'):
                   lookupDirectory(path + i + '/')
               if isExtensionPermited(getExtension(i)) == True:
                   print(i)
