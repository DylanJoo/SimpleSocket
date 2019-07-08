# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 00:14:32 2018

@author: DYLAN
"""
import socket

class client():

    def __init__(self):
        self.get_connect()
        
    def get_connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('52.90.188.77', 8888))
 
    def send(self, msg):
        self.s.send(msg.encode('utf-8'))

    def get_recieve(self):
        data = self.s.recv(1024)
        data.decode('utf-8')
        return data
