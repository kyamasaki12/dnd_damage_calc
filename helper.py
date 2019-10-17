# this file contains helper functions to clean up gui.py 

# convertArrays converts arrays to readable format, hopefully
# can be copied into excel or a csv file

def convertArray(data):
    tempData = []
    tempData.append('Key:(AC, Chance to Hit, Average Damage)')
    for x in data:
        tempString = ','.join(map(str, x))
        tempString = ' (' + tempString + ')'
        tempData.append(tempString)
    data = ','.join(tempData)
    return data