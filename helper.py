# this file contains helper functions to clean up gui.py

def convertArray(data):
    tempData = []
    tempData.append('(AC, Chance to Hit, Average Damage)')
    for x in data:
        tempString = ','.join(map(str, x))
        tempString = ' (' + tempString + ')'
        tempData.append(tempString)
    data = ','.join(tempData)
    return data