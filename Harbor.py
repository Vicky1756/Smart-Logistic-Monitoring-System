class Harbor:
    countHarbor = 0
    def __init__(self,name):
        self.name = name
        if (Harbor.countHarbor == 0):
            self.country = ["India", "Indonesia", "Hong Kong"]
        elif (Harbor.countHarbor == 1):
            self.country = ["Philipine", "Singapore", "Sri Lanka"]
        elif (Harbor.countHarbor == 2):
            self.country = ["Egypt", "Congo", "Madagascar"]
        Harbor.countHarbor += 1