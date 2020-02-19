from chempy import Equilibrium
from sympy import symbols
def balance (first, next, some1, some2)
	K1, K2, Kw = symbols('K1 K2 Kw')
	e1 = Equilibrium(first, next, K1)
	e2 = Equilibrium(some1, some2, K2)
	coeff = Equilibrium.eliminate([e1, e2], 'e-')

	redox = e1*coeff[0] + e2*coeff[1]
	print(redox)
	autoprot = Equilibrium({'H2O': 1}, {'H+': 1, 'OH-': 1}, Kw)
	n = redox.cancel(autoprot)
	redox2 = redox + n*autoprot
	print(redox2)
 