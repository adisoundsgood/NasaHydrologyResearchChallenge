import challenge
import math

s_filename = 'angles_UCI_CS.csv'
angleList = [90,60,30,0] # hardcoded to test angles_UCI_CS.csv
resultList = []
counter = 0

for deg in angleList: # create the correct result list to test the code in challenge.py
    angle = math.cos((angleList[counter]) * math.pi / 180)
    resultList.append(angle)
    counter += 1


def testAnswer():
    assert challenge.do_work(s_filename) == resultList


