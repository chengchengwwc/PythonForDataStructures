# -*- coding: utf-8 -*-

#@author: weicheng

#@file: cashier.py

#@time: 2018/07/29

from DataStructures.Market.linkedqueue import LinkedQueue


class Cashier(object):

    def __init__(self):
        self._totalCustomerWaitTime = 0
        self._customersServed = 0
        self._currentCustomer = None
        self._queue = LinkedQueue()


    def addCustomer(self,c):
        self._queue.add(c)

    def serverCustomers(self,currentTime):
        if self._currentCustomer is None:
            if self._queue.isEmpty():
                return
            else:
                self._currentCustomer = self._queue.pop()
                self._totalCustomerWaitTime += currentTime - self._currentCustomer.arrivalTime
                self._customersServed += 1
        self._currentCustomer.serve()
        if self._currentCustomer.amountOfServiceNeeded() == 0:
            self._currentCustomer = None


    def __str__(self):
        result = str(self._customersServed)
        if self._customersServed != 0:
            aveWaitTime = self._totalCustomerWaitTime/self._customersServed
            result += str(len(self._queue)) + "\n" + aveWaitTime
        return result










