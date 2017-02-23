import sys

vowels = 'eyuioa'
consonants = 'qwrtpsdfghjklzxcvbnm'
cluster = ['ch','zh','sh','th','wh','ck','gh']

def first_vowel(string):
    position = -1
    for letter in string:
        position += 1
        if letter in vowels:
            return position
    return -1

def is_cluster(string):
    return (string+'00')[0:2] in cluster

def vowel_convert (string):
    # if word begins with vowel sounds add "way" to the end
    return string + 'way'

def consonant_convert (string, pos):
    # if word begins with consonant sounds all letters before the initial vowel are placed at the end of the word sequence, then, "ay" is added
    # if words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end when speaking or writing
    if is_cluster(string):
        return string[2:] + string[0:2] + 'ay'
    return string[pos:]+string[0:pos]+'ay'

def no_convert(string):
    return string+'ay'

def pig_latin(args):
    for arg in args:
        first_vowel_position = first_vowel(arg)
        if first_vowel_position < 0:
            print('%s becomes %s' % (arg, no_convert(arg)))
        elif first_vowel_position == 0:
            print ('%s becomes %s' % (arg, vowel_convert(arg)))
        else:
            print('%s becomes %s' % (arg, consonant_convert(arg, first_vowel_position)))

pig_latin(sys.argv[1:])