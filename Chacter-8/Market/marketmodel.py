# -*- coding: utf-8 -*-

#@author: weicheng

#@file: marketmodel.py

#@time: 2018/07/29

from DataStructures.Market.cashier import Cashier
from DataStructures.Market.customer import Customer


class MarketModel(object):

    def __init__(self,lengthOfSimulation,averageTimePerCus,probabilityOfNewArrival):
        self._probabilityOfNewArrival = probabilityOfNewArrival
        self._lengthOfSimulation = lengthOfSimulation
        self._averageTimePerCus = averageTimePerCus
        self._cashier = Cashier()

    def runSimulation(self):
        for currentTime in range(self._lengthOfSimulation):
            customer = Customer.generateCustomer(
                self._probabilityOfNewArrival,
                currentTime,
                self._averageTimePerCus
            )
            if customer != None:
                self._cashier.addCustomer(customer)
            self._cashier.serverCustomers(currentTime)

    def __str__(self):
        return str(self._cashier)



