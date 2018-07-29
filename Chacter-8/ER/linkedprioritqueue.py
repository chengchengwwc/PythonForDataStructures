# -*- coding: utf-8 -*-

#@author: weicheng

#@file: linkedprioritqueue.py

#@time: 2018/07/29


from DataStructures.Market.linkedqueue import LinkedQueue
from DataStructures.Market.node import Node


class LinkPriorityQueue(LinkedQueue):

    def __init__(self,sourceCollection=None):
        LinkedQueue.__init__(sourceCollection)


    def add(self,item):
        if self.isEmpty() or item >=self._rear.data:
            LinkedQueue.add(self,item)
        else:
            probe = self._front
            trailer = None
            while item >= probe.data:
                trailer = probe
                probe = probe.next
            newNode = Node(item,probe)
            if trailer is None:
                self._front = newNode
            else:
                trailer.next = newNode
            self._size += 1




