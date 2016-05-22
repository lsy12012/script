# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:42:02 2016

@author: dltkd
"""

import socket

HOST = ''     # 호스트를 지정하지 않으면 가능한 모든 인터페이스 의미
PORT = 50007  # 포트 지정
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data) # 받은 데이터를 그대로 클라이언트에 보냄
conn.close()