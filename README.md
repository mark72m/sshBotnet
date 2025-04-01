# sshBotnet

The Morris Worm includes
forcing common usernames and passwords against the remote shell (RSH)
service as one of its three attack vectors. 

RSH[Remote Shell] helps in remotely connecting to a machine and manage it by 
performing a series of terminal commands on the host.

The Secure Shell (SSH) protocol has since replaced RSH by
combining RSH with a public-key cryptographic scheme in order to secure the
traffic. However, this does very little to stop the same attack vector by forcing
out common user names and passwords. SSH Worms have proven to be very
successful and common attack vectors

SSH Worm that brute forces user credentials against a target       
wait and match for an expected output before sending further
input commands.

To connect to our SSH machine at IP Address, 127.0.0.1, the application first asks us to confirm
the RSA key fingerprint. In this case, we must answer, “yes” before continuing.
Next, the application asks us to enter a password before granting us a command prompt. 
Finally, we execute our command uname –v to determine the
kernel version running on our target.  

Pexpect has the ability to interact with programs, watch for
expected outputs, and then respond based on expected outputs. This makes
it an excellent tool of choice for automating the process of brute forcing SSH
user credentials.
