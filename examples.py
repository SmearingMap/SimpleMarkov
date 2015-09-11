from markov import *
import os

###I am aware that this is awful code, but I wanted to get examples up and running very quicklyy


def load_trump():
    f = open('example_text'+os.sep+'trump.txt')
    text = map(lambda x: x.rstrip(), f.readlines())
    f.close()
    text = filter(lambda x: not 'APPLAUSE' in x, text)
    text = filter(lambda x: not x.startswith('AUDIENCE'), text)
    text = map(lambda x: x.replace('TRUMP: ', ''), text)
    text = map(lambda x: x.replace("\"", ''), text)
    text = filter(lambda x: x != '', text)
    return tokenize('\n'.join(text))

def load_cruz():
    f = open('example_text'+os.sep+'cruz.txt')
    text = map(lambda x: x.rstrip(), f.readlines())
    f.close()
    text = filter(lambda x: not 'APPLAUSE' in x, text)
    text = filter(lambda x: not x.startswith('AUDIENCE'), text)
    text = map(lambda x: x.replace('CRUZ: ', ''), text)
    text = map(lambda x: x.replace("\"", ''), text)
    text = filter(lambda x: x != '', text)
    return tokenize('\n'.join(text))

def load_huckabee():
    f = open('example_text'+os.sep+'huckabee.txt')
    text = map(lambda x: x.rstrip(), f.readlines())
    f.close()
    text = filter(lambda x: not 'APPLAUSE' in x, text)
    text = filter(lambda x: not x.startswith('AUDIENCE'), text)
    text = map(lambda x: x.replace("\"", ''), text)
    text = filter(lambda x: x != '', text)
    return tokenize('\n'.join(text))

def load_clinton():
    f = open('example_text'+os.sep+'clinton.txt')
    text = map(lambda x: x.rstrip(), f.readlines())
    f.close()
    text = filter(lambda x: not 'APPLAUSE' in x, text)
    text = filter(lambda x: not x.startswith('AUDIENCE'), text)
    text = map(lambda x: x.replace("\"", ''), text)
    text = filter(lambda x: x != '', text)
    return tokenize('\n'.join(text))

if __name__ == '__main__':
    cruz = load_cruz()
    trump = load_trump()
    huckabee = load_huckabee()
    clinton = load_clinton()
    print
    print "Ted Cruz: ", gen_sentence(cruz)
    print
    print "Donald Trump: ", gen_sentence(trump)
    print
    print "Mike Huckabee: ", gen_sentence(huckabee)
    print
    print "Hillary Clinton: ", gen_sentence(clinton)
    print
