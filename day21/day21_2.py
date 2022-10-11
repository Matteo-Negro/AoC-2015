import mip as mp
import math

# Game Setup
# BOSS stats
BOSS_HIT = 100
BOSS_DAMAGE = 8
BOSS_ARMOR = 2

# PLAYER stats
PLR_HIT = 100

# Shop
weapons = {'Dagger': [4, 8],
           'Shortsword': [5, 10],
           'Warhammer': [6, 25],
           'Longsword': [7, 40],
           'Greataxe': [8, 74]}

armors = {'Leather': [1, 13],
          'Chainmail': [2, 31],
          'Splintmail': [3, 53],
          'Bandedmail': [4, 75],
          'Platemail': [5, 102]}

rings = {'Damage +1': [1, 25],
         'Damage +2': [2, 50],
         'Damage +3': [3, 100],
         'Defense +1': [1, 20],
         'Defense +2': [2, 40],
         'Defense +3': [3, 80]}

# Model
model = mp.Model()

# Variables
w = [model.add_var(name=f'{key}', var_type=mp.INTEGER, lb=0, ub=1) for key in weapons.keys()]
a = [model.add_var(name=f'{key}', var_type=mp.INTEGER, lb=0, ub=1) for key in armors.keys()]
r = [model.add_var(name=f'{key}', var_type=mp.INTEGER, lb=0, ub=1) for key in rings.keys()]

# Helper operation
bossAttacks = math.pow(PLR_HIT, -1) * ((BOSS_DAMAGE - 1 -
                                        mp.xsum(a[i] * armors[key][0] for i, key in enumerate(armors.keys())) -
                                        mp.xsum(r[i] * rings[f'Defense +{i - 2}'][0] for i in range(3, 6))))
playerAttacks = math.pow(BOSS_HIT, -1) * ((mp.xsum(w[i] * weapons[key][0] for i, key in enumerate(weapons.keys())) +
                                           mp.xsum(r[i] * rings[f'Damage +{i + 1}'][0] for i in range(3)) - BOSS_ARMOR))

# Feasible constraints
model.add_constr(mp.xsum(w[i] for i in range(5)) == 1)
model.add_constr(mp.xsum(a[i] for i in range(5)) <= 1)
model.add_constr(mp.xsum(r[i] for i in range(6)) <= 2)

# Lose constraints
model.add_constr(mp.xsum(w[i] * weapons[key][0] for i, key in enumerate(weapons.keys())) +
                 mp.xsum(r[i] * rings[f'Damage +{i + 1}'][0] for i in range(3)) >= BOSS_ARMOR)
model.add_constr(bossAttacks >= playerAttacks)

# Objective function
model.objective = mp.maximize(mp.xsum(w[i] * weapons[key][1] for i, key in enumerate(weapons.keys())) +
                              mp.xsum(a[i] * armors[key][1] for i, key in enumerate(armors.keys())) +
                              mp.xsum(r[i] * rings[key][1] for i, key in enumerate(rings.keys())))

model.optimize()

print(f'DAY21_2 result: {model.objective.x}')

for item in model.vars:
    if item.x != 0:
        print(f'Item: {item}')
