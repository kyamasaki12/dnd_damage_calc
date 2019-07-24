# main.py
import pandas as pd

# hit calc is supposed to return a percent chance to hit a given ac,
# value modifiers using AC, to hit modifiers, and advantage string
# input


def hit_calc(ac, toHit, df, toCrit):
    tempval = ac - toHit
    value = max(2, min(toCrit, tempval))
    return df.loc[df.roll == value, 'probability'].values[0]


# counts the average damage on die before modifications

def damage_helper(numDice, df):
    damage = 0
    counter = 0
    for x in numDice:
        # print("x is: " + str(x))
        # print(df.loc[counter])
        damage += x * df.loc[counter, 'average']
        counter += 1
    return damage

# numDice = array of dice, toCrit is critical minimum,
# df = probability of rolling at least value x
# df2 = damage per die


def damage_on_crit(numDice, toCrit, df, df2):
    crit_probability = df.loc[toCrit-1, 'probability']
    return crit_probability * damage_helper(numDice, df2)


def damage_on_hit(numDice, damage_mod, df):
    damage = damage_helper(numDice, df)
    return damage+damage_mod


# numDice should be an list, with values [d4,d6,d8,d10,d12]
# to_crit is int, usually 20, 19 or 18 with champion
# proficiency: applied to hit only, ability:to hit and damage
# damageMod:to damage only, magic_weapon: applies to both,
# advantage is a string, sa = savage attacker, gwf is great
# weapon fighter


def calculations(numDice, numAttacks, toCrit, proficiency,
                 ability, damageMod, magicWeapon,
                 advantage, gwf, sharpshooter):
    acRange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    proficiency = ability + proficiency + magicWeapon
    toDamage = damageMod + ability + magicWeapon
    # get sharpshooter info
    if(sharpshooter == 'yes'):
        proficiency -= 5
        toDamage += 10

    # get correct advantage disadvantage type
    if(advantage == 'disadvantage'):
        csvPath = "rolls_atleast/disadvantage_atleast.csv"
    elif(advantage == 'advantage'):
        csvPath = "rolls_atleast/advantage_atleast.csv"
    elif(advantage == 'elven'):
        csvPath = "rolls_atleast/elven_advantage_atleast.csv"
    else:
        csvPath = "rolls_atleast/normal_atleast.csv"
    df = pd.read_csv(csvPath)
    if(gwf == "Yes"):
        csvPath = "dice_average/gwf_damage.csv"
    else:
        csvPath = "dice_average/normal_damage.csv"
    df2 = pd.read_csv(csvPath)
    toHit = []
    damage = []
    for x in acRange:
        # print(x)
        toHit.append(hit_calc(x, proficiency, df, toCrit))
        # print("damage on hit: " + str(damage_on_hit(numDice, toDamage, df2)))
        # print("damage on crit" + str(damage_on_crit(numDice, toCrit, df, df2)))
        damage_per_hit = (toHit[x-1] * damage_on_hit(numDice, toDamage, df2)) 
        + damage_on_crit(numDice, toCrit, df, df2)
        damage.append([x, toHit[x-1], numAttacks * damage_per_hit])
    return damage


def testField(attr):
    print(attr)

# die_average = pd.read_csv('dice_average/normal_damage.csv')
# hit_probs = pd.read_csv('rolls_atleast/normal_atleast.csv')

# print(hit_calc(20, 5, hit_probs, 20))
# print(damage_helper([0,2,0,0,0], die_average))

# print(calculations([0, 0, 1, 0, 0], 1, 20, 3, 3,
#                    2, 0, 'advantage', 'no', 'no'))

# calculations(numDice, numAttacks, toCrit, proficiency, ability,
#              toDamage, magicWeapon, advantage_string, gwf)
