# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"


import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
interactions_matcher = Matcher(nlp.vocab)

# alone
alone1 = [{'LEMMA': 'on'}, {'LOWER': 'my'}, {'LEMMA': 'own'}]
alone2 = [{'LEMMA': 'by'}, {'LOWER': 'myself'}]
alone3 = [{'LEMMA': 'alone', 'POS': {'IN': ['ADV', 'ADJ']}}]

interactions_matcher.add('alone', None, alone1, alone2, alone3)


# animal
animal1 = [{'LEMMA': 'animal', 'POS': 'NOUN'}]
animal2 = [{'LEMMA': 'cat', 'POS': 'NOUN'}]
animal3 = [{'LEMMA': 'cub', 'POS': 'NOUN'}]
animal4 = [{'LEMMA': 'dog', 'POS': 'NOUN'}]
animal5 = [{'LOWER': 'doggie', 'POS': 'NOUN'}]
animal6 = [{'LOWER': 'doggo', 'POS': 'NOUN'}]
animal7 = [{'LOWER': 'doggy', 'POS': 'NOUN'}]
animal8 = [{'LEMMA': 'kitten', 'POS': 'NOUN'}]
animal9 = [{'LEMMA': 'kitty', 'POS': 'NOUN'}]
animal10 = [{'LEMMA': 'pet', 'POS': 'NOUN'}]
animal11 = [{'LEMMA': 'pup', 'POS': 'NOUN'}]
animal12 = [{'LEMMA': 'puppy', 'POS': 'NOUN'}]

interactions_matcher.add('animal', None, animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8,
                         animal9, animal10, animal11, animal12)


# cohabitants
cohabitants1 = [{'LEMMA': 'boarder', 'POS': 'NOUN'}]
cohabitants2 = [{'LEMMA': 'cohabitant', 'POS': 'NOUN'}]
cohabitants3 = [{'LEMMA': 'flat', 'POS': 'NOUN'}, {'LEMMA': 'mate', 'POS': 'NOUN'}]
cohabitants4 = [{'LEMMA': 'flat', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'mate', 'POS': 'NOUN'}]
cohabitants5 = [{'LEMMA': 'flatmate', 'POS': 'NOUN'}]
cohabitants6 = [{'LEMMA': 'house', 'POS': 'NOUN'}, {'LEMMA': 'mate', 'POS': 'NOUN'}]
cohabitants7 = [{'LEMMA': 'house', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'mate', 'POS': 'NOUN'}]
cohabitants8 = [{'LEMMA': 'housemate', 'POS': 'NOUN'}]
cohabitants9 = [{'LOWER': 'roomie', 'POS': 'NOUN'}]
cohabitants10 = [{'LOWER': 'roomies', 'POS': 'NOUN'}]
cohabitants11 = [{'LEMMA': 'roommate', 'POS': 'NOUN'}]
cohabitants12 = [{'LEMMA': 'room', 'POS': 'NOUN'}, {'LEMMA': 'mate', 'POS': 'NOUN'}]
cohabitants13 = [{'LEMMA': 'room', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'mate', 'POS': 'NOUN'}]
cohabitants14 = [{'LOWER': 'roomy', 'POS': 'NOUN'}]

interactions_matcher.add('cohabitants', None, cohabitants1, cohabitants2, cohabitants3, cohabitants4, cohabitants5,
                         cohabitants6, cohabitants7, cohabitants8, cohabitants9, cohabitants10, cohabitants11,
                         cohabitants12, cohabitants13, cohabitants14)


# colleagues
colleagues1 = [{'LEMMA': 'assistant', 'POS': 'NOUN'}]
colleagues2 = [{'LEMMA': 'boss', 'POS': 'NOUN'}]
colleagues3 = [{'LEMMA': 'chief', 'POS': 'NOUN'}]
colleagues4 = [{'LEMMA': 'client', 'POS': 'NOUN'}]
colleagues5 = [{'LEMMA': 'colleague', 'POS': 'NOUN'}]
colleagues6 = [{'LEMMA': 'co', 'POS': 'NOUN'}, {'LEMMA': 'worker', 'POS': 'NOUN'}]
colleagues7 = [{'LEMMA': 'co', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'worker', 'POS': 'NOUN'}]
colleagues8 = [{'LEMMA': 'coworker', 'POS': 'NOUN'}]
colleagues9 = [{'LEMMA': 'employee', 'POS': 'NOUN'}]
colleagues10 = [{'LEMMA': 'employer', 'POS': 'NOUN'}]
colleagues11 = [{'LEMMA': 'fellow', 'POS': 'NOUN'}]
colleagues12 = [{'LEMMA': 'fellow', 'POS': 'NOUN'}, {'LEMMA': 'worker', 'POS': 'NOUN'}]
colleagues13 = [{'LEMMA': 'work', 'POS': 'NOUN'}, {'LEMMA': 'mate', 'POS': 'NOUN'}]
colleagues14 = [{'LEMMA': 'work', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'mate', 'POS': 'NOUN'}]
colleagues15 = [{'LEMMA': 'workmate', 'POS': 'NOUN'}]

interactions_matcher.add('colleagues', None, colleagues1, colleagues2, colleagues3, colleagues4, colleagues5,
                         colleagues6, colleagues7, colleagues8, colleagues9, colleagues10, colleagues11, colleagues12,
                         colleagues13, colleagues14, colleagues15)

# friends
friends1 = [{'LOWER': 'bae'}]
friends2 = [{'LEMMA': 'boyfriend', 'POS': 'NOUN'}]
friends3 = [{'LOWER': 'bro'}]
friends4 = [{'LEMMA': 'buddy', 'POS': 'NOUN'}]
friends5 = [{'LEMMA': 'comrade', 'POS': 'NOUN'}]
friends6 = [{'LEMMA': 'date', 'POS': 'NOUN'}]
friends7 = [{'LEMMA': 'friend', 'POS': 'NOUN'}]
friends8 = [{'LEMMA': 'girlfriend', 'POS': 'NOUN'}]
friends9 = [{'LOWER': 'pal'}]

interactions_matcher.add('friends', None, friends1, friends2, friends3, friends4, friends5, friends6, friends7,
                         friends8, friends9)


# other
other1 = [{'LEMMA': 'assistant', 'POS': 'NOUN'}]
other2 = [{'LEMMA': 'doctor', 'POS': 'NOUN'}]
other3 = [{'LEMMA': 'g'}, {'IS_PUNCT': True}, {'LEMMA': 'p'}, {'IS_PUNCT': True}]
other4 = [{'LOWER': 'general'}, {'LOWER': 'partictioner'}]
other5 = [{'LOWER': 'gp'}]
other6 = [{'LEMMA': 'physician', 'POS': 'NOUN'}]
other7 = [{'LEMMA': 'stranger', 'POS': 'NOUN'}]
other8 = [{'LEMMA': 'vet', 'POS': 'NOUN'}]
other9 = [{'LEMMA': 'veterinary', 'POS': 'NOUN'}]
other10 = [{'LEMMA': 'teacher', 'POS': 'NOUN'}]
other11 = [{'LEMMA': 'professor', 'POS': 'NOUN'}]

interactions_matcher.add('other', None, other1, other2, other3, other4, other5, other6, other7, other8, other9, other10,
                         other11)

# family
family1 = [{'LEMMA': 'aunty', 'POS': 'NOUN'}]
family2 = [{'LEMMA': 'aunt', 'POS': 'NOUN'}]
family3 = [{'LEMMA': 'aunty', 'POS': 'NOUN'}]
family4 = [{'LEMMA': 'babe', 'POS': 'NOUN'}]
family5 = [{'LEMMA': 'baby', 'POS': 'NOUN'}]
family6 = [{'LEMMA': 'baby', 'POS': 'NOUN'}, {'LEMMA': 'boy', 'POS': 'NOUN'}]
family7 = [{'LEMMA': 'baby', 'POS': 'NOUN'}, {'LEMMA': 'girl', 'POS': 'NOUN'}]
family8 = [{'LOWER': 'better'}, {'LEMMA': 'half', 'POS': 'NOUN'}]
family9 = [{'LEMMA': 'boy', 'POS': 'NOUN'}]
family10 = [{'LEMMA': 'brother', 'POS': 'NOUN'}]
family11 = [{'LEMMA': 'child', 'POS': 'NOUN'}]
family12 = [{'LEMMA': 'dad', 'POS': 'NOUN'}]
family13 = [{'LEMMA': 'dada', 'POS': 'NOUN'}]
family14 = [{'LEMMA': 'daddy', 'POS': 'NOUN'}]
family15 = [{'LEMMA': 'daughter', 'POS': 'NOUN'}]
family16 = [{'LEMMA': 'family', 'POS': 'NOUN'}]
family17 = [{'LEMMA': 'father', 'POS': 'NOUN'}]
family18 = [{'LEMMA': 'girl', 'POS': 'NOUN'}]
family19 = [{'LOWER': 'gramps'}]
family20 = [{'LEMMA': 'grandad', 'POS': 'NOUN'}]
family21 = [{'LEMMA': 'mother', 'POS': 'NOUN'}]

family22 = [{'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'in'}, {'IS_PUNCT': True}, {'LEMMA': 'law', 'POS': 'NOUN'}]
family23 = [{'POS': 'NOUN'}, {'LEMMA': 'in'}, {'LEMMA': 'law', 'POS': 'NOUN'}]
family24 = [{'LEMMA': 'fatherinlaw', 'POS': 'NOUN'}]
family25 = [{'LEMMA': 'motherinlaw', 'POS': 'NOUN'}]
family26 = [{'LEMMA': 'brotherinlaw', 'POS': 'NOUN'}]
family27 = [{'LEMMA': 'sisterinlaw', 'POS': 'NOUN'}]


family28 = [{'LEMMA': 'grand', 'POS': 'ADJ'}, {'IS_PUNCT': True}, {'POS': 'NOUN'}]
family29 = [{'LEMMA': 'grand', 'POS': 'ADJ'}, {'POS': 'NOUN'}]
family30 = [{'LEMMA': 'granddad', 'POS': 'NOUN'}]
family31 = [{'LEMMA': 'grandchild', 'POS': 'NOUN'}]
family32 = [{'LEMMA': 'granddaughter', 'POS': 'NOUN'}]
family33 = [{'LEMMA': 'grandfather', 'POS': 'NOUN'}]
family34 = [{'LEMMA': 'grandma', 'POS': 'NOUN'}]
family35 = [{'LEMMA': 'grandmother', 'POS': 'NOUN'}]
family36 = [{'LEMMA': 'grandmum', 'POS': 'NOUN'}]
family37 = [{'LEMMA': 'grandmam', 'POS': 'NOUN'}]
family38 = [{'LEMMA': 'grandpa', 'POS': 'NOUN'}]
family39 = [{'LEMMA': 'grandson', 'POS': 'NOUN'}]
family40 = [{'LEMMA': 'granny', 'POS': 'NOUN'}]

family41 = [{'LEMMA': 'half', 'POS': 'ADJ'}, {'POS': 'NOUN'}]
family42 = [{'LEMMA': 'step', 'POS': 'ADJ'}, {'POS': 'NOUN'}]
family43 = [{'LEMMA': 'half', 'POS': 'ADJ'}, {'IS_PUNCT': True}, {'POS': 'NOUN'}]
family44 = [{'LEMMA': 'step', 'POS': 'ADJ'}, {'IS_PUNCT': True}, {'POS': 'NOUN'}]

family45 = [{'LEMMA': 'in'}, {'IS_PUNCT': True}, {'LOWER': 'laws'}]

family46 = [{'LEMMA': 'halfbrother', 'POS': 'NOUN'}]
family47 = [{'LEMMA': 'halfsister', 'POS': 'NOUN'}]
family48 = [{'LEMMA': 'husband', 'POS': 'NOUN'}]
family49 = [{'LEMMA': 'infant', 'POS': 'NOUN'}]
family50 = [{'LEMMA': 'kid', 'POS': 'NOUN'}]
family51 = [{'LOWER': 'kiddo', 'POS': 'NOUN'}]
family52 = [{'LOWER': 'kiddos', 'POS': 'NOUN'}]
family53 = [{'LEMMA': 'ma', 'POS': 'NOUN'}]
family54 = [{'LEMMA': 'mama', 'POS': 'NOUN'}]
family55 = [{'LEMMA': 'mate', 'POS': 'NOUN'}]
family56 = [{'LEMMA': 'mom', 'POS': 'NOUN'}]
family57 = [{'LEMMA': 'momma', 'POS': 'NOUN'}]
family58 = [{'LEMMA': 'mommy', 'POS': 'NOUN'}]
family59 = [{'LEMMA': 'mum', 'POS': 'NOUN'}]
family60 = [{'LEMMA': 'mummy', 'POS': 'NOUN'}]
family61 = [{'LEMMA': 'nana', 'POS': 'NOUN'}]
family62 = [{'LEMMA': 'nanny', 'POS': 'NOUN'}]
family63 = [{'LEMMA': 'nephew', 'POS': 'NOUN'}]
family64 = [{'LEMMA': 'niece', 'POS': 'NOUN'}]
family65 = [{'LEMMA': 'pa', 'POS': 'NOUN'}]
family66 = [{'LEMMA': 'pap', 'POS': 'NOUN'}]
family67 = [{'LEMMA': 'papa', 'POS': 'NOUN'}]
family68 = [{'LEMMA': 'pappa', 'POS': 'NOUN'}]
family69 = [{'LEMMA': 'parent', 'POS': 'NOUN'}]
family70 = [{'LEMMA': 'partner', 'POS': 'NOUN'}]
family71 = [{'LEMMA': 'pop', 'POS': 'NOUN'}]
family72 = [{'LEMMA': 'poppa', 'POS': 'NOUN'}]
family73 = [{'LEMMA': 'relative', 'POS': 'NOUN'}]
family74 = [{'LEMMA': 'sib', 'POS': 'NOUN'}]
family75 = [{'LEMMA': 'sibling', 'POS': 'NOUN'}]
family76 = [{'LEMMA': 'significant'}, {'LEMMA': 'other'}]
family77 = [{'LEMMA': 'son', 'POS': 'NOUN'}]
family78 = [{'LEMMA': 'stepbrother', 'POS': 'NOUN'}]
family79 = [{'LEMMA': 'stepdad', 'POS': 'NOUN'}]
family80 = [{'LEMMA': 'stepdaddy', 'POS': 'NOUN'}]
family81 = [{'LEMMA': 'stepfather', 'POS': 'NOUN'}]
family82 = [{'LEMMA': 'stepmama', 'POS': 'NOUN'}]
family83 = [{'LEMMA': 'stepmom', 'POS': 'NOUN'}]
family84 = [{'LEMMA': 'stepmother', 'POS': 'NOUN'}]
family85 = [{'LEMMA': 'stepmum', 'POS': 'NOUN'}]
family86 = [{'LEMMA': 'stepsister', 'POS': 'NOUN'}]
family87 = [{'LEMMA': 'toddler', 'POS': 'NOUN'}]
family88 = [{'LEMMA': 'twin', 'POS': 'NOUN'}]
family89 = [{'LEMMA': 'und', 'POS': 'NOUN'}]
family90 = [{'LEMMA': 'uncle', 'POS': 'NOUN'}]
family91 = [{'LEMMA': 'wife', 'POS': 'NOUN'}]

family92 = [{'POS': 'NUM'}, {'LEMMA': 'year'}, {'LEMMA': 'old'}]
family93 = [{'POS': 'NUM'}, {'LEMMA': 'month'}, {'LEMMA': 'old'}]
family94 = [{'POS': 'NUM'}, {'IS_PUNCT': True}, {'LEMMA': 'year'}, {'IS_PUNCT': True}, {'LEMMA': 'old'}]
family95 = [{'POS': 'NUM'}, {'IS_PUNCT': True}, {'LEMMA': 'month'}, {'IS_PUNCT': True}, {'LEMMA': 'old'}]

interactions_matcher.add('family', None, family1, family2, family3, family4, family5, family6, family7, family8,
                         family9, family10, family11, family12, family13, family14, family15, family16, family17,
                         family18, family19, family20, family21, family22, family23, family24, family25, family26,
                         family27, family28, family29, family30, family31, family32, family33, family34, family35,
                         family36, family37, family38, family39, family40, family41, family42, family43, family44,
                         family45, family46, family47, family48, family49, family50, family51, family52, family53,
                         family54, family55, family56, family57, family58, family59, family60, family61, family62,
                         family63, family64, family65, family66, family67, family68, family69, family70, family71,
                         family72, family73, family74, family75, family76, family77, family78, family79, family80,
                         family81, family82, family83, family84, family85, family86, family87, family88, family89,
                         family90, family91, family92, family93, family94, family95)


def match(sentence):
    matches = interactions_matcher(sentence)
    return matches
