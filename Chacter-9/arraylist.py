# -*- coding: utf-8 -*-

#@author: weicheng

#@file: arraylist.py

#@time: 2018/08/04

from arrays import Array
from abstraclist import AbstractList
from arraylistiterator import ArrayListIterator


class ArrayList(object):

    DEFAULT_CAPACITY = 10

    def __init__(self,sourceCollection=None):
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        AbstractList.__init__(self,sourceCollection)

    def _resize(self,array,logicalSzie):
        temp = None
        if len(array) == logicalSzie:
            temp = Array(2*len(array))

        elif logicalSzie <= .25 * len(array) and \
             len(array) >= ArrayList.DEFAULT_CAPACITY:
            temp = Array(round(.5 * len(array)))
        # None of the above
        else:
            return array
        # Copy items to new array
        for i in range(logicalSzie):
            temp[i] = array[i]
        return temp

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, item):
        return self._items[item]


    def clear(self):
        self._size = 0
        self._items = Array(ArrayList.DEFAULT_CAPACITY)

    def __setitem__(self, key, value):
        self._items[key] = value


    def insert(self, i, item):
        """Inserts the item at position i."""
        self._items = self._resize(self._items, len(self))
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                 self._items[j] = self._items[j - 1]
        self._items[i] = item
        self._size += 1
        self.incModCount()

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self._items[i]
        for j in range(i, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self.incModCount()
        self._items = self._resize(self._items, len(self))
        return item

    def listIterator(self):
        """Returns a list iterator."""
        return ArrayListIterator(self)














