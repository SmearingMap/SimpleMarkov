import random
from collections import Counter 


def tokenize(text):
    return text.replace('.', ' .').replace(',', ' ,').replace("?", " ?").split()

def build_model(list):
    transitions = {word : Counter() for word in list}
    for i in range(len(list) - 1):
        current = list[i]
        next = list[i+1]
        if next in transitions[current].keys():
            transitions[current][next] += 1
        else:
            transitions[current][next] = 1
    return transitions 

def gen_sentence(list, MIN_LEN=4):
    transitions = build_model(list)
    sentence = []
    sentence_starters = filter(lambda x: '.' not in x, transitions['.'].keys())
    start = random.choice(sentence_starters)
    sentence.append(start)
    while not '.' in sentence[-1]:
        if len(sentence) > 0:
            choices = transitions[sentence[-1]]
        else:
            choices = transitions[" ."]
        sentence.append(weighted_choice(choices))
    if len(sentence) < MIN_LEN + 1:
        return gen_sentence(list, MIN_LEN=MIN_LEN)
    retval = ' '.join(sentence).replace(' ,', ',').replace(' .', '.').replace(' ?', '?').capitalize().replace(" i ", " I ").replace(" i\'", " I\'")
    return retval

def make_cdf(choices):
    cumsum = 0.0
    total = float(sum(choices.values()))
    cdf = []
    for key, value in choices.items():
        cumsum += value / total
        cdf.append((cumsum, key))
    return cdf

def weighted_choice(choices):
    cdf = make_cdf(choices)
    random_number = random.uniform(0,1)
    found = False
    i = 0
    while not found:
       cdf_val, token = cdf[i]
       i += 1
       if cdf_val >= random_number:
           found = True
    return token
