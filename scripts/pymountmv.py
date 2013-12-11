#!/usr/bin/python/
import subprocess as pro,pexpect as pxp,sys,os
ip = 'ssh 192.168.56.109'
commount = [
'sudo',
'mount',
'/home/user/owncloud/'
]
comumount =[
'sudo',
'umount',
'/home/user/owncloud/'
]
commv =[
'sudo'
'cp',
 'main.html',
'about.html',
'mission.html',
'contact.html',
'style.css',
'/home/user/owncloud/backup/'
]
try:
 if pro.call(commount):
  if px == pxp.spawn(ip):
   px.expect('Username:');
   px.sendline('tux_admin');
   px.expect('Password:');
   px.sendline('master');
  for l in file('/proc/mounts'):
   if l[0] == '192.168.56.110/owncloud/files/webdav.php':
    pro.call(commv)
    if pro.call(commv):
     pro.call(comumount)
except IOError as e:
 print "error has occured in program"
 
