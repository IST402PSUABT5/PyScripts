#!/bin/python/
from os import path as p
from email.mime.text import MIMEText
import smtplib
result = False #test value against checking files
#Array with files to be checked
harray = [("/home/user/wfsync/main.html"),
("/home/user/wfsync/about.html"),
("/home/user/wfsync/mission.html"),
("/home/user/wfsync/contact.html"),
("/home/user/wfsync/about.html")]
fromAddress = "nab5230@psu.edu"
toAddress = "nab5230@psu.edu"
Subject="Status of File Existence"
msgp=MIMEText('Files are all accounted for and are synced properly')
msgf=MIMEText('FIles are missing and must be checked to see sync problems')
msgp['Subject']='Subject'
msgf['Subject']='Subject'
msgp['From']=fromAddress
msgf['From']=fromAddress
msgp['To']=toAddress
msgf['To']=toAddress
try:
 s = smtplib.SMTP_SSL('authsmtp.psu.edu',465)
 for fname in harray:
  if p.exists(fname):
   result = True
 if result == True:
   s.sendmail(fromAddress,[toAddress],msgp.as_string())
   s.quit()
 if result == False:
  s.sendmail(fromAddress,[toAddress],msgf.as_string())
  s.quit()
except IOError as e:
 print"Failed cause of %s"%e.args[0]
