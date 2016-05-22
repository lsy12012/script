# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:46:30 2016

@author: dltkd
"""

import socket

HOST = '127.0.0.1'  #localhost
PORT = 50007        #서버와 같은 포트를 사용함
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성
s.connect((HOST, PORT))
s.send(b'Hello, python') #문자를 보냄
data = s.recv(1024)  # 서버로 부터 정보를 받음
s.close()
print('Received', repr(data))