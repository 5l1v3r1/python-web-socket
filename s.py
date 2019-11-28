#!/usr/bin/python

#################
# Python Socket #
# By FilthyRoot #
#################

from socket import *
s = socket(AF_INET, SOCK_STREAM,SOL_TCP)
port = 1337
html = '<title>Hacked by FilthyRoot</title><body bgcolor="black"><font color="white"><center><pre><img src="https://media.giphy.com/media/VUC9YdLSnKuJy/source.gif" style="width:400px;"><br><br>Hacked by FilthyRoot<br>Sora Cyber Team<br><br>SabaExplo<font color="red">IT</font> Pwnd?<br><i><br><a href="http://instagram.com/khidhiribrhm_">Indonesian Hacker Rulez</a></i>'
server = ('0.0.0.0', port)

s.bind(server)
s.listen(5)
print "Running on port : "+str(port)
while(True):
	c,addr = s.accept()
	print addr
	c.recv(1024)
	c.send('HTTP/1.0 200 OK\n')
	c.send('Server: Jogjakarta Hacker Link\n')
	c.send('Content-Type: text/html\n')
	c.send('\n')
	c.send(str(html))
	c.close()
s.close()