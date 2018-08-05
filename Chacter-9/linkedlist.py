# -*- coding: utf-8 -*-

#@author: weicheng

#@file: linkedlist.py

#@time: 2018/08/04


from node import TwoWayNode
from abstraclist import AbstractList


class LinkedList(AbstractList):

    def __init__(self,sourceCollection):
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        AbstractList.__init__(self,sourceCollection)

    def _getNode(self,i):
        if i == len(self):
            return self._head
        elif i == len(self) -1:
            return self._head.previous

        prode = self._head.next
        while i > 0:
            prode = prode.next
            i -=1
        return prode

    def __getitem__(self, item):
        if item <0 or item >= len(self):
            raise IndexError("BAD")
        return self._getNode(item).data


    def clear(self):
        self._size = 0
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head


    def __setitem__(self, key, value):
        if key < 0 or key >= len(self):
            raise IndexError("BAD")
        self._getNode(key).data = value


    def insert(self,i,item):
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        theNode = self._getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self._size += 1
        self.incModCount()

    def pop(self, i=None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        theNode = self._getNode(i)
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self._size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        return LinkedList.ListIterator(self)



    class ListIterator(object):

        def __init__(self):
            raise Exception("BBBB")








