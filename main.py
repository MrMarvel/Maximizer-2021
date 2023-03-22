import scipy as sc
from scipy.optimize import linprog
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

SPACE = 338
MONEY = 300
a_money = 10
b_money = 7
c_money = 5
a_space = 9
b_space = 8
c_space = 3
a_prod = 8
b_prod = 6
c_prod = 3
a_max = int(max(SPACE/a_space, MONEY/a_money))
b_max = int(max(SPACE/b_space, MONEY/b_money))
c_max = int(max(SPACE/c_space, MONEY/c_money))
obj = [-a_prod, -b_prod, -c_prod]  # a, b, c
#      ─┬  ─┬  ─┬
#       │   │   └─┤ Коэффициент для c
#       │   └─────┤ Коэффициент для b
#       └─────────┤ Коэффициент для a

lhs_ineq = [[a_space, b_space, c_space],  # левая сторона ограничение площадь неравенства
            [a_money, b_money, c_money]]  # левая сторона ограничение деньги неравенства

rhs_ineq = [SPACE,  # правая сторона ограничение площадь неравенства
            MONEY]  # правая сторона ограничение деньги неравенства

lhs_eq = [[0, 0, 0]]  # левая сторона зеленого равенства
rhs_eq = [0]  # правая сторона зеленого равенства

bnd = [(0, a_max),  # Границы a
       (0, b_max),  # Границы b
       (0, c_max)]  # Границы c

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
              method="simplex", )

print(opt.x)
