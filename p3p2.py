import glob, os, re
from math import log

def strip(word):
    result = ""
    for i in word:
        if i not in ".?,\"'-&#1234567890@()*:;[]{}<>$%^=+/\\|\n":
            result += i
    return result

def charCount(string):
    char_count = {}
    line = strip(string)
    for i in line:
        if i not in char_count:
            char_count[i] = 0
        char_count[i] += 1
    return char_count

def list_bigrams(string): #ordered list w/ repeats
    result = []
    begin = True
    line = strip(string)
    for i in line:
        if begin:
            result.append(i)
            begin = False
        else:
            result[-1] += i
        result.append(i)
    if len(result) > 0:
        result.pop()
    return result

def language(infile, is_file=True): #dictionary
    bigrams = {}
    char_counts = {}
    if is_file:
        lines = open(infile)
    else:
        lines = [infile]
    for line in lines:
        counts = charCount(line)
        for letter in counts:
            if letter not in char_counts:
                char_counts[letter] = 0
            char_counts[letter] += counts[letter]
        for bigram in list_bigrams(line):
            if bigram not in bigrams:
                bigrams[bigram] = 0
            bigrams[bigram] += 1
    if is_file:
        lines.close()
    return bigrams, char_counts

def probability(test_bigram, test_char, bigrams):
    pLog = 0.0
    for bigram in bigrams:
        if bigram in test_bigram:
            P = float(test_bigram[bigram]) / float(test_char[bigram[0]])
            pLog += log(P)
    return pLog

if __name__ == "__main__":
    path = "language.identification/training/"
    english_bigrams, english_char_counts = language(path + 'English')
    french_bigrams, french_char_counts = language(path + 'French')
    italian_bigrams, italian_char_counts = language(path + 'Italian')
    german_bigrams, german_char_count = language(path + 'German')

    #P_th_english = float(english_bigrams['th']) / english_char_counts['t']
    i = 1
    for line in open('language.identification/test'):
        bigrams, _ = language(line, False)
        pEnglish = probability(english_bigrams, english_char_counts, bigrams)
        pFrench = probability(french_bigrams, french_char_counts, bigrams)
        pItalian = probability(italian_bigrams, italian_char_counts, bigrams)
        pGerman = probability(german_bigrams, german_char_count, bigrams)

        

        if (pEnglish > pFrench) and (pEnglish > pItalian):
            print str(i) + " English"
        elif (pFrench > pEnglish) and (pFrench > pItalian):
            print str(i) + " French"
        else:
            print str(i) + " Italian"
        i += 1
