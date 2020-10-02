#!/usr/bin/python

import pexpect


PROMPT = ['#','>>>','>','\$']

def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print (child.before) #this command print the output of our command executed on target machine 

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
	child.expect(PROMPT)
	return child



def main():
	host = raw_input("[+] Enter Target IP Address:")
	user = raw_input("[+] Enter SSH User Name: ")
	password = raw_input("[+] Enter SSH Password:")
	child = connect(user,host,password)
	send_command(child,'ls;ps')

main()