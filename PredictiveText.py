import math
import string

student_name = "Daniel Marvin"

############################################################
# Imports
############################################################

import random
import re


############################################################
# Section 1: Markov Models
############################################################


def tokenize(text):
    t = string.punctuation + ' '
    x = '\n\r\t\x0b\x0c'
    tokens = []
    start = 0
    end = 1

    for letter in text:
        if letter in t:
            a = text[start:end - 1]
            b = text[end - 1: end]
            if not a == '' and not a == ' ':
                tokens.append(a)
            if not b == '' and not b == ' ':
                tokens.append(b)
            start = end
        if letter in x:
            a = text[start:end - 1]
            b = text[end - 1: end]
            if not a == '' and not a == ' ' and a not in x:
                tokens.append(a)
            if not b == '' and not b == ' ' and b not in x:
                tokens.append(b)
            start = end
        end += 1
    # address edge case where there is an end of file
    if not start == end - 1:
        tokens.append(text[start:end - 1])
    return tokens


def ngrams(n, tokens):
    sentence = ['<START>'] * n
    sentence.extend(tokens)
    sentence.append('<END>')
    rtn = []
    tracker = n

    for word in sentence:
        if not word == '<START>':
            count = n
            current = []
            for i in range(n - 1):
                t = tracker - count
                count -= 1
                if not t < 0:
                    current.append(sentence[tracker - count])
            rtn.append((tuple(current), word))
            tracker += 1

    return rtn


class NgramModel(object):

    def __init__(self, n):
        self.text = []
        self.n = n

    def update(self, sentence):
        tok = tokenize(sentence)
        self.text.extend(ngrams(self.n, tok))
        pass

    def prob(self, context, token):
        total = 0
        tokenCount = 0

        for con, tok in self.text:
            if con == context:
                total += 1
                if tok == token:
                    tokenCount += 1

        if total == 0:
            return 0
        return tokenCount / total

    def random_token(self, context):
        li = []

        for con, tok in self.text:
            if con == context:
                li.append(tok)
        li.sort()
        r = random.random()
        l = len(li)

        return li[math.floor(r * l)]

    # takes in the number of words you want in the randomly generated text
    def random_text(self, token_count):
        text = ""
        li = []
        context_list = ["<START>"] * (self.n - 1)
        for count in range(token_count):
            current = self.random_token(tuple(context_list))
            li.append(current)
            context_list.append(current)
            del context_list[0]
            if current == "<END>":
                context_list = ["<START>"] * (self.n - 1)
        for word in li:
            text += word + " "
        return text[0: len(text) - 1]

    def perplexity(self, sentence):
        # tokenize the sentence and add the start and end buffers
        words = tokenize(sentence)
        context = ["<START>"] * (self.n - 1)
        context.extend(words)
        context.append('<END>')
        total = 1
        counter = 0

        # loop through the context and find the probabilities based on n-gram model size
        for i in range(len(context) - self.n + 1):
            tempMath = []
            for j in range(self.n):
                if not j == self.n - 1:
                    tempMath.append((context[counter + j]))
            a = self.prob(tuple(tempMath), context[counter + self.n - 1])
            total *= a
            counter += 1
        # compute the geometric mean of 1/probabilities and return it
        rtn = math.pow(total, (1 / counter))
        return 1 / rtn

        pass

# takes in the number of n-grams you want in your context and the file path of the text you want your model based on
def create_ngram_model(n, path):
    file = open(path)
    lines = file.readlines()
    model = NgramModel(n)
    for line in lines:
        model.update(line)
    file.close()
    return model

    pass


model = create_ngram_model(3, "frankenstein.txt")
print(model.random_text(50))


