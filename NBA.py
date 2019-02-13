import requests
import csv
import matplotlib.pyplot as plt
import json
import numpy as np


eightys = "1985,1986,1987,1988,1989"
ninetys = "1990,1991,1992,1993,1994,1995,1996,1997,1998,1999"
twoThousands = "2000,2001,2002,2003,2004,2005,2006,2007,2008,2009"
tens = "2010,2011,2012,2013,2014,2015,2016,2017,2018"
def averageHeight():
    with open("nba.csv") as file:
        playerList = []
        read = csv.reader(file)
        total80sPlayers = 0 # keeps track of how many players we loop through from decade
        total90sPlayers = 0
        totaltwoThousandsPlayers = 0
        totaltensPlayers = 0
        next(read) # skip the header of csv file
        total80s = 0 # keeps track of total inches of all players from decade
        total90s = 0
        totaltwoThousands = 0
        totaltens = 0
        for row in read:
            if row[12] in eightys:
                eightysHeight = (row[6].split("-"))
                inches = int(eightysHeight[0]) * 12 + int(eightysHeight[1]) # convert feet-inch format to inches
                total80s += inches
                playerList.append((row[1],inches,row[12],1980))
                total80sPlayers += 1
            if row[12] in ninetys:
                ninetysHeight = (row[6].split("-"))
                inches = int(ninetysHeight[0]) * 12 + int(ninetysHeight[1])
                total90s += inches
                playerList.append((row[1],inches,row[12],1990))
                total90sPlayers += 1
            if row[12] in twoThousands:
                twoThousandsHeight = (row[6].split("-"))
                inches = int(twoThousandsHeight[0]) * 12 + int(twoThousandsHeight[1])
                totaltwoThousands += inches
                playerList.append((row[1],inches,row[12],2000))
                totaltwoThousandsPlayers += 1
            if row[12] in tens:
                tensHeight = (row[6].split("-"))
                inches = int(tensHeight[0]) * 12 + int(tensHeight[1])
                totaltens += inches
                playerList.append((row[1],inches,row[12],2010))
                totaltensPlayers += 1
##            with open("nba3.csv","w") as outfile: use matlib
##                csv_out = csv.writer(outfile)
##                for row in playerList:
##                    csv_out.writerow(row)
        averageEighties = total80s/total80sPlayers
        averageNineties = total90s/total90sPlayers
        averageThousands = totaltwoThousands/totaltwoThousandsPlayers
        averageTens = totaltens/totaltensPlayers
        file.close()
     
        decades = (1980,1990,2000,2010)
        height = (averageEighties,averageNineties,averageThousands,averageTens)
        ypos = np.arange(len(decades))
        plt.bar(ypos,height, align = 'center', alpha = .5)
        plt.xticks(ypos,decades)
        plt.ylabel("Average Height in Inches")
        plt.title("Differences in Height over Decades")
        ax = plt.gca()
        ax.set_ylim([70,80]) # set limit of y axis
        plt.show()

    
        
                    
        
##        print(playerList)
##        print(total80s/total80sPlayers)
##        print(total90s/total90sPlayers)
##        print(totaltwoThousands/totaltwoThousandsPlayers)
##        print(totaltens/totaltensPlayers)

def averageYears():
    yearsList = []
    total80s = 0
    total90s = 0
    total00s = 0
    total10s = 0
    total80splayers = 0
    total90splayers = 0
    total00splayers = 0
    total10splayers = 0
    with open("nba.csv") as file:
        read = csv.reader(file)
        next(read)       
        for row in read:
            if row[12] in eightys:
                yearsList.append((row[1],row[10],1980))
                total80s += int(row[10])
                total80splayers += 1
            if row[12] in ninetys:
                yearsList.append((row[1],row[10],1990))
                total90s += int(row[10])
                total90splayers += 1
            if row[12] in twoThousands:
                yearsList.append((row[1],row[10],2000))
                total00s += int(row[10])
                total00splayers += 1
            if row[12] in tens:
                total10s += int(row[10])
                total10splayers += 1
                yearsList.append((row[1],row[10],2010))
##            with open("nba2.csv","w") as outfile: use matlib
##                csv_out = csv.writer(outfile)
##                for row in yearsList:
##                    csv_out.writerow(row)
        average80s = total80s/total80splayers
        average90s = total90s/total90splayers
        average00s = total00s/total00splayers
        average10s = total10s/total10splayers
        decades = (1980,1990,2000,2010)
        years = (average80s,average90s,average00s,average10s)
        ypos = np.arange(len(decades))
        plt.bar(ypos,years, align = 'center', alpha = .5)
        plt.xticks(ypos,decades)
        plt.ylabel("Average Years in the NBA")
        plt.title("Years in the NBA when Winning Player of the Week")
        #ax = plt.gca()
       # ax.set_ylim([70,80]) # set limit of y axis
        plt.show()
        file.close()

def averagePosition():
    back80s = 0
    front80s = 0
    back90s = 0
    front90s = 0
    back00s = 0
    front00s = 0
    back10s = 0
    front10s = 0   
    with open("nba.csv") as file:
        read = csv.reader(file)
        next(read)
        for row in read:
            if row[12] in eightys:
                if "G" in row[5]:
                    back80s += 1
                elif "F" or "C" in row[5]:
                    front80s += 1
            if row[12] in ninetys:
                if "G" in row[5]:
                    back90s += 1
                elif "F" or "C" in row[5]:
                    front90s += 1
            if row[12] in twoThousands:
                if "G" in row[5]:
                    back00s += 1
                elif "F" or "C" in row[5]:
                    front00s += 1
            if row[12] in tens:
                if "G" in row[5]:
                    back10s += 1
                elif "F" or "C" in row[5]:
                    front10s += 1
        ratio80s = back80s / front80s
        ratio90s = back90s / front90s
        ratio00s = back00s / front00s
        ratio10s = back10s / front10s
        
        decades = (1980,1990,2000,2010)
        ratio = (ratio80s,ratio90s,ratio00s,ratio10s)
        ypos = np.arange(len(decades))
        plt.bar(ypos,ratio, align = 'center', alpha = .5)
        plt.xticks(ypos,decades)
        plt.ylabel("Backcourt to Frontcourt Ratio")
        plt.title("Average Backcourt to Frontcourt Ratio for Player of the Week Winners")
        #ax = plt.gca()
        #ax.set_ylim([70,80]) # set limit of y axis
        plt.show()

        file.close()
            
my_file = open("wholesale.json", "r")
json_string = my_file.read()
my_dict = json.loads(json_string)
my_file.close()
lisbonFresh = 0
lisbonCount = 0
otherFresh = 0
otherCount = 0
oportoFresh = 0
oportoCount = 0
retailDetergent = 0
hotelDetergent = 0
retailCount = 0
hotelCount = 0
lisbonMilk = 0
otherMilk = 0
oportoMilk = 0
lisbonMilkCount = 0
otherMilkCount = 0
oportoMilkCount = 0


for element in my_dict['data']:
    if element["Industry"] == "hotel/restaurant/cafe" and element["Region"] == "Lisbon":
        lisbonFresh += element["Annual spending on fresh products"]
        lisbonCount += 1
    elif element["Industry"] == "hotel/restaurant/cafe" and element["Region"] == "Oporto":
        oportoFresh += element["Annual spending on fresh products"]
        oportoCount += 1
    elif element["Industry"] == "hotel/restaurant/cafe" and element["Region"] == "other region":
        otherFresh += element["Annual spending on fresh products"]
        otherCount += 1
for element in my_dict['data']:
    if element["Industry"] == "hotel/restaurant/cafe":
        hotelDetergent += element["Annual spending on detergents and paper products"]
        hotelCount +=1
    elif element["Industry"] == "retail":
        retailDetergent += element["Annual spending on detergents and paper products"]
        retailCount += 1
for element in my_dict['data']:
    if element["Industry"] == "retail" and element["Region"] == "Lisbon":
        lisbonMilk += element["Annual spending on milk products"]
        lisbonMilkCount += 1
    elif element["Industry"] == "retail" and element["Region"] == "Oporto":
        oportoMilk += element["Annual spending on milk products"]
        oportoMilkCount += 1
    elif element["Industry"] == "retail" and element["Region"] == "other region":
        otherMilk += element["Annual spending on milk products"]
        otherMilkCount += 1
def findMilk():
    lisbonMilkAverage = lisbonMilk/lisbonMilkCount
    oportoMilkAverage = oportoMilk /oportoMilkCount
    otherMilkAverage = otherMilk / otherMilkCount
    regions = ("Lisbon", "Oporto", "Other Region")
    money = (lisbonMilkAverage,oportoMilkAverage,otherMilkAverage)
    ypos = np.arange(len(regions))
    plt.bar(ypos,money, align = 'center', alpha = .5)
    plt.xticks(ypos,regions)
    plt.ylabel("Money Spent")
    plt.title("Spendings on Milk Products in the Retail Industry by Region")
    plt.show()


def findDetergent():
    retailAverage = retailDetergent/retailCount
    hotelAverage = hotelDetergent/hotelCount
    industry = ("Retail","Hotel/Restaurant/Cafe")
    spent = [retailAverage,hotelAverage]
    ypos = np.arange(len(industry))
    plt.bar(ypos,spent, align = 'center', alpha = .5)
    plt.xticks(ypos,industry)
    plt.ylabel("Money Spent")
    plt.title("Spendings on Detergent and Paper Products by Industry")
    plt.show()

        
    
def findFresh():
    lisbonAverage = lisbonFresh/lisbonCount
    oportoAverage = oportoFresh/oportoCount
    otherAverage = otherFresh/otherCount
    regions = ("Lisbon", "Oporto", "Other Region")
    money = [lisbonAverage,oportoAverage,otherAverage]
    ypos = np.arange(len(regions))
    plt.bar(ypos,money, align = 'center', alpha = .5)
    plt.xticks(ypos,regions)
    plt.ylabel("Money Spent")
    plt.title("Spendings on Fresh Products in the H./R./C. Industry by Region")
    plt.show()



                   
                
             






                
