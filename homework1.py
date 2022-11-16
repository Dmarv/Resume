############################################################
# CIS 521: Homework 1
############################################################
import numpy as np
from nltk import sent_tokenize, word_tokenize, RegexpTokenizer, pos_tag
from nltk.corpus import stopwords

student_name = "Daniel Marvin"

# This is where your grade report will be sent.
student_email = "dmarv@seas.upenn.edu"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """We can consider Python strongly typed since while the program runs, the interpreter 
knows what types each variable is. Python is also dynamically types since the interpreter will change the varibale
type to match the type is been assigned.
Example, x = 5. Python knows that this is an int. If we then proceed to write x = '5', python will both let you
do this and know that x is a type string"""

python_concepts_question_2 = """ When we run this code, we get the error unhashable type: list. this is because we
cannot use a list as a key in python since they have not built in hashcode for lists"""

python_concepts_question_3 = """Concatenate2 is much faster. Concatenate1 must iterate through each string and 
then store it in result. Since strings are immutable, To store it, it needs to make a new string which the additional
information and then replace the old string. Concatenate2, on the other hand, treats each string as an iterable
 and yields the next string so it doesnt have to make a new string every time"""


###########################################################
# Section 2: Working with Lists
###########################################################


def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]


def concatenate(seqs):
    return [y for i in seqs for y in i]
    pass


def transpose(matrix):
    x = matrix[0].__len__()
    y = matrix.__len__()

    result = []
    for i in range(x):
        # initialize a new list in 'results' with the corresponding element in 'matrix'
        result.append([matrix[0][i]])
        # traverse only through y - 1 since initialize took up one iteration
        for j in range(y - 1):
            # populate it with the rest of the elements
            result[i].append(matrix[j + 1][i])

    return result
    pass


############################################################
# Section 3: Sequence Slicing
############################################################


def copy(seq):
    return seq[:]
    pass


def all_but_last(seq):
    return seq[0:-1]
    pass


def every_other(seq):
    return seq[::2]
    pass


############################################################
# Section 4: Combinatorial Algorithms
############################################################


def prefixes(seq):
    for i in range(len(seq) + 1):
        yield seq[0:i]
    pass


def suffixes(seq):
    for i in range(len(seq) + 1):
        yield seq[i:len(seq)]
    pass


def slices(seq):
    for i in range(len(seq) + 1):
        for j in range(len(seq) + 1):
            if j > i:
                yield seq[i:j]
    pass


############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join(text.lower().split())
    pass


def no_vowels(text):
    result = ""
    for i in text:
        if i not in "aeiouAEIOU":
            result += i
    return result
    pass


def digits_to_words(text):
    result = ""

    for i in text:
        if i in "0123456789":
            if i == '0':
                result += "zero "
            elif i == '1':
                result += "one "
            elif i == '2':
                result += "two "
            elif i == '3':
                result += "three "
            elif i == '4':
                result += "four "
            elif i == '5':
                result += "five "
            elif i == '6':
                result += "six "
            elif i == '7':
                result += "seven "
            elif i == '8':
                result += "eight "
            elif i == '9':
                result += "nine "

    return result.strip()
    pass


def to_mixed_case(name):
    count = 0
    result = ""

    li = name.split('_')
    lis = [i for i in li if len(i) > 0]
    for i in lis:
        if count == 0:
            result += i.lower()
        else:
            result += i.capitalize()
        count += 1
    # if len(result) > 1:
    #     result[0].lower()
    return result
    pass


############################################################
# Section 6: Polynomials
############################################################


class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial = polynomial
        pass

    def get_polynomial(self):
        return tuple(self.polynomial)
        pass

    def __neg__(self):

        return Polynomial(tuple([(i[0] * -1, i[1]) for i in self.polynomial]))
        pass

    def __add__(self, other):
        li = []

        for i in self.polynomial:
            li.append(i)
        for j in other.polynomial:
            li.append(j)
        return Polynomial(tuple(li))
        pass

    def __sub__(self, other):
        li = []
        for i in self.polynomial:
            li.append(i)
        for j in other.polynomial:
            li.append((j[0] * -1, j[1]))
        return Polynomial(tuple(li))
        pass

    def __mul__(self, other):
        li = []
        for i in self.polynomial:
            for j in other.polynomial:
                li.append((i[0] * j[0], i[1] + j[1]))
        return Polynomial(tuple(li))
        pass

    def __call__(self, x):
        num = 0
        for i in self.polynomial:
            num += (x ** i[1] * i[0])
        return num
        pass

    def simplify(self):
        li = []
        current_power_list = []
        current_power = "null"
        result = []
        ret = []

        # construct a sorted list
        for i in self.polynomial:
            if len(li) < 1:
                li.append(i)
            else:
                li.insert(0, i)
                x = len(li)
                for j in range(x):
                    if j + 1 < x:
                        if li[j][1] < li[j + 1][1]:
                            temp = li[j + 1]
                            li[j + 1] = li[j]
                            li[j] = temp
        # cycle through the list and add the coefficients of similar power
        if len(li) > 1:
            current_power = li[0][1]
            counter = len(li)
            while counter > 0:
                while li[0][1] == current_power:
                    current_power_list.append(li[0])
                    del li[0]
                    counter -= 1
                    if counter == 0:
                        break
                temp = 0
                for k in current_power_list:
                    temp += k[0]
                result.append((temp, current_power))
                if counter == 0:
                    break
                current_power = li[0][1]
                current_power_list = []
        else:
            result = li[:]
        for i in result:
            if i[0] != 0:
                ret.append(i)
        if len(ret) == 0:
            ret.append((0, 0))
        self.polynomial = tuple(ret)
        pass

    def __str__(self):
        to = self.polynomial
        li = []
        st = " "
        s = ""
        special = 0
        for i in self.polynomial:
            co = 0
            power = 0
            sign = "null"
            if i[0] < 0:
                sign = "-"
                co = i[0] * -1
            else:
                sign = "+"
                co = i[0]
            power = i[1]
            if power == 0 & co == 0:
                s = ('%d' % co)
            elif power == 1 & co == 1:
                s = 'x'
            elif power == 1:
                if co != 1:
                    s = ('%dx' % co)
            elif power == 1 & co == 1:
                s = '0x'
            elif power > 1 & co == 1:
                s = ('x^%d' % power)
            else:
                s = ('%dx^%d' % (co, power))

            li.append(sign)
            li.append(s)

        st = st.join(li)
        temp = ""
        if len(li) == 0:
            return temp
        if st[0] == '-':
            for i in range(len(st)):
                if i != 1:
                    temp += st[i]
        else:
            for i in range(len(st)):
                if i > 1:
                    temp += st[i]
        st = temp
        return st

        pass




############################################################
# Section 7: Python Packages
############################################################
import numpy
def sort_array(list_of_matrices):
    m = np.array([])
    a = np.array([])
    for i in list_of_matrices:
        a = i.ravel()
        b = np.append(m, a)
        m = b
    sor = np.sort(m)
    m = sor[::-1]
    return m


import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
def POS_tag(sentence):
    tok = word_tokenize(sentence)
    st = set(stopwords.words('english'))
    li_lower = [i.lower() for i in tok if i.isalnum()]
    li_no_st_wds = [i for i in li_lower if i not in st]
    li_rtn = pos_tag(li_no_st_wds)
    return li_rtn
    pass

############################################################
# Section 8: Feedback
############################################################

feedback_question_1 = """
About 12 hours. It didn't take longer because I struggled with the material. It was more
of a struggle figuring out the style of answers. In contrast to 591 and 593 where were forbidden to use built
in functions because the whole point was to understand HOW, for example, concatenate works, here, we were meant to
find the fastest way by specifically using built in functions. This core idea woven through this assignment 
was not obvious to me until much too late. I understand that this is meant to be a python refresher and this should
have been obvious, but for some reason I did not internalize it. 
"""

feedback_question_2 = """
There were parts of the assignment that I spent far to long trying to be clever and avoid write some code. 
Upon reflection, I shouldn't have waisted so much time trying to avoid the work. 
For example, in the simplify function found in the Polynomial class, 
I spent a lot of time searching for a function to sort tuples in lists. In the end, I just wrote itmyself. 
Another example is in the __str__ function found in the Polynomial class. I was spent a lot of time thinking of a more
general pattern when I could have just wrote the few exceptions out in elif (which i ended up doing) and saved
myself a lot of time. 
"""

feedback_question_3 = """
Overall, the homework built upon itself in a wise and elegant way. There were just a few parts I would change.
For questions 8, we were instructed to have a bunch of stylistic constraints like
"the power portion omitted if the power is 1." While it makes sense if I were publishing a tool for the public to 
conform to some style
1. it felt tedious and a waist of time if the goal of this homework to was get us caught up with python
2. I really like have powers of 0 and coefficients of 1 in my work. For example, take the power expansion of e, 
if you don't write out the implicit powers for the first few element, you lose some of the pattern without 
some investigation. I always prefer to see how a function looks in 0 and 1 dimensions instead of ignoring it. 
There maybe a few more small thing like this I would change. But, overall it was a lot of fun and
didn't feel overwhelming.


"""
