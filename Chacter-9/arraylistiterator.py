# -*- coding: utf-8 -*-

#@author: weicheng

#@file: arraylistiterator.py

#@time: 2018/08/04


class ArrayListIterator(object):


    def __init__(self,backingStore):
        self._backingStore = backingStore
        self._modCount = self._backingStore.getModCount()
        self.first()

    def first(self):
        self._cursor = 0
        self._lastItemPos = -1

    def hasNext(self):
        return self._cursor <len(self._backingStore)

    def next(self):

        if not self.hasNext():
            raise ValueError("DO not have next")

        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("illegal modification of backing store")

        self._lastItemPos = self._cursor
        self._cursor += 1
        return self._backingStore[self._lastItemPos]


    def last(self):
        self._cursor = len(self._backingStore)
        self._lastItemPos = -1

    def hasPrevious(self):
        return self._cursor > 0


    def previous(self):
        if not self.hasPrevious():
            raise ValueError("DO not hava previous")

        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("illegal modification of backing store")

        self._cursor -= 1
        self._lastItemPos = self._cursor
        return self._backingStore[self._lastItemPos]


    def replace(self,item):
        if self._lastItemPos == -1:
            raise AttributeError("The current position is undefined")

        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("illegal modification of backing store")

        self._backingStore[self._lastItemPos] = item
        self._lastItemPos = -1

    def insert(self,item):
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("illegal modification of backing store")

        if self._lastItemPos == -1:
            self._backingStore.add(item)

        else:
            self._backingStore.insert(self._lastItemPos,item)
            self._lastItemPos = -1
        self._modCount += 1


    def remove(self):
        if self._lastItemPos == -1:
            raise AttributeError("The current position is undefined")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("illegal modification of backing store")
        self._backingStore.pop(self._lastItemPos)
        if self._lastItemPos < self._cursor:
            self._cursor -= 1
        self._modCount += 1
        self._lastItemPos = -1



































