import time


map = {0:0}
indivAreas = []
distance = 0.0
filename = ""

def main():
    global filename
    global distance
    numOfFiles = int(input("How many files will you be analyzing today? (Please input a positive integer.) "))
    while numOfFiles > 0:
        readFile()
        calculate()
        print("Total Distance Traveled in file ", filename, ": ", roundDistance(), " miles (assuming the units were mph)\n\n")
        numOfFiles -= 1
    print("\n\n\nThe program will automatically close in 40 seconds.")
    time.sleep(40)


def readFile():
    global filename
    filename = input("What is the name of your file?\n(Input without file extension; file extension is assumed to be .txt)\nIf no file name is specified, the filename will be assumed as \"Speeds\"\n")
    if filename == "":
        filename = "Speeds"
    filename += ".txt"
    global map
    file = open(filename)
    line = file.readline()
    while line:
        arr = line.split(",")
        map[float(arr[0])] = float(arr[1])
        line = file.readline()


def calculate():
    global map
    global distance
    global indivAreas
    indivAreas = []
    distance = 0.0
    time = 0.008333333
    d = 1.0
    while d <= 30.0:
        areaTemp = 0.0
        prevHeight = map[d-0.5]
        currentHeight = map[d]
        if prevHeight < currentHeight:
            areaTemp = (time * prevHeight) + (time * (currentHeight - prevHeight) * 0.5)
        elif currentHeight < prevHeight:
            areaTemp = (time * currentHeight) + (time * (prevHeight - currentHeight) * 0.5)
        elif currentHeight == prevHeight:
            areaTemp = time * currentHeight
        indivAreas.append(areaTemp)
        d += 0.5
    totAreaTemp = 0.0
    for d in indivAreas:
        totAreaTemp += d
    distance = totAreaTemp


def roundDistance():
    global distance
    return round(distance,3)


main()