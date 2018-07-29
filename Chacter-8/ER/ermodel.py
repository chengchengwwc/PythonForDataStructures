# -*- coding: utf-8 -*-

#@author: weicheng

#@file: ermodel.py

#@time: 2018/07/29

from DataStructures.ER.linkedprioritqueue import LinkPriorityQueue


class Condition(object):

    def __init__(self,rank):
        self._rank = rank

    def __eq__(self, other):
        return self._rank == other._rank


    def __lt__(self, other):
        return self._rank < other._rank

    def __le__(self, other):
        return self._rank <= other._rank

    def __str__(self):
        if self._rank == 1:  return "critical"
        elif self._rank == 2:return "serious"
        else:                return "fair"



class Patient(object):

    def __init__(self,name,condition):
        self._name= name
        self._condition = condition


    def __eq__(self, other):
        return  self._condition == other._conditon

    def __lt__(self, other):
        return self._condition < other._conditon

    def __le__(self, other):
        return self._condition <= other._conditon

    def __str__(self):
        return self._name + "\n" + self._condition



class ERModel(object):

    def __init__(self):
        pass

    def isEmpty(self):
        return True


    def schedule(self):
        pass


    def treatNext(self):
        pass







