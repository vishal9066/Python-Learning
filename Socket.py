#Sockets: used to connect port and ip
import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

#to run
#nc -nvlp 7777