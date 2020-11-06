from Harbor import Harbor
from Airport import Airport
from Warehouse import Warehouse
from Truck import Truck
from Train_station import Train_station
from Create_item import Create_item
from Set_path import Set_path
import re
fromPattern = r'from(.*?)to '   # String ระหว่าง from .... to
toPattern = r'(?: to)(.*)'
patternImport = r'\s(\w+)'

output = open("log_test.txt","w")
harbordict = {}
airportdict = {}
warehousedict = {}
truckdict = {}
traindict = {}
pathdict  = {}
itemdict  = {}
stock= [] #เก็บorderแต่ละอัน
num = 0 #number of warehouse that has been created
check = r'“(.*?)”' #check pattern city
check2 = r'\((.*?)\)' #check comma
numOnly = r'[0-9]+' #check number
count = 0 # count the order
def changeWord(line):
    result = []
    fromm = re.search(fromPattern, line)
    fromm = fromm.group()
    fromm = fromm[5:-4]
    too = re.search(toPattern, line)
    too = too.group()
    too = too[4:]
    result.append(fromm)
    result.append(too)
    return result
def cityCountry(country):
    for city in harbordict:
        if country in city.country:
            return city.name
    for city in airportdict:
        if country in city.country:
            return city.name
    for city in traindict:
        if country in city.country:
            return city.name
def checkPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = checkPath(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
def checkTruck(OrderLine):
    weightList = []
    result = []
    for line in OrderLine:
        # print(line)
        num_item = line.split()[1]
        item = line.split()[2]
        weight = int(num_item) * int(itemdict[item].weight)
        weightList.append(weight)
    maxWeight = max(weightList)
    for truck in truckdict:
        result = []
        if int(truckdict[truck].min_load) <= maxWeight <= int(truckdict[truck].max_load):
            result.append(True)
            result.append(truck)
            return result
        else:
            pass
        result.append(False)
        result.append("Reject")
    return result
def checkTemp(OrderLine):
    for line in OrderLine:
        splitLine = line.split()
        print(splitLine)
        change = changeWord(line)
        if "Import" in line:
            print(line)
            print("======")
            if int(itemdict[splitLine[2]].min_temp) <= int(warehousedict[change[1]].temperature) <= int(itemdict[splitLine[2]].max_temp):
                return True
            else:
                return False
        elif "Transfer" in line:
            if int(itemdict[splitLine[2]].min_temp) <= int(warehousedict[change[1]].temperature) <= int(itemdict[splitLine[2]].max_temp):
                return True
            else:
                return False
        elif "Export" in line:
            return True
def checkCap(OrderLine):
    for line in OrderLine:
        splitLine = line.split()
        print(splitLine)
        change = changeWord(line)
        if "Import" in line:
            print(line)
            print("======")
            if int(splitLine[1]) <= (int(warehousedict[change[1]].capacity) - int(splitLine[1])):
                return True
            else:
                return False
        elif "Transfer" in line:
            if (int(splitLine[1]) <= (int(warehousedict[change[1]].capacity) - int(splitLine[1]))) and (int(warehousedict[change[0]].capacity) >= (int(splitLine[1]))):
                return True
            else:
                return False
        elif "Export" in line:
            if int(warehousedict[change[0]].capacity) >= (int(splitLine[1])):
                return True
            else:
                return False

def operating(line,truckSelect):
    change = changeWord(line)
    if "Import" in line:
        cit = cityCountry(change[0])   # ชื่อเมือง ของประเทศส่งออก
        for truck in traindict:
            print(truck)

Setup = True

OrderLine = []
temp_weight = []
city_database = []


with open('input.txt',encoding="utf16") as f:
    content = f.readlines()
    for line in content:
        line = line.rstrip()
        if Setup == True:
            if "Harbor" in line:
                quote = re.findall(check,line)
                city = quote[0]
                harbordict[city] = Harbor(name=city)
                city_database.append(city)
            elif "Airport" in line:
                quote = re.findall(check,line)
                city = quote[0]
                airportdict[city] = Airport(name=city)
                city_database.append(city)
            elif "Warehouse" in line:
                quote = re.findall(check, line)
                city = quote[0]
                city_database.append(city)
                xxx = re.findall(check2, line)  # find temp and cap
                a = xxx[0].split(',')
                warehousedict[city] = Warehouse(name=city,temperature = a[0],capacity = a[1])
                num+= 1
            elif "Truck" in line:
                quote = re.findall(check, line)
                city = quote[0]
                city_database.append(city)
                xxx = re.findall(check2, line) #find min load,max load
                a = xxx[0].split(',')
                truckdict[city] = Truck(name=city,min_load =a[0],max_load =a[1])
            elif "Train_Station " in line:
                quote = re.findall(check, line)
                city = quote[0]
                city_database.append(city)
                traindict[city] = Train_station(name=city)
            elif "Set_path" in line:
                path_city = []
                line = line.split(' ')
                distance = line[-1]
                del line[0]  #ลบ Set_path
                del line[-1] #ลบ ระยาทาง
                # print(line)
                if len(line) > 2:
                    for index, x in enumerate(line):
                        # print (index,x)
                        if line[index] != line[-1]:
                            Sep_word = line[index] + " " + line[index+1]
                            if Sep_word in city_database:
                                path_city.append(Sep_word)
                            else:
                                path_city.append(x)
                else:
                    path_city = line
                # print(path_city)
                CityFrom = path_city[0]
                CityTo = path_city[1]
                if (CityFrom not in pathdict) and (CityTo in pathdict):
                    pathdict[CityFrom] = Set_path(name=CityFrom, placetoplace=CityTo, distance=distance)
                    pathdict[CityTo].update(placetoplace=CityFrom, distance=distance)
                elif (CityFrom in pathdict) and (CityTo in pathdict) :
                    pathdict[CityFrom].update(placetoplace=CityTo,distance=distance)
                    pathdict[CityTo].update(placetoplace=CityFrom,distance=distance)
                elif (CityFrom not in pathdict) and (CityTo not in pathdict) :
                    pathdict[CityFrom] = Set_path(name = CityFrom, placetoplace=CityTo, distance=distance)
                    pathdict[CityTo] = Set_path(name = CityTo, placetoplace=CityFrom, distance=distance)
                elif (CityFrom in pathdict) and (CityTo not in pathdict) :
                    pathdict[CityFrom].update(placetoplace=CityTo, distance=distance)
                    pathdict[CityTo] = Set_path(name = CityTo, placetoplace=CityFrom, distance=distance)

                # print("Creating Path : " + pathdict[CityFrom].name + " <--------> " + str(pathdict[CityFrom].placetoplace))
                # print("Distance : " + str(pathdict[CityFrom].distance))
                # print("Creating Path : " + pathdict[CityTo].name + " <--------> " + str(pathdict[CityTo].placetoplace))
                # print("Distance : " + str(pathdict[CityTo].distance))
            elif "Create_item" in line:
                quote = re.findall(check, line)
                item = quote[0]
                xxx = re.findall(check2, line)  # find min load,max load
                a = xxx[0].split(',')
                itemdict[item] = Create_item(name =item,min_temp =a[0],max_temp =a[1],weight =a[2])
            elif "Order" in line:
                output.writelines("Order 1:" + "\n")
                Setup = False

            # elif "Import" in line:
            #     num_item = line.split()[1]
            #     item = line.split()[2]
            #     beginning = line.split()[4] #ประเทศต้นทาง
            #     ending = line.split()[6] #จุดหมาย
            # elif "Export" in line:
            #     num_item = line.split()[1]
            #     item = line.split()[2]
            #     beginning = line.split()[4]  # ประเทศต้นทาง
            #     ending = line.split()[6]  # จุดหมาย
            # elif "Transfer" in line:
            #     num_item = line.split()[1]
            #     item = line.split()[2]
            #     beginning = line.split()[4]  # ประเทศต้นทาง
            #     ending = line.split()[6]  # จุดหมาย

        elif Setup == False:
            if "Order" not in line:
                OrderLine.append(line)

            elif "Order" in line:
                number = re.findall(numOnly,line)

                # print(OrderLine)
                TruckTest = checkTruck(OrderLine)  # Return ชื่อTruck หรือ Reject
                # print(TruckTest)
                if TruckTest[0] == False:
                    output.writelines("Reject" + "\n")
                elif TruckTest[0] == True:                      # Check Truck Avaliable
                    output.writelines(TruckTest[1] + "\n")
                    TempTest = checkTemp(OrderLine)
                    if TempTest == True:                        # Check Tempertature Avaliable
                        CapTest = checkCap(OrderLine)
                        if CapTest == True:                     # Check Capacity Avaliable
                            for process in OrderLine:
                                operating(process,TruckTest[1])

                        else:
                            print("Fail")
                    else:
                        print("Fail")





                output.writelines("Order " + str(number[0]) + ":" + "\n")
                OrderLine = []
                # if checkTruck() != "Reject":
                #
                #     print(checkTruck())
                #
                #
                # elif checkTruck() == "Reject":
                #     pass
                # progress(OrderLine)
            # OrderLine = []






# print(itemdict)
# print(itemdict['lightsaber'].weight)