# dnd_damage_calc

# What does the project do?
This project calculates the average damage that tabletop rpg character in the d20 roleplaying system will produce per round of combat.

# Who is the project for?
This project is for tabletop RPG players, with a focus on players of dungeons and dragons 5th edition. Players of other role playing games should be able to use this if they understand their combat systems, and what numbers are added where, but additional work may be required. 

# Why is it different?
This project is different because it gives more information about the probability of hitting, and the average damage per round.

# How do I use it? (installation instructions)
dependancies: python, kivy, pandas, numpy, matplotlib.

install dependancies, and clone repository.

run: "python gui.py"

# How does it work?
once the app is run, a form will pop up. input data into the form

d4, d6, d8, d10, d12:The number of corresponding damage dice per attack

Number of attacks: the number of attacks the character has per round using the given damage dice on hit

Minimum Die Roll to Crit: minimum die roll unmodified needed to roll a critical hit

Proficiency: proficiency modifier, applies to modifier to attack roll only

Attack Ability Modifier: modifier number for attacking stat, applies to attack and damage rolls

Additional Modifiers to Damage only: self explanatory

Magic Weapon Modifier: applies in the same manner as Attack Ability Modifier

'advantage', 'disadvantage', 'elven accuracy', or 'flat': input should be literally "advantage", "disadvantage", "elven accuracy" or "flat". inputs correspond to given possibilities in dungeons and dragons 5e

Great Weapon Fighting: input should be "yes" or "no". applies modifiers to damage as the great weapon fighting style in dungeons and dragons.

Buttons:
Run: runs the program, generates the given damage.

Graphs: will show graphs of damage and possible to hits.

below graphs are arrays showing to hit and damage for corresponding enemy armor classes(AC). 
