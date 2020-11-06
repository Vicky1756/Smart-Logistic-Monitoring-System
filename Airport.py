class Airport:
    countAirport = 0
    def __init__(self,name):
        self.name = name
        if (Airport.countAirport == 0):
            self.country = ["USA", "UK", "Italy"]
        elif (Airport.countAirport == 1):
            self.country = ["Wakanda", "Germany", "USSR"]
        elif (Airport.countAirport == 2):
            self.country = ["Brazil", "Argentina", "Ireland"]
        Airport.countAirport += 1