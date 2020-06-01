# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"

import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
places_matcher = Matcher(nlp.vocab)

# education
education1 = [{'LEMMA': 'campus', 'POS': 'NOUN'}]
education2 = [{'LEMMA': 'class', 'POS': 'NOUN'}]
education3 = [{'LEMMA': 'classroom', 'POS': 'NOUN'}]
education4 = [{'LEMMA': 'college', 'POS': 'NOUN'}]
education5 = [{'LEMMA': 'school', 'POS': 'NOUN'}]
education6 = [{'LEMMA': 'uni', 'POS': {'IN': ['NOUN', 'PROPN']}}]
education7 = [{'LEMMA': 'university', 'POS': 'NOUN'}]

places_matcher.add('education', None, education1, education2, education3, education4, education5, education6,
                   education7)

# home
home1 = [{'LEMMA': 'bathroom', 'POS': 'NOUN'}]
home2 = [{'LEMMA': 'bed', 'POS': 'NOUN'}]
home3 = [{'LEMMA': 'bedroom', 'POS': 'NOUN'}]
home4 = [{'LEMMA': 'chair', 'POS': 'NOUN'}]
home5 = [{'LEMMA': 'couch', 'POS': 'NOUN'}]
home6 = [{'LEMMA': 'dining', 'POS': 'NOUN'}, {'LEMMA': 'room', 'POS': 'NOUN'}]
home7 = [{'LEMMA': 'garage', 'POS': 'NOUN'}]
home8 = [{'LEMMA': 'home', 'POS': 'NOUN'}]
home9 = [{'LEMMA': 'home', 'POS': 'NOUN'}, {'LEMMA': 'office', 'POS': 'NOUN'}]
home10 = [{'LEMMA': 'kitchen', 'POS': 'NOUN'}]
home11 = [{'LEMMA': 'living', 'POS': 'NOUN'}, {'LEMMA': 'room', 'POS': 'NOUN'}]
home12 = [{'LEMMA': 'pantry', 'POS': 'NOUN'}]
home13 = [{'LEMMA': 'sofa', 'POS': 'NOUN'}]

places_matcher.add('home', None, home1, home2, home3, home4, home5, home6, home7, home8, home9, home10, home11, home12,
                   home13)

# leisure
leisure1 = [{'LEMMA': 'bathroom', 'POS': 'NOUN'}]
leisure2 = [{'LEMMA': 'cafe', 'POS': 'NOUN'}]
leisure3 = [{'LEMMA': 'café', 'POS': 'NOUN'}]  # check this
leisure4 = [{'LEMMA': 'cinema', 'POS': 'NOUN'}]
leisure5 = [{'LEMMA': 'club', 'POS': 'NOUN'}]
leisure6 = [{'LEMMA': 'coffee', 'POS': 'NOUN'}, {'LEMMA': 'place', 'POS': 'NOUN'}]
leisure7 = [{'LEMMA': 'gym', 'POS': 'NOUN'}]
leisure8 = [{'LEMMA': 'library', 'POS': 'NOUN'}]
leisure9 = [{'LEMMA': 'museum', 'POS': 'NOUN'}]
leisure10 = [{'LEMMA': 'pool', 'POS': 'NOUN'}]
leisure11 = [{'LEMMA': 'pub', 'POS': 'NOUN'}]
leisure12 = [{'LEMMA': 'restaurant', 'POS': 'NOUN'}]
leisure13 = [{'LEMMA': 'shop', 'POS': 'NOUN'}]
leisure14 = [{'LEMMA': 'store', 'POS': 'NOUN'}]
leisure15 = [{'LEMMA': 'swimming', 'POS': 'NOUN'}, {'LEMMA': 'pool', 'POS': 'NOUN'}]
leisure16 = [{'LEMMA': 'theater', 'POS': 'NOUN'}]
leisure17 = [{'LEMMA': 'theatre', 'POS': 'NOUN'}]

places_matcher.add('leisure', None, leisure1, leisure2, leisure3, leisure4, leisure5, leisure6, leisure7, leisure8,
                   leisure9, leisure10, leisure11, leisure12, leisure13, leisure14, leisure15, leisure16, leisure17)


# other
other1 = [{'LEMMA': 'hospital', 'POS': 'NOUN'}]
other2 = [{'LEMMA': 'toilet', 'POS': 'NOUN'}]
other3 = [{'LEMMA': 'hotel', 'POS': 'NOUN'}]
other4 = [{'LEMMA': 'motel', 'POS': 'NOUN'}]
other5 = [{'LOWER': 'airbnb', 'POS': 'NOUN'}]
other6 = [{'LOWER': 'bnb', 'POS': 'NOUN'}]

places_matcher.add('other', None, other1, other2, other3, other4, other5, other6)


# outdoor
outdoor1 = [{'LEMMA': 'back', 'POS': 'NOUN'}, {'LEMMA': 'yard', 'POS': 'NOUN'}]
outdoor2 = [{'LEMMA': 'back', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'yard', 'POS': 'NOUN'}]
outdoor3 = [{'LEMMA': 'backyard', 'POS': 'NOUN'}]
outdoor4 = [{'LEMMA': 'beach', 'POS': 'NOUN'}]
outdoor5 = [{'LEMMA': 'camp', 'POS': {'IN': ['NOUN', 'VERB']}}]
outdoor6 = [{'LEMMA': 'cliff', 'POS': 'NOUN'}]
outdoor7 = [{'LEMMA': 'forest', 'POS': 'NOUN'}]
outdoor8 = [{'LEMMA': 'front', 'POS': 'NOUN'}, {'LEMMA': 'yard', 'POS': 'NOUN'}]
outdoor9 = [{'LEMMA': 'front', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'yard', 'POS': 'NOUN'}]
outdoor10 = [{'LEMMA': 'front', 'POS': 'NOUN'}]
outdoor11 = [{'LEMMA': 'garden', 'POS': 'NOUN'}]
outdoor12 = [{'LEMMA': 'hill', 'POS': 'NOUN'}]
outdoor13 = [{'LEMMA': 'hill', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'side', 'POS': 'NOUN'}]
outdoor14 = [{'LEMMA': 'hill', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'top', 'POS': 'NOUN'}]
outdoor15 = [{'LEMMA': 'hill', 'POS': 'NOUN'}, {'LEMMA': 'side', 'POS': 'NOUN'}]
outdoor16 = [{'LEMMA': 'hill', 'POS': 'NOUN'}, {'LEMMA': 'top', 'POS': 'NOUN'}]
outdoor17 = [{'LEMMA': 'hillside', 'POS': 'NOUN'}]
outdoor18 = [{'LEMMA': 'hilltop', 'POS': 'NOUN'}]
outdoor19 = [{'LEMMA': 'lake', 'POS': 'NOUN'}]
outdoor20 = [{'LEMMA': 'mountain', 'POS': 'NOUN'}]
outdoor21 = [{'LEMMA': 'mountain', 'POS': 'NOUN'}, {'LEMMA': 'side', 'POS': 'NOUN'}]
outdoor22 = [{'LEMMA': 'mountain', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'side', 'POS': 'NOUN'}]
outdoor23 = [{'LEMMA': 'mountainside', 'POS': 'NOUN'}]
outdoor24 = [{'LEMMA': 'outdoor', 'POS': {'IN': ['ADJ', 'ADV']}}]
outdoor25 = [{'LEMMA': 'outside', 'POS': 'ADV'}]
outdoor26 = [{'LEMMA': 'park', 'POS': 'NOUN'}]
outdoor27 = [{'LEMMA': 'path', 'POS': 'NOUN'}]
outdoor28 = [{'LEMMA': 'peak', 'POS': 'NOUN'}]
outdoor29 = [{'LEMMA': 'river', 'POS': 'NOUN'}]
outdoor30 = [{'LEMMA': 'sea', 'POS': 'NOUN'}, {'LEMMA': 'shore', 'POS': 'NOUN'}]
outdoor31 = [{'LEMMA': 'sea', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'shore', 'POS': 'NOUN'}]
outdoor32 = [{'LEMMA': 'seashore', 'POS': 'NOUN'}]
outdoor33 = [{'LEMMA': 'sea', 'POS': 'NOUN'}, {'LEMMA': 'side', 'POS': 'NOUN'}]
outdoor34 = [{'LEMMA': 'sea', 'POS': 'NOUN'}, {'IS_PUNCT': True}, {'LEMMA': 'side', 'POS': 'NOUN'}]
outdoor35 = [{'LEMMA': 'seaside', 'POS': 'NOUN'}]
outdoor36 = [{'LEMMA': 'shore', 'POS': 'NOUN'}]
outdoor37 = [{'LEMMA': 'sport', 'POS': 'NOUN'}, {'LEMMA': 'ground', 'POS': 'NOUN'}]
outdoor38 = [{'LEMMA': 'trail', 'POS': 'NOUN'}]
outdoor39 = [{'LEMMA': 'wood', 'POS': 'NOUN'}]
outdoor40 = [{'LEMMA': 'yard', 'POS': 'NOUN'}]

places_matcher.add('outdoor', None, outdoor1, outdoor2, outdoor3, outdoor4, outdoor5, outdoor6, outdoor7, outdoor8,
                   outdoor9, outdoor10, outdoor11, outdoor12, outdoor13, outdoor14, outdoor15, outdoor16, outdoor17,
                   outdoor18, outdoor19, outdoor20, outdoor21, outdoor22, outdoor23, outdoor24, outdoor25, outdoor26,
                   outdoor27, outdoor28, outdoor29, outdoor30, outdoor31, outdoor32, outdoor33, outdoor34, outdoor35,
                   outdoor36, outdoor37, outdoor38, outdoor39, outdoor40)


# workplace
workplace1 = [{'LEMMA': 'administration', 'POS': 'NOUN'}]
workplace2 = [{'LEMMA': 'job', 'POS': 'NOUN'}]
workplace3 = [{'LEMMA': 'office', 'POS': 'NOUN'}]
workplace4 = [{'LEMMA': 'work', 'POS': 'NOUN'}]
workplace5 = [{'LEMMA': 'workplace', 'POS': 'NOUN'}]

places_matcher.add('workplace', None, workplace1, workplace2, workplace3, workplace4, workplace5)


def match(sentence):
    matches = places_matcher(sentence)
    return matches




