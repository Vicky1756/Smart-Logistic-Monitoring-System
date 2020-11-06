class Environment:
    countAirport = 0
    countHarbor = 0
    CountTrain = 0
    def __init__(self):
        self.country = []
    def airport(self, name):
        self.name = name
        if (Environment.countAirport == 0):
            self.country = ["USA", "UK", "Italy"]
        elif (Environment.countAirport == 1):
            self.country = ["Wakanda", "Germany", "USSR"]
        elif (Environment.countAirport == 2):
            self.country = ["Brazil", "Argentina", "Ireland"]
        Environment.countAirport += 1

    def print(self):
        print(self.country)
    def harbor(self, name):
        self.name = name
        if (Environment.countHarbor == 0):
            self.country = ["India", "Indonesia", "Hong Kong"]
        elif (Environment.countHarbor == 1):
            self.country = ["Philipine", "Singapore", "Sri Lanka"]
        elif (Environment.countHarbor == 2):
            self.country = ["Egypt", "Congo", "Madagascar"]
        Environment.countHarbor += 1

    def train_station(self, name):
        self.name = name
        if (Environment.countTrain == 0):
            self.country = ["Vietnam", "China", "Laos"]
        elif (Environment.countTrain == 1):
            self.country = ["Hungary", "Austria", "Myanmar"]
        elif (Environment.countTrain == 2):
            self.country = ["Bulgaria", "Poland", "Latvia"]
        Environment.countTrain += 1