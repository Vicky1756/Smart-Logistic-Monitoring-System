class Set_path:
    def __init__(self,name,placetoplace,distance):
        self.name = name
        self.placetoplace =[]
        self.distance = []
        self.placetoplace.append(placetoplace)
        self.distance.append(distance)
    def update(self,placetoplace,distance):
        self.placetoplace.append(placetoplace)
        self.distance.append(distance)