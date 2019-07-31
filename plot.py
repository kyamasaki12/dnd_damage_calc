# this file contains algorithms that are solely associated with printing the graphs.
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


def getRolls():
    rolls = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30')
    return rolls

def formatDataToHit(sharpshooter, non_sharpshooter):
    to_hit = []
    ss = []
    nss = []
    for i in range(30):
        value1 = sharpshooter[i]
        value2 = non_sharpshooter[i]
        ss.append(value1[1])
        nss.append(value2[1])
    to_hit.append(nss)
    to_hit.append(ss)
    return to_hit


def formatDataDamage(sharpshooter, non_sharpshooter):
    damage = []
    ss = []
    nss = []
    for i in range(30):
        value1 = sharpshooter[i]
        value2 = non_sharpshooter[i]
        ss.append(value1[2])
        nss.append(value2[2])
    damage.append(nss)
    damage.append(ss)
    return damage

def toHitHistogram(data):
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
    plt.ylabel('chance to hit')
    plt.title('chance to hit per armor class')
    plt.xticks(index + bar_width, getRolls())
    for tick in ax.xaxis.get_major_ticks()[1::2]:
        tick.set_pad(15)
    plt.legend()

    # plt.show()
    plt.savefig('images/toHit.png')


    pass

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
    plt.ylabel('average damage')
    plt.title('average damage per armor class')
    plt.xticks(index + bar_width, getRolls())
    for tick in ax.xaxis.get_major_ticks()[1::2]:
        tick.set_pad(15)
    plt.legend()

    # plt.show()
    plt.savefig('images/damage.png')
    pass

def hist(nss, ss):
    toHit = formatDataToHit(ss, nss)
    damage = formatDataDamage(ss, nss)
    toHitHistogram(toHit)
    damageHistogram(damage)
    pass