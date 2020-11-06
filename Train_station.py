class Train_station:
    countTrain = 0
    def __init__(self,name):
        self.name = name
        if (Train_station.countTrain == 0):
            self.country = ["Vietnam", "China", "Laos"]
        elif (Train_station.countTrain == 1):
            self.country = ["Hungary", "Austria", "Myanmar"]
        elif (Train_station.countTrain == 2):
            self.country = ["Bulgaria", "Poland", "Latvia"]
        Train_station.countTrain += 1