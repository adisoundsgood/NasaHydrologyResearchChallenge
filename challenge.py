'''
Aditya Iyer
24377286
01/19/2018
NASA Hydrology Tools Challenge
'''

import csv
import math

# Read data from a given csv file with format [station_id],[angle_degrees]
s_filename = 'angles_UCI_CS.csv'

def do_work(filename):
    cosineList = []
    b_firstLineFlag = False

    with open(filename, newline = '') as csvfile:
        print("")

        csvReader = csv.reader(csvfile)
        for row in csvReader:
            if (not b_firstLineFlag): # If  it's the first line of csv file (syntax), skip
                b_firstLineFlag = True
            else:
                angle = math.cos(int(row[1]) * math.pi / 180)
                cosineList.append(angle)
                print("station id: {0:>3}, angle in degrees: {1:>3.4}, cosine of angle: {2:3.4f}".format(row[0],row[1],angle))

        print("")
        return cosineList


do_work(s_filename)
