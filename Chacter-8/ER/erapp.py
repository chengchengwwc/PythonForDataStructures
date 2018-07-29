# -*- coding: utf-8 -*-

#@author: weicheng

#@file: erapp.py

#@time: 2018/07/29


from DataStructures.ER.ermodel import ERModel,Patient,Condition



class ERView(object):

    def __init__(self,model):
        self._model = model


    def run(self):
        pass

    
    def treatNext(self):
        if getattr(self._model,"isEmpty"):
            print ("No one ")
        else:
            patient = getattr(self._model,"treatNext")
            print (patient)

    def treatAll(self):
        if getattr(self._model,"isEmpty"):
            print ("No ")
        else:
            while not getattr(self._model,"isEmpty"):
                self.treatNext()


    def _schedule(self):
        name = input("Name")
        condition = self._getCondition()
        self._model.schedule(Patient(name,condition))

    def _getCondition(self):
        menu="1,2,3"
        number = self._getCommand(3,menu)
        return Condition(number)



    def _getCommand(self,high,menu):
        promt = "Enter a number"
        commandPage = list(map(str,range(1,high+1)))
        error = "Error number must be 1"
        while True:
            print (menu)
            command = input(promt)
            if command in commandPage:
                return int(command)
            else:
                print (error)

def main():
    model = ERModel()
    view = ERView(model)
    view.run()


if __name__ == "__main__":
    main()