# -*- coding: utf-8 -*-

#@author: weicheng

#@file: node.py

#@time: 2018/08/04


class Node(object):

    def __init__(self,data,next=None):
        self.data = data
        self.next = next



class TwoWayNode(Node):

    def __init__(self,data=None,previous=None,next=None):
        Node.__init__(self,data,next)
        self.previous = previous


