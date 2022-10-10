import mip as mp

BOSS_HIT = 100
BOSS_DAMAGE = 8
BOSS_ARMOR = 2

PLR_HIT = 100

weaponValue = [4, 5, 6, 7, 8]
weaponCost = [8, 10, 25, 40, 74]
armorValue = [1, 2, 3, 4, 5]
armorCost = [13, 31, 53, 75, 102]
ringValue = [1, 2, 3, 1, 2, 3]
ringCost = [25, 50, 100, 20, 40, 80]

model = mp.Model()

w = [model.add_var(name=f'Weapon{i}', var_type=mp.INTEGER, lb=0, ub=1) for i in range(5)]
a = [model.add_var(name=f'Armor{i}', var_type=mp.INTEGER, lb=0, ub=1) for i in range(5)]
r = [model.add_var(name=f'Ring{i}', var_type=mp.INTEGER, lb=0, ub=1) for i in range(6)]

# Feasible contr.
model.add_constr(mp.xsum(w[i] for i in range(5)) == 1)
model.add_constr(mp.xsum(a[i] for i in range(5)) <= 1)
model.add_constr(mp.xsum(r[i] for i in range(6)) <= 2)
model.add_constr(mp.xsum(w[i] * weaponValue[i] for i in range(5)) +
                 mp.xsum(r[i] * ringValue[i] for i in range(3)) >= BOSS_ARMOR)
model.add_constr(((BOSS_DAMAGE - mp.xsum(a[i] * armorValue[i] for i in range(5)) -
                   mp.xsum(r[i] * ringValue[i] for i in range(3, 6)) - 1)) >=
                 ((mp.xsum(w[i] * weaponValue[i] for i in range(5)) +
                   mp.xsum(r[i] * ringValue[i] for i in range(3)) - BOSS_ARMOR)))

model.objective = mp.maximize(mp.xsum(w[i] * weaponCost[i] for i in range(5)) +
                              mp.xsum(a[i] * armorCost[i] for i in range(5)) +
                              mp.xsum(r[i] * ringCost[i] for i in range(6)))

model.optimize()

print(f'DAY21_2 result: {model.objective.x}')
