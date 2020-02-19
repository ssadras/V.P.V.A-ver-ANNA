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

class polynominal (object):
	def __init__ (self, name,*coeffs):
		self.coeffs = list(coeffs)
		self.coeffs_set = Set(self.coeffs);
		self.name = name;
	def _create(self, x):
		logical_result = 0
		symbolised_result = ""
		sym = ""
		degree_result = []
		for i in range(len(self.coeffs)):
			sym = ""
			if self.coeffs[i][0]:
				sym = "+"
			else:
				sym = "-"
			logical_result += self.coeffs[i] * x ** (i+1);
			symbolised_result += "+({}{}).{}^{}".format(sym, self.coeffs[i], x, i+1);
			degree_result.append(i+1)
		self.polynominal_logical_result = logical_result;
		self.polynominal_symbolized_result = symbolised_result
		self.degree_result = degree_result
		return result;

	def __add__ (self, p2):
		try:
			logical_sum = self.polynominal_logical_result + p2.polynominal_logical_result
		except :
			logical_sum = "INF"
			#assert True, "one of arguments dosen't have the parameter 'polynominal_logical_result'";
			raise Exception("one of arguments haven't been created")
		finally:
			return logical_sum;
	def __eq__ (self, p2):
		try:
			result = self.polynominal_logical_result == p2.polynominal_logical_result;
		except :
			result = False;
			raise Exception("one of arguments haven't been created")
		finally:
			return result;
	

