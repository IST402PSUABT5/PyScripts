#!/bin/python/
from os import path as p
#This is importing the path module to find if file exist or not
#Array used for grabbing information about files that are uplaoded or not
result = False
harray = [("/home/user/wfsync/main.html"),
("/home/user/wfsync/about.html"),
("/home/user/wfsync/mission.html"),
("/home/user/wfsync/contact.html"),
("/home/user/wfsync/about.html")]

try:
 for fname in harray:
  if p.exists(fname):
   result = True
 if result == True:
  myfile = open('infopass.txt','w')#creates file that is writeable
  myfile.write('All files are accounted for')#writes to file
  myfile.close()#closes the file
 if result == False:
  myfile = open('infofail.txt','w')
  myfile.write("Some files are missing")
  myfile.close()
except IOError as e:
 print "Error:script error and files not found"
