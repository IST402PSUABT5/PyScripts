#!/bin/python/
#Author Nicholas Blair
#Checker:Abishai Rajan
#Professor:Joe Oakes
#Date:December 8, 2013
#Purpose: The purpose of this program is to check and see if the files are all
#present and were synced properly
from os import path as p#this imports the path moudle to allow seraching of file
from email.mime.text import MIMEText#email module being ported in to allow sening of emails
import smtplib#the library for smtp
import MySQLdb as sql
result = False #test value against checking files
#Array with files to be checked against for email to be sent
harray = [("/home/user/wfsync/main.html"),
("/home/user/wfsync/about.html"),
("/home/user/wfsync/mission.html"),
("/home/user/wfsync/contact.html"),
("/home/user/wfsync/about.html")]
fromAddress = "nab5230@psu.edu"#Address of the sender
toAddress = "nab5230@psu.edu"#Address of the recipent
Subject="Status of File Existence"#Subject title that will be in the email
msgp=MIMEText('Files are all accounted for and are synced properly')#files are present message set
msgf=MIMEText('FIles are missing and must be checked to see sync problems')#Files are missing message set
msgp['Subject']='Subject'
msgf['Subject']='Subject'
msgp['From']=fromAddress#If message passes will use the fromAddress
msgf['From']=fromAddress#If message fails will use the form Address
msgp['To']=toAddress
msgf['To']=toAddress
#try catch statement that allows us to catch errors within the code
try:
 con = sql.connect('localhost','root','root','logdb')
 cur = con.cursor()
 cur.execute("DROP TABLE IF EXISTS eventlog")
 cur.execute("CREATE TABLE eventlog(EventId INT NOT NULL AUTO_INCREMENT,PRIMARY KEY(EventId),EventName VARCHAR(2),EventStatus VARCHAR(2))")
#This is using the SSL to send the email
 s = smtplib.SMTP_SSL('authsmtp.psu.edu',465)#using protcol 465
 for fname in harray:
  if p.exists(fname):#This is using the subprocess module to check if files are there or not
   result = True
 if result == True:
#sends message out to recipent if results proven true if all files are located there
   s.sendmail(fromAddress,[toAddress],msgp.as_string())
   s.quit()
   cur.execute("INSERT INTO eventlog (EventId,EventName,EventStatus)VALUES (NULL,'ES','EP')")
   cur.execute("INSERT INTO eventlog (EventId,EventName,EventStatus) VALUES (NULL,'FS','FP')")
   cur.execute("SELECT * FROM eventlog")
   con.commit()
   con.close()
 if result == False:
#Will send a failure email to reciepent to inform them of missing files
  s.sendmail(fromAddress,[toAddress],msgf.as_string())
  cur.exexute("INSERT INTO eventlog VALUES (NULL,'ES','EF')")
  cur.execute("INSERT INTO eventlog VALUES (NULL,'FS','FF')")
  s.quit()
  con.close()
except IOError as e:
 print"Failed cause of %s"%e.args[0]
