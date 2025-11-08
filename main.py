#START OF IMPORTATIONS
import logging, socket, json, os, re, time, asyncio, discord
from discord.ext.commands import Bot
from discord.ext import commands
from collections import defaultdict
from urllib.request import urlopen
from urllib.error import URLError
#END OF IMPORTATIONS

#START OF CALLS DISCORD
os.chdir(r'')
#END OF CALLS DISCORD

#GLOBALS
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'username'
token = ''
channel = '#name'
#END GLOBALS DECLARE

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\r\n".encode('utf-8'))
sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
sock.send(f"JOIN {channel}\r\n".encode('utf-8'))

print("STARTING!") #BOT HAS STARTED!

while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))

    elif len(resp) > 0:
        print(time.time(), resp)
