#!/bin/python
#Author: Nick Blair
#Checker:
#Purpose: Provide logging to the database when user has logged in and when they chagned script files
#This will log the entries when the admin has signed on and when he has modified files. This will be logged to a MYSQL database
import datetime,os as p,MySQLdb as sql,sys,platform,time
#This is importing the needed functions for python to execute and log to database
conn = None #Will set the connection value default to none
username =  p.getlogin()#grabs who the user is currently logged in on the terminal
userlog = get_nix_login_time()#grabs current login time#This doesn't work need work around
filearray  = [('/home/user/scripts/lanfilecheck.py'),('/home/user/scripts/wanfilecheck.py'),('/home/user/scripts/pymountmv.py')]#aray of files that will be checked
filetime = p.getmtime(filearray)#checks the files in the array for the time of each
curtime =time.time()#This reads out all the times
timelasped = filetime - curtime# checks to see if time elapsed or not for file change
isttimelaspe = datetime.datetime.fromtimestamp(timelasped.strftime('%Y-%m-%d %H:%M:%S'))#This will convert the unix epoch(seconds) time to readable time
for x in filearray:
 if x == timelasped:
  x = filename
try:

 conn = sql.connect("cloud","root","root","logdb")#will connect to the MySQL database
 cur = db.cursor()#
#logger is a insert variable that will insert large values extracted from python into the mysql table 
#
 cur.execute("DROP TABLE IF EXISTS logs")

 if timelasped > 0:
  cur.execute( 'INSERT INTO logs VALUES(%s,%s,%s,%s)',(username,filename,userlog,isttimelaspe))
 cursor.execute('SELECT * FROM logs')
 res = cur.fetchall()
 with open ('dblog.txt','w') as l:
  for i in res:
   print i 
   f.write('%s/n' % str(i))
  
except Exception as e:
 print "Error occured was %s" %e.args[0]

finally:
 if con:
  con.close()
