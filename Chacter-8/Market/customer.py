# -*- coding: utf-8 -*-

#@author: weicheng

#@file: customer.py

#@time: 2018/07/29

import random


class Customer(object):

    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival,
                         arrivalTime,
                         averageTimePerCustomer):
        """Returns a Customer object if the probability
        of arrival is greater than or equal to a random number.
        Otherwise, returns None, indicating no new customer.
        """
        if random.random() <= probabilityOfNewArrival:
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None




    def __init__(self,arrivalTime,serviceNeeded):
        self._arrivalTime = arrivalTime
        self._amountOfServiceNeeded = serviceNeeded


    def arrivalTime(self):
        return self._arrivalTime

    def amountOfServiceNeeded(self):
        return self._amountOfServiceNeeded

    def server(self):
        self._amountOfServiceNeeded -= 1










