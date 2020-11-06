class Warehouse:
    def __init__(self,name ,temperature ,capacity ):
        self.row = []
        self.checkstock  = 0
        self.name       = name
        self.temperature = temperature
        self.capacity    = capacity
    def addRow(self):
        self.row.append([])
    def order(self,num):
        self.order = num
    def status(self):
        self.process = 0
        self.success = 0
        self.fail    = 0
    # def addProduct(self,number =0 ,r = 0 ):
    #     self.number = number
    #     self.process += 1
    #     Warehouse.currentPos = self
    #     if self.temperature >= self.min_temp and self.temperature <= self.max_temp :
    #         self.process += 1
    #         for i in range(number):
    #             self.row[r].append(self.name_item)
    #         else:
    #             self.fail += 1
