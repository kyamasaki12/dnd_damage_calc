# this file contains algorithms that are solely associated with printing the graphs.
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# rolls is a static array, representing AC from 1 to 30. most likely
# choices are between 8 and 24.
def getRolls():
    rolls = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30')
    return rolls

# formatDataToHit and formatDamage format the data incoming from
# the calculation for each table

# formatDataToHit takes in two arrays, and takes the toHit variable from each
# set, and appends them to two new lists. it then appends the two new lists to a
# list of lists

def formatDataToHit(sharpshooter, non_sharpshooter):
    # initialize lists
    to_hit = []
    ss = []
    nss = []
    # extract data to new lists
    for i in range(30):
        value1 = sharpshooter[i]
        value2 = non_sharpshooter[i]
        ss.append(value1[1])
        nss.append(value2[1])
    # append data to new lists
    to_hit.append(nss)
    to_hit.append(ss)
    return to_hit

# formatDataDamage takes in two multilayer lists, and takes the damage
# variable from each inner list, for each set of data. appends each value 
# to a new list, and appends each of the new lists to another list, creating
# a list of lists

def formatDataDamage(sharpshooter, non_sharpshooter):
    # initialize values
    damage = []
    ss = []
    nss = []
    # extract data to correct lists
    for i in range(30):
        value1 = sharpshooter[i]
        value2 = non_sharpshooter[i]
        ss.append(value1[2])
        nss.append(value2[2])
    # append data to new lists
    damage.append(nss)
    damage.append(ss)
    return damage

# toHitHistogram takes in the data generated above, and creates the
# corresponding bar graph

def toHitHistogram(data):
    # set initial values for each 
    rolls = getRolls()
    normal = data[0]
    sharpshooter = data[1]
    ngroups = 30
    # create plot
    fig, ax = plt.subplots()
    y_val = np.arange(0, max(max(sharpshooter), max(normal))+1, .5)
    index = np.arange(ngroups)
    bar_width = 0.35
    opacity = 0.8
    # add values to plot
    rects1 = plt.bar(index, normal, bar_width,
                     alpha=opacity, color='b', label='normal')

    rects2 = plt.bar(index + bar_width, sharpshooter, bar_width,
                     alpha=opacity, color='g', label='sharpshooter')
    # add labels to plot
    plt.xlabel('AC')
    plt.ylabel('Probability to Hit AC')
    plt.title('Probability to Hit per Armor Class')
    # format xticks
    plt.xticks(index + bar_width, getRolls())
    for tick in ax.xaxis.get_major_ticks()[1::2]:
        tick.set_pad(15)
    plt.legend()
    # save plot locally
    plt.savefig('images/toHit.png')
    pass

# create histogram for damage. very similar to above

def damageHistogram(data):
    rolls = getRolls()
    normal = data[0]
    sharpshooter = data[1]

    ngroups = 30
    fig, ax = plt.subplots()
    y_val = np.arange(0, max(max(sharpshooter), max(normal))+1, .5)
    index = np.arange(ngroups)
    bar_width = 0.35
    opacity = 0.8
    
    rects1 = plt.bar(index, normal, bar_width,
                     alpha=opacity, color='b', label='normal')

    rects2 = plt.bar(index + bar_width, sharpshooter, bar_width,
                     alpha=opacity, color='g', label='sharpshooter')
    plt.xlabel('AC')
    plt.ylabel('Average DPR')
    plt.title('Average Damage per Opponent Armor Class')
    plt.xticks(index + bar_width, getRolls())
    for tick in ax.xaxis.get_major_ticks()[1::2]:
        tick.set_pad(15)
    plt.legend()

    # plt.show()
    plt.savefig('images/damage.png')
    pass

# main function, calls all other functions

def hist(nss, ss):
    # format data
    toHit = formatDataToHit(ss, nss)
    damage = formatDataDamage(ss, nss)
    # create graphs
    toHitHistogram(toHit)
    damageHistogram(damage)
    pass