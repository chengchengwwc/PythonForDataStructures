# -*- coding: utf-8 -*-

#@author: weicheng

#@file: abstraclist.py

#@time: 2018/08/04


from abstractcollection import Abstractcollection


class AbstractList(Abstractcollection):

    def __init__(self,sourceCollection):
        self._modCount = 0
        Abstractcollection.__init__(self,sourceCollection)

    def getModCount(self):
        return self._modCount

    def incModCount(self):
        self._modCount += 1

    def index(self,item):
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError("{} is not in list".format(position))

    def remove(self,item):
        position = self.index(item)
        self.pop(position)

    def add(self,item):
        self.insert(len(self),item)

    def append(self,item):
        self.add(item)




