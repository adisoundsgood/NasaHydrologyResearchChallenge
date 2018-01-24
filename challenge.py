"""
Aditya Iyer
24377286
01/19/2018
NASA Hydrology Tools Challenge
"""

import math
import requests

# Read data from a given csv file with format [station_id],[angle_degrees]
s_filename = 'angles_UCI_CS.csv'


def do_work(url):
    cosineList = []
    b_firstLineFlag = False

    r = requests.get(url)

    # Each line of r.text() is of this format [string],[string]\r\n
    data = r.text.split("\r\n")  # Each list is a line in the file

    for line in data:
        row = line.split(",")

        if (len(row) > 1): # Skips the last, empty line
            if (not b_firstLineFlag):  # If  it's the first line of csv file (syntax), skip
                b_firstLineFlag = True
            else:
                angle = math.cos(int(row[1]) * math.pi / 180)
                cosineList.append(angle)
                print("station id: {0:>3}, angle in degrees: {1:>3.4}, cosine of angle: {2:3.4f}".format(row[0], row[1], angle))
    return cosineList
