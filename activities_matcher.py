# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"

import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
activities_matcher = Matcher(nlp.vocab)

# communicating
communicating1 = [{'LEMMA': 'chat', 'POS': 'VERB'}]
communicating2 = [{'LEMMA': 'communicate', 'POS': 'VERB'}]
communicating3 = [{'LEMMA': 'converse', 'POS': 'VERB'}]
communicating4 = [{'LEMMA': 'socialise', 'POS': 'VERB'}]
communicating5 = [{'LEMMA': 'socialize', 'POS': 'VERB'}]
communicating6 = [{'LEMMA': 'speak', 'POS': 'VERB'}]
communicating7 = [{'LEMMA': 'talk', 'POS': 'VERB'}]

activities_matcher.add('communicating', None, communicating1, communicating2, communicating3, communicating4,
                       communicating5, communicating6, communicating7)

# commuting
commuting1 = [{'LOWER': 'aeroplane', 'POS': 'NOUN'}]
commuting2 = [{'LOWER': 'airplane', 'POS': 'NOUN'}]
commuting3 = [{'LOWER': 'airport', 'POS': 'NOUN'}]
commuting4 = [{'LOWER': 'bus', 'POS': 'NOUN'}]
commuting5 = [{'LOWER': 'cab', 'POS': 'NOUN'}]
commuting6 = [{'LOWER': 'car', 'POS': 'NOUN'}]
commuting7 = [{'LOWER': 'commute', 'LEMMA': 'commute', 'POS': 'NOUN'}]
commuting8 = [{'LEMMA': 'commute', 'POS': 'VERB'}]
commuting9 = [{'LEMMA': 'drive', 'POS': 'VERB'}]
commuting10 = [{'LOWER': 'metro', 'POS': 'NOUN'}]
commuting11 = [{'LOWER': 'plane', 'POS': 'NOUN'}]
commuting12 = [{'LOWER': 'station', 'POS': 'NOUN'}]
commuting13 = [{'LOWER': 'taxi', 'POS': 'NOUN'}]
commuting14 = [{'LOWER': 'train', 'POS': 'NOUN'}]
commuting15 = [{'LOWER': 'travel', 'POS': 'NOUN'}]
commuting16 = [{'LEMMA': 'travel', 'POS': 'VERB'}]
commuting17 = [{'LOWER': 'tube', 'POS': 'NOUN'}]
commuting18 = [{'LOWER': 'underground', 'POS': 'NOUN'}]
commuting19 = [{'POS': 'NOUN'}, {'LOWER': 'station', 'POS': 'NOUN'}]  # compounds with station

activities_matcher.add('commuting', None, commuting1, commuting2, commuting3, commuting4, commuting5, commuting6,
                       commuting7, commuting8, commuting9, commuting10, commuting11, commuting12, commuting13,
                       commuting14, commuting15, commuting16, commuting17, commuting18, commuting19)

# drinking-alcohol
alcohol1 = [{'LOWER': 'beer', 'POS': 'NOUN'}]
alcohol2 = [{'LOWER': 'can', 'POS': {'NOT_IN': ['VERB', 'AUX']}}]
alcohol3 = [{'LOWER': 'cider', 'POS': 'NOUN'}]
alcohol4 = [{'LOWER': 'cocktail', 'POS': 'NOUN'}]
alcohol5 = [{'LOWER': 'drink', 'POS': {'NOT_IN': ['VERB']}}]
alcohol6 = [{'LOWER': 'liquor', 'POS': 'NOUN'}]
alcohol7 = [{'LOWER': 'mead', 'POS': 'NOUN'}]
alcohol8 = [{'LOWER': 'pint', 'POS': 'NOUN'}]
alcohol9 = [{'LOWER': 'wine', 'POS': 'NOUN'}]

activities_matcher.add('alcohol', None, alcohol1, alcohol2, alcohol3, alcohol4, alcohol5, alcohol6, alcohol7,
                       alcohol8, alcohol9)

# eating
eating1 = [{'LEMMA': 'brunch', 'POS': 'NOUN'}]
eating2 = [{'LEMMA': 'eat', 'POS': 'VERB'}]
eating3 = [{'LEMMA': {'NOT_IN': ['cook', 'prepare', 'make']}}, {'LEMMA': 'breakfast', 'POS': 'NOUN'}]
eating4 = [{'LEMMA': {'NOT_IN': ['cook', 'prepare', 'make']}}, {'LEMMA': 'lunch', 'POS': 'NOUN'}]
eating5 = [{'LEMMA': {'NOT_IN': ['cook', 'prepare', 'make']}}, {'LEMMA': 'dinner', 'POS': 'NOUN'}]
eating13 = [{'LEMMA': {'NOT_IN': ['cook', 'prepare', 'make']}}, {'POS': 'DET'}, {'LEMMA': {'IN': ['breakfast', 'lunch', 'dinner']}}]
eating6 = [{'LEMMA': 'water', 'POS': 'NOUN'}]
eating7 = [{'LEMMA': 'coffee', 'POS': 'NOUN'}]
eating8 = [{'LEMMA': 'juice', 'POS': 'NOUN'}]
eating9 = [{'LEMMA': 'tea', 'POS': 'NOUN'}]
eating10 = [{'LEMMA': 'snack', 'POS': 'NOUN'}]
eating11 = [{'LEMMA': 'cup'}, {'LEMMA': 'of'}, {'POS': 'NOUN'}]
eating12 = [{'LEMMA': 'eat', 'POS': 'VERB'}, {'POS': 'NOUN'}]  # eating breakfast
eating13 = [{'LEMMA': 'eat', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # eating my breakfast
eating14 = [{'LEMMA': 'eat', 'POS': 'VERB'}, {'POS': 'NOUN'},  {'POS': 'NOUN'}]  # eating ice cream


activities_matcher.add('eating', None, eating1, eating2, eating3, eating4, eating5, eating6, eating7, eating8, eating9,
                       eating10, eating11, eating12, eating13, eating14)

# grooming
grooming1 = [{'LEMMA': 'bath', 'POS': 'NOUN'}]
grooming2 = [{'LEMMA': 'hair', 'POS': 'NOUN'}]
grooming3 = [{'LEMMA': 'teeth', 'POS': 'NOUN'}]
grooming4 = [{'LEMMA': 'groom', 'POS': 'VERB'}]
grooming5 = [{'LEMMA': 'haircut', 'POS': 'NOUN'}]
grooming6 = [{'LEMMA': 'hair'}, {'LEMMA': 'cut'}]
grooming7 = [{'LEMMA': 'hair'}, {'IS_PUNCT': True}, {'LEMMA': 'cut'}]
grooming8 = [{'LEMMA': 'shave'}]
grooming9 = [{'LEMMA': 'shower'}]

activities_matcher.add('grooming', None, grooming1, grooming2, grooming3, grooming4, grooming5, grooming6, grooming7,
                       grooming8, grooming9)

# leisure
leisure1 = [{'LEMMA': 'book', 'POS': 'NOUN'}]  # book
leisure2 = [{'LEMMA': 'computer', 'POS': 'NOUN'}]  # computer
leisure3 = [{'LEMMA': 'dance', 'POS': 'VERB'}]  # dance
leisure4 = [{'LEMMA': 'draw', 'POS': 'VERB'}]  # draw
leisure5 = [{'LEMMA': 'game', 'POS': {'IN': ['NOUN', 'VERB']}}]  # game
leisure6 = [{'LEMMA': 'kint', 'POS': 'VERB'}]  # knit
leisure7 = [{'LEMMA': 'laptop', 'POS': 'NOUN'}]  # laptop
leisure8 = [{'LEMMA': 'leisure', 'POS': 'NOUN'}]  # leisure
leisure9 = [{'LEMMA': {'IN': ['movie', 'film', 'video', 'serie', 'show']}, 'POS': 'NOUN'}]  # movies and co
leisure10 = [{'LEMMA': 'music', 'POS': 'NOUN'}]  # music
leisure11 = [{'LOWER': 'netflix'}]  # netflix
leisure12 = [{'LOWER': 'online'}]  # online
leisure13 = [{'LOWER': 'on'}, {'LOWER': 'line'}]  # on line
leisure14 = [{'LOWER': 'on'}, {'IS_PUNCT': True}, {'LOWER': 'line'}]  # on-line
leisure15 = [{'LEMMA': 'phone', 'POS': {'IN': ['NOUN', 'VERB']}}]  # phone
leisure16 = [{'LEMMA': 'play', 'POS': 'VERB'}]  # play
leisure17 = [{'LOWER': 'prime', 'POS': 'PROPN'}]  # prime
leisure18 = [{'LEMMA': 'radio', 'POS': 'NOUN'}]  # radio
leisure19 = [{'LEMMA': 'read', 'POS': 'VERB'}]  # reading
leisure20 = [{'LEMMA': 'series', 'POS': 'PROPN'}]  # series
leisure21 = [{'LEMMA': 'shop', 'POS': 'VERB'}]  # shop
leisure22 = [{'LEMMA': 'sing', 'POS': 'VERB'}]  # sing
leisure23 = [{'LOWER': 'tv'}]  # tv
leisure24 = [{'LOWER': 't'}, {'IS_PUNCT': True}, {'LOWER': 'v'}, {'IS_PUNCT': True}]  # t.v.
leisure25 = [{'LEMMA': 'telephone', 'POS': {'IN': ['NOUN', 'VERB']}}]  # telephone
leisure26 = [{'LEMMA': 'television', 'POS': 'NOUN'}]  # television
leisure27 = [{'LEMMA': 'videogame', 'POS': 'NOUN'}]  # videogame
leisure28 = [{'LEMMA': 'video'}, {'LEMMA': 'game'}]  # video game
leisure29 = [{'LEMMA': 'video'}, {'IS_PUNCT': True}, {'LEMMA': 'game'}]  # video-game
leisure30 = [{'LOWER': 'you'}, {'LOWER': 'tube'}]  # you tube
leisure31 = [{'LOWER': 'youtube'}]  # youtube YouTube

leisure32 = [{'LEMMA': 'play', 'POS': 'VERB'}, {'POS': 'NOUN'}]  # playing music, playing violin, playing videogames
leisure33 = [{'LEMMA': 'play', 'POS': 'VERB'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}]  # play video games
leisure34 = [{'LEMMA': {'IN': ['play', 'sing']}, 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # play the piano, sing a song
leisure35 = [{'LEMMA': 'do', 'POS': {'IN': ['AUX', 'VERB']}}, {'LEMMA': 'craft', 'POS': 'NOUN'}]  # do craft
leisure36 = [{'LEMMA': 'tv', 'POS': 'NOUN'}, {'POS': 'NOUN'}]  # tv show, tv serie
leisure37 = [{'LEMMA': 'listen', 'POS': 'VERB'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]  # listening to music
leisure38 = [{'LEMMA': 'listen', 'POS': 'VERB'}, {'POS': 'ADP'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # listening to some music, listening to the radio
leisure39 = [{'LEMMA': 'watch', 'POS': 'VERB'}, {'POS': 'NOUN'}]  # watching tv
leisure40 = [{'LEMMA': 'watch', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # watching a movie
leisure41 = [{'LEMMA': 'watch', 'POS': 'VERB'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}]  # watching youtube videos
leisure42 = [{'LEMMA': 'watch', 'POS': 'VERB'}, {'POS': 'ADJ'}, {'POS': 'NOUN'}]  # watching music videos
leisure43 = [{'POS': 'VERB'}, {'LEMMA': 'tv'}]  # watching tv
leisure44 = [{'LEMMA': 'watch', 'POS': 'VERB'}, {'POS': 'NOUN'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]  # watching videos on youtube
leisure45 = [{'LEMMA': 'watch', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]  # watching a video on youtube
leisure46 = [{'LEMMA': 'read', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # read a book
leisure47 = [{'LEMMA': 'read', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'ADJ'}, {'POS': 'NOUN'}]   # read a new book
leisure48 = [{'LEMMA': 'watch', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'PROPN'}]  # watching some Netflix
leisure49 = [{'LOWER': 'pc'}]  # PC, pc

activities_matcher.add('leisure', None, leisure1, leisure2, leisure3, leisure4, leisure5, leisure6, leisure7, leisure8,
                       leisure9, leisure10, leisure11, leisure12, leisure13, leisure14, leisure15, leisure16, leisure17,
                       leisure18, leisure19, leisure20, leisure21, leisure22, leisure23, leisure24, leisure25,
                       leisure26, leisure27, leisure28, leisure29, leisure30, leisure31, leisure32, leisure33,
                       leisure34, leisure35, leisure36, leisure37, leisure38, leisure39, leisure40, leisure41,
                       leisure42, leisure43, leisure44, leisure45, leisure46, leisure47, leisure48, leisure49)


# other
other1 = [{'LEMMA': 'chore', 'POS': 'NOUN'}]
other2 = [{'LEMMA': 'clean', 'POS': 'VERB'}]
other3 = [{'LEMMA': 'nurse', 'POS': 'VERB'}]
other4 = [{'LEMMA': 'wait', 'POS': 'VERB'}]

activities_matcher.add('other', None, other1, other2, other3, other4)

# prepare-food
prepare1 = [{'LEMMA': 'bake', 'POS': 'VERB'}]
prepare2 = [{'LEMMA': 'bake', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # bake a cake
prepare3 = [{'LEMMA': 'bake', 'POS': 'VERB'}, {'POS': {'IN': ['NOUN', 'PRON']}}]
prepare4 = [{'LEMMA': 'cook', 'POS': 'VERB'}]
prepare5 = [{'LEMMA': 'cook', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # cook a meal
prepare6 = [{'LEMMA': 'cook', 'POS': 'VERB'}, {'POS': {'IN': ['NOUN', 'PRON']}}]  # cook something, cook dinner
prepare7 = [{'LEMMA': 'make', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # make a meal
prepare8 = [{'LEMMA': 'make', 'POS': 'VERB'}, {'POS': 'NOUN'}]  # make dinner
prepare9 = [{'LEMMA': 'prepare', 'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}]  # prepare a meal
prepare10 = [{'LEMMA': 'prepare', 'POS': 'VERB'}, {'POS': {'IN': ['NOUN', 'PRON']}}]  # prepare something, prepare dinner
prepare11 = [{'LEMMA': 'soup', 'POS': 'NOUN'}]
prepare12 = [{'LEMMA': 'knead', 'POS': 'VERB'}]
prepare13 = [{'LOWER': 'foodprep'}]
prepare14 = [{'LOWER': 'food'}, {'LOWER': 'prep'}]
prepare15 = [{'LOWER': 'food'}, {'LOWER': 'preparation'}]
prepare16 = [{'LOWER': 'food'}, {'IS_PUNCT': True}, {'LOWER': 'prep'}]
prepare17 = [{'LOWER': 'food'}, {'IS_PUNCT': True}, {'LOWER': 'preparation'}]

activities_matcher.add('cooking', None, prepare1, prepare2, prepare3, prepare4, prepare5, prepare6, prepare7,
                       prepare8, prepare9, prepare10, prepare11, prepare12, prepare13, prepare14, prepare15, prepare16,
                       prepare17)

# relaxing
relaxing1 = [{'LEMMA': 'chill', 'POS': 'VERB'}]
relaxing2 = [{'LEMMA': 'relax', 'POS': 'VERB'}]

activities_matcher.add('relaxing', None, relaxing1, relaxing2)

# sleeping
sleeping1 = [{'LEMMA': 'nap', 'POS': 'VERB'}]
sleeping2 = [{'LEMMA': 'nap', 'POS': 'NOUN'}]
sleeping3 = [{'LEMMA': 'sleep', 'POS': 'VERB'}]
sleeping4 = [{'LEMMA': 'sleep', 'POS': 'NOUN'}]

activities_matcher.add('sleeping', None, sleeping1, sleeping2, sleeping3, sleeping4)

# smoking
smoking1 = [{'LEMMA': 'cigar', 'POS': 'NOUN'}]
smoking2 = [{'LEMMA': 'cigarette', 'POS': 'NOUN'}]
smoking3 = [{'LEMMA': 'joint', 'POS': 'NOUN'}]
# smoking4 = [{'LEMMA': 'pot', 'POS': 'NOUN'}]
smoking5 = [{'LEMMA': 'skunk', 'POS': 'NOUN'}]
smoking6 = [{'LEMMA': 'tobacco', 'POS': 'NOUN'}]
smoking7 = [{'LEMMA': 'weed', 'POS': 'NOUN'}]
smoking8 = [{'LEMMA': 'smoke', 'POS': 'VERB'}]
smoking9 = [{'LEMMA': 'smoking', 'POS': 'NOUN'}]

activities_matcher.add('smoking', None, smoking1, smoking2, smoking3, smoking5, smoking6, smoking7, smoking8,
                       smoking9)


# sport
sport1 = [{'LOWER': 'athletics', 'POS': 'NOUN'}]
sport2 = [{'LEMMA': 'basketball', 'POS': 'NOUN'}]
sport3 = [{'LEMMA': 'basket', 'POS': 'NOUN'}]
sport4 = [{'LEMMA': 'bike', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport5 = [{'LEMMA': 'bicycle', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport6 = [{'LEMMA': 'boat', 'POS': 'NOUN'}]
sport7 = [{'LEMMA': 'boulder', 'POS': 'VERB'}]
sport8 = [{'LEMMA': 'bouldering', 'POS': 'NOUN'}]
sport9 = [{'LEMMA': 'canoe',  'POS': {'IN': ['VERB', 'NOUN']}}]
sport10 = [{'LEMMA': 'canoeing', 'POS': 'NOUN'}]
sport11 = [{'LEMMA': 'climb', 'POS': 'VERB'}]
sport12 = [{'LEMMA': 'climbing', 'POS': 'NOUN'}]
sport13 = [{'LEMMA': 'cycle',  'POS': {'IN': ['VERB', 'NOUN']}}]
sport14 = [{'LEMMA': 'cycling', 'POS': 'NOUN'}]
sport15 = [{'LEMMA': 'exercise', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport16 = [{'LEMMA': 'football', 'POS': 'NOUN'}]
sport17 = [{'LEMMA': 'hike', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport18 = [{'LEMMA': 'hiking', 'POS': 'NOUN'}]
sport19 = [{'LEMMA': 'punt', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport20 = [{'LEMMA': 'punting', 'POS': 'NOUN'}]
sport21 = [{'LEMMA': 'row', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport22 = [{'LEMMA': 'rowing', 'POS': 'NOUN'}]
sport23 = [{'LEMMA': 'run', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport24 = [{'LEMMA': 'running', 'POS': 'NOUN'}]
sport25 = [{'LEMMA': 'skate', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport26 = [{'LEMMA': 'skating', 'POS': 'NOUN'}]
sport27 = [{'LEMMA': 'ski', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport28 = [{'LEMMA': 'skiing', 'POS': 'NOUN'}]
sport29 = [{'LEMMA': 'soccer', 'POS': 'NOUN'}]
sport30 = [{'LEMMA': 'swim', 'POS': 'NOUN'}]
sport31 = [{'LEMMA': 'swimming', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport32 = [{'LEMMA': 'trek', 'POS': 'NOUN'}]
sport33 = [{'LEMMA': 'trekking', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport34 = [{'LEMMA': 'volley', 'POS': 'NOUN'}]
sport35 = [{'LEMMA': 'volleyball', 'POS': 'NOUN'}]
sport36 = [{'LEMMA': 'walking', 'POS': 'NOUN'}]
sport37 = [{'LEMMA': 'walk', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport38 = [{'LEMMA': 'weight'}, {'IS_PUNCT': True}, {'LEMMA': 'lift'}]
sport39 = [{'LEMMA': 'weight'}, {'IS_PUNCT': True}, {'LOWER': 'lifting'}]
sport40 = [{'LEMMA': 'weightlift', 'POS': {'IN': ['VERB', 'NOUN']}}]
sport41 = [{'LOWER': 'weightlifting'}]

activities_matcher.add('sport', None, sport1, sport2, sport3, sport4, sport5, sport6, sport7, sport8, sport9, sport10,
                       sport11, sport12, sport13, sport14, sport15, sport16, sport17, sport18, sport19, sport20,
                       sport21, sport22, sport23, sport24, sport25, sport26, sport27, sport28, sport29, sport30,
                       sport31, sport32, sport33, sport34, sport35, sport36, sport37, sport38, sport39, sport40,
                       sport41)

# work-study
work_study1 = [{'LEMMA': 'essay', 'POS': 'NOUN'}]
work_study2 = [{'LEMMA': 'exam', 'POS': 'NOUN'}]
work_study3 = [{'LEMMA': 'homework', 'POS': 'NOUN'}]
work_study4 = [{'LEMMA': 'learn', 'POS': 'VERB'}]
work_study5 = [{'LEMMA': 'study', 'POS': 'VERB'}]
work_study6 = [{'LEMMA': 'work', 'POS': 'VERB'}]
work_study7 = [{'LEMMA': 'revise', 'POS': 'VERB'}]
work_study8 = [{'LEMMA': 'revision', 'POS': 'NOUN'}]

activities_matcher.add('workstudy', None, work_study1, work_study2, work_study3, work_study4, work_study5, work_study6,
                       work_study7, work_study8)


def match(sentence):
    matches = activities_matcher(sentence)
    return matches
