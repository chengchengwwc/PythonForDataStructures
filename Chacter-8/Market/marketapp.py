# -*- coding: utf-8 -*-

#@author: weicheng

#@file: marketapp.py

#@time: 2018/07/29


from DataStructures.Market.marketmodel import MarketModel


def main():
    lengthOfSimulation = int(input("Enter the total running time: "))
    averageTimePerCus = int(input("Enter the average processing time per customer: "))
    probabilityOfNewArrival = float(input("Enter the probability of a new arrival: "))
    if lengthOfSimulation <1 or lengthOfSimulation > 1000:
        print ("larget or small")

    elif averageTimePerCus <=0 or averageTimePerCus >= lengthOfSimulation:
        print ("BAD")

    elif probabilityOfNewArrival <= 0 or probabilityOfNewArrival >1
        print ("DFDF")
    else:
        model  = MarketModel(lengthOfSimulation,averageTimePerCus,probabilityOfNewArrival)
        model.runSimulation()
        print (model)

if __name__ == "__main__":
    main()


