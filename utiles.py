import matplotlib.pyplot as plt
from math import *
import numpy as np
import os


class function(object):
    def __init__(self, function_string):
        self.funct = function_string


    def execute_function(self, domain, ratio):  # given function has one variable named x -> f(x)=x^4
        array = [part for part in self.funct]
        index_array = [index for index in range(len(array)) if array[index] == "x"]
        ans = []
        domain_1 = []
        for number in range(len(domain)-1):
            i = 0
            while domain[number]+i<domain[number+1]:
                domain_1.append(domain[number]+i)
                i += ratio
        domain = domain_1[:]
        self.domain = domain
        for number in domain:

            changed_ind = index_array[:]
            changed_array = array[:]

            for i in changed_ind:
                changed_array[i] = str(number)

            inner_answer = "".join(changed_array)

            exec("global answer;answer=%s"%inner_answer)

            global answer

            ans.append(answer)

        return ans
    def show_function(self, answers, radius=5):
        plt.scatter(self.domain, answers, s=radius, edgecolors='none', c=answers, cmap=plt.cm.Reds)
        plt.show()



class polynomial(object):
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def find_root(self):
        p = np.poly1d(self.coeffs)
        rootsp = p.r
        return list(rootsp)


    def execute_polynomial(self, domain):
        answers = []
        for number in domain:
            sum = 0
            for coeff in range(len(self.coeffs)):
                sum += (self.coeffs[coeff])*((number)**(len(self.coeffs)-coeff-1))
            answers.append(sum)
        return answers


    def show_polynomial(self, domain, answers):
        plt.plot(domain, answers)
        plt.show()

'''
class plot(object):
    def __init__(self, plot):
        self.plot_data = plot
        self.unit_square = [10, 10]


    def process_data(self):
        pass

    def calculate_underneath(self, levels):
        def important_argument_plot():
            xList = [x for x, y in self.plot_data]
            yList = [y for x, y in self.plot_data]
            return max(xList), max(yList), min(xList), min(yList), xList, yList

        def do(level_id, ratio):
            under = []
            for x, y in self.plot_data:
                if (y):
                    pass


        def decrease_unit_square(level_id, ratio):
            self.unit_square = [ratio**level_id*self.unit_square[0], ratio**level_id*self.unit_square[0]]


        max_x, max_y, min_x, min_y, x_list, y_list = important_argument_plot()
        self.levels = levels

        while (True):
            do();
            decrease_unit_square();



    def draw_rect(self, pos, width, height):
            plt.axes()
            rectangle = plt.Rectangle(tuple(pos), width, height)
            plt.gca().add_patch(rectangle)
            plt.axis('scaled')
            plt.show()
'''
a = function("sin(x)")
x = a.execute_function(range(1, 100), 0.01)
a.show_function(x)
