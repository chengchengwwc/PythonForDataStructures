# -*- coding: utf-8 -*-

#@author: weicheng

#@file: node.py

#@time: 2018/07/29

class Node(object):

    def __init__(self,data,next=None):
        self.data = data
        self.next = next
