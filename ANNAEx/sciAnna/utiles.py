import matplotlib.pyplot as plt 
import numpy as np 
import math


class Set (object) :
	def __init__ (self, members_list):
		self.mems = list(set(members_list))
		self.length = len(list(members_list))

	@staticmethod
	def subSet (A, B):
		for member in A :
			if member not in B:
				return 0
		else:
			return 1

	def __eq__ (self, B):
		
		if Set.subSet(self.mems, B.mems):
			if Set.subSet(B.mems, self.mems):
				return 1
		return 0

	def union (self, *argv):
		mems_2 = self.mems[:]
		for arg in argv:
			for mem in arg:
				mems_2.append()
		return Set(mems_2);
		

	def common (self, sets_list):
		if len(sets_list) == 1:
			common = []
			for i in sets_list[0].mems:
				if i in self.mems:
					common.append(i)
			return Set(common) 
		elif len(sets_list)>1:
			return sets_list[0].common(sets_list[1:])
		else:
			raise ValueError;
	def __sub__ (self, sets_list):
		return Set([i for i in self.mems if i not in set.mems]);

	def __mul__ (self, B):# A*B*C*... = {(a, b, c, ...)|a in A, b in B, c in C ,...}
		new_mul_array = [(i, j) for i in self.mems for j in B.mems]
		return Set(new_mul_array)

	def __str__ (self):
		
		new_str = ""
		for i in range(len(self.mems)):
			a = "" if i == len(self.mems)-1 else ", "
			new_str += "%s"%(str(self.mems[i])+a)
		string = "{%s}"%new_str
		return string;
class polynominal(object):
	"""docstring for polynominal"""
	def __init__(self, sentences):
		self.sentences = sentences; # a sentence : (2, k)
		#print(self.sentences)
	def simplize (self):
		print("simplization")
		result = {}
		p2 = []
		degree_zero = []
		var = None;
		for sentence in self.sentences:
			if sentence[-1] == "NaN":
				degree_zero.append(sentence[0])
				continue;
			var = sentence[-1]
			bool = 1
			for key, val in result.items():
				if var == key:
					bool = 0
			if bool:
				result.update({var:sentence[0]})
			else:
				result[var] += sentence[0];
		for key, val in result.items():
			p2.append((val, key))
		for i in degree_zero:
			p2.append((i, "NaN"))
		self.simplized = p2[:]
		print("p2:", p2)
		#print("poly : ", polynominal(self.simplized).sentences)
		return polynominal(self.simplized);

	def _mult (self, other_number):
		mult = [(other_number*i[0], i[-1]) for i in self.sentences]
		#print("mult: ", mult)
		return polynominal(mult)

	def __add__ (self, other):
		new = self.sentences[:]
		for sent in other.sentences:
			new.append(sent);
		return polynominal(new)

	def coeffs (self):
		return (x[0] for x in self.sentences);


class equation (object):
	''' p1 and p2 are polynominal objects'''
	def __init__ (self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def simplize_each_side(self):
		return equation(self.p1.simplize(), self.p2.simplize())

	def move (self):
		#making polynominal
		new_one = []
		polynm = self.p2.simplize();
		for coeff, var in polynm.sentences:
			if var == "NaN":
				continue;
			new_one.append((-1*coeff, var))
			polynm.sentences.remove((coeff, var));
		return (p1+polynominal(new_one)).simplize()

'''
p2 = polynominal([(10, "x")])
print(tuple(p2.coeffs()))'''

class equation_system (object):
	def __init__ (self, *equations):
		self.equations = list(equations);

	def simplize_each_equation (self):
		result = []
		for eq in self.equations:
			result.append(eq.simplize_each_side());
		self.symplized = simplized;
		#return simplized;

	def solve (self):
		### moving and making one side zero ###
		for eq in self.equations:
			eq.move()

		A = []
		B = []
		for eq in self.equations:
			A.append(list(eq.p1.coeffs()))
			B.append([0])
		a = np.array(A);
		inv_a = np.linalg.inv(A)
		b = np.array(B)
		X = np.linalg.inv(a).dot(b)
		return X
p1 = polynominal([(4, "x"), (3, "y")])
p2 = polynominal([(20, "NaN")])

e1 = equation(p1, p2)

p3 = polynominal([(-5, "x"), (9, "y")])
p4 = polynominal([(26, "NaN")])

e2 = equation(p3, p4)

a = equation_system(e1, e2)
print(a.solve())


