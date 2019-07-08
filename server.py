# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 00:14:32 2018

@author: DYLAN
"""
import socket

class server():

     def __init__(self):
          self.get_connect()
          self.get_accept()

          
     def get_connect(self):
          self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          self.s.bind(('0.0.0.0', 8888))
          self.s.listen(5)
          
     def get_accept(self):
          self.conn, addr = self.s.accept()
          print('現在連接位址：', addr)
          
     def get_recieve(self):
          data = self.conn.recv(1024)
          data = data.decode('utf-8')
          return data
     
     def close(self):
          self.s.close()
          self.conn.close()

     def send(self, data):
          data = data.encode('utf-8')
          self.conn.send(data)

