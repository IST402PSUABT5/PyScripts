#!/bin/python
#
#This will log the entries when the admin has signed on and when he has modified files. This will be logged to a MYSQL database
import datetime,os.path as p,MySQLdb as sql
#This is importing the needed functions for python to execute and log to database
db = sql.connect("cloud","root","root","logdb")
cur = db.cursor()
try:

