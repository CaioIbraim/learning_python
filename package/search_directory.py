# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:50:34 2018

@author: 13125877
"""

import os

def getExtension(name):
   fileName, fileExtension = os.path.splitext(name)
   return fileExtension

def isExtensionPermited(extension):
   extensions = ['jpeg', 'jpg', 'mp3']
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
                   
lookupDirectory('C:\estudos_python\sessions\music')