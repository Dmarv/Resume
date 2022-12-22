student_name = "Type your full name here."

############################################################
# Imports
############################################################

import homework9_data as data
import math

# Include your imports here, if any are used.


############################################################
# Section 1: Perceptrons
############################################################

class BinaryPerceptron(object):

    def __init__(self, examples, iterations):
        self.weight = [0, 0]
        for iteration in range(iterations):
            for vector, category in examples:
                x = unravel(vector)
                y_hat = sign(dot_prod(self.weight, x))
                if not y_hat == category:
                    if category:
                        self.weight = add_vectors(self.weight, x, '+')
                    else:
                        self.weight = add_vectors(self.weight, x, '-')
        pass

    def predict(self, x):
        vector = unravel(x)
        return sign(dot_prod(self.weight, vector))
        pass


def dot_prod(vector1, vector2):
    sum = 0
    for position in range(len(vector1)):
        sum += vector1[position] * vector2[position]
    return sum


def add_vectors(vector1, vector2, sign):
    rtn = [0] * len(vector1)
    if sign == "+":
        for position in range(len(vector1)):
            rtn[position] = vector1[position] + vector2[position]
    if sign == "-":
        for position in range(len(vector1)):
            rtn[position] = vector1[position] - vector2[position]
    return rtn


def sign(number):
    if number > 0:
        return True
    else:
        return False


def unravel(dic):
    rtn = [0, 0]
    if "x1" in dic.keys():
        rtn[0] = dic["x1"]
    if "x2" in dic.keys():
        rtn[1] = dic["x2"]
    return rtn


# train = [({"x1": 1}, True), ({"x2": 1}, True), ({"x1": -1}, False), ({"x2": -1}, False)]
#
# test = [{"x1": 1}, {"x2": 1, "x2" : 1}, {"x1": -1, "x2": 1.5}, {"x1" : -0.5,"x2": -2}]
# p = BinaryPerceptron(train, 1)
#
# [print(p.predict(x)) for x in test]

class MulticlassPerceptron(object):

    def __init__(self, examples, iterations):
        self.categories = []
        self.weights = {}
        for v, c in examples:
            if c not in self.weights.keys():
                self.weights[c] = [0, 0]
                self.categories.append(c)
        for iteration in range(iterations):
            for vector, category in examples:
                x = unravel(vector)
                y_hat = max_cycle_cat(self.weights, self.categories, x)
                if not y_hat == category:
                    self.weights[category] = add_vectors(self.weights[category], x, '+')
                    self.weights[y_hat] = add_vectors(self.weights[y_hat], x, '-')
        pass

    def predict(self, x):
        return max_cycle_cat(self.weights, self.categories, unravel(x))
        pass


def max_cycle_cat(dic, lis, vector):
    sum = -math.inf
    category = None
    for i in lis:
        temp = dot_prod(dic[i], vector)
        if temp > sum:
            sum = temp
            category = i
    return category


# train = [({"x1": 1}, 1), ({"x1": 1, "x2": 1}, 2), ({"x2": 1}, 3), ({"x1": -1, "x2": 1}, 4), ({"x1": -1}, 5),
#          ({"x1": -1, "x2": -1}, 6), ({"x2": -1}, 7), ({"x1": 1, "x2": -1}, 8)]
#
# p = MulticlassPerceptron(train, 10)
# [print(p.predict(x)) for x, y in train]
############################################################
# Section 2: Applications
############################################################

class IrisClassifier(object):

    def __init__(self, data):
        self.categories = []
        self.weights = {}
        for v, c in data:
            if c not in self.weights.keys():
                self.weights[c] = [0, 0, 0, 0]
                self.categories.append(c)
        for vector, category in data:
            x = gen_unravel(vector)
            y_hat = max_cycle_cat(self.weights, self.categories, x)
            if not y_hat == category:
                self.weights[category] = add_vectors(self.weights[category], x, '+')
                self.weights[y_hat] = add_vectors(self.weights[y_hat], x, '-')
        pass

    def classify(self, instance):
        return max_cycle_cat(self.weights, self.categories, gen_unravel(instance))
        pass


def gen_unravel(tup):
    rtn = []
    for i in tup:
        rtn.append(i)
    return rtn


# c = IrisClassifier(data.iris)
# print(c.classify((5.1, 3.5, 1.4, 0.2)))

class DigitClassifier(object):

    def __init__(self, data):
        self.categories = []
        self.weights = {}
        for v, c in data:
            if c not in self.weights.keys():
                self.weights[c] = [0] * 64
                self.categories.append(c)
        for i in range(15):
            for vector, category in data:
                x = gen_unravel(vector)
                y_hat = max_cycle_cat(self.weights, self.categories, x)
                if not y_hat == category:
                    self.weights[category] = add_vectors(self.weights[category], x, '+')
                    self.weights[y_hat] = add_vectors(self.weights[y_hat], x, '-')
        pass

    def classify(self, instance):
        return max_cycle_cat(self.weights, self.categories, gen_unravel(instance))
        pass


class BiasClassifier(object):

    def __init__(self, data):
        self.weight = 0
        for i in range(10):
            for vector, category in data:
                y_hat = bias_cut_off(self.weight, vector)
                if not y_hat == category:
                    if category:
                        self.weight = self.weight + vector
                    else:
                        self.weight = self.weight - vector
        pass

    def classify(self, instance):
        return bias_cut_off(self.weight, instance)
        pass


def bias_cut_off(weight, vector):
    if weight * vector > 1:
        return True
    else:
        return False


# c = BiasClassifier(data.bias)
# [print(c.classify(x)) for x in (-1, 0, 0.5, 1.5, 2)]


class MysteryClassifier1(object):

    def __init__(self, data):
        self.weight = 0
        for i in range(1):
            for vector, category in data:
                y_hat = myst_1_cut_off(self.weight, vector)
                if not y_hat == category:
                    if category:
                        self.weight += dist(vector)
                    else:
                        self.weight -= dist(vector)
        pass

    def classify(self, instance):
        return myst_1_cut_off(self.weight, instance)
        pass


def dist(vector):
    vec = math.pow(vector[0], 2) + math.pow(vector[1], 2)
    return math.pow(vec, .5)

def myst_1_cut_off(weight, vector):
    if (weight * dist(vector)) > 10:
        return True
    else:
        return False

# c = MysteryClassifier1(data.mystery1)
# [print(c.classify(x)) for x in ((0, 0), (0, 1), (-1, 0), (1, 2), (-3, -4))]

class MysteryClassifier2(object):

    def __init__(self, data):
        self.weight = 0
        for i in range(10):
            for vector, category in data:
                y_hat = myst_2_cut_off(self.weight, vector)
                if not y_hat == category:
                    if category:
                        self.weight += trans2(vector)
                    else:
                        self.weight -= trans2(vector)
        pass

    def classify(self, instance):
        return myst_2_cut_off(self.weight, instance)
        pass

def trans2(vector):
    sum = 1
    for i in range(3):
        sum *= vector[i]
    return sum


def myst_2_cut_off(weight, vector):
    if (weight * trans2(vector)) > 0:
        return True
    else:
        return False


# c = MysteryClassifier2(data.mystery2)
# [print(c.classify(x)) for x in ((1, 1, 1), (-1, -1, -1), (1, 2, -3), (-1, -2, 3))]


# for vec, cat in data.mystery2:
#     print(cat)

