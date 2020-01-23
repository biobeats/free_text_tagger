# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"

import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
emotions_matcher = Matcher(nlp.vocab)

# angry
angry1 = [{'LEMMA': 'aggressive', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry2 = [{'LEMMA': 'anger', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry3 = [{'LEMMA': 'angry', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry4 = [{'LEMMA': 'annoyed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry5 = [{'LEMMA': 'annoying', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry6 = [{'LEMMA': 'betrayed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry7 = [{'LEMMA': 'bitter', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry8 = [{'LEMMA': 'critical', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry9 = [{'LEMMA': 'dismissive', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry10 = [{'LEMMA': 'disrespected', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry11 = [{'LEMMA': 'distant', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry12 = [{'LEMMA': 'frustrated', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry13 = [{'LEMMA': 'fustration', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry14 = [{'LEMMA': 'furious', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry15 = [{'LEMMA': 'hostile', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry16 = [{'LEMMA': 'humiliated', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry17 = [{'LEMMA': 'indignant', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry18 = [{'LEMMA': 'infuriated', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry19 = [{'LEMMA': 'irritated', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry20 = [{'LEMMA': 'let', 'POS': 'VERB'}, {'LEMMA': 'down'}]
angry21 = [{'LEMMA': 'let', 'POS': 'VERB'}, {'LEMMA': 'me'}, {'LEMMA': 'down'}]
angry22 = [{'LEMMA': 'mad', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry23 = [{'LEMMA': 'numb', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry24 = [{'LEMMA': 'provoked', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry25 = [{'LEMMA': 'resentful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry26 = [{'LEMMA': 'ridiculed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry27 = [{'LEMMA': 'sceptical', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry28 = [{'LEMMA': 'upset', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry29 = [{'LEMMA': 'violated', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
angry30 = [{'LEMMA': 'withdrawn', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('angry', None, angry1, angry2, angry3, angry4, angry5, angry6, angry7, angry8, angry9, angry10,
                     angry11, angry12, angry13, angry14, angry15, angry16, angry17, angry18, angry19, angry20,
                     angry21, angry22, angry23, angry24, angry25, angry26, angry27, angry28, angry29, angry30)

# bad
bad1 = [{'LEMMA': 'apathetic', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad2 = [{'LEMMA': 'bad', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad3 = [{'LEMMA': 'bored', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad4 = [{'LEMMA': 'busy', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad5 = [{'LEMMA': 'drained', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad6 = [{'LEMMA': 'hopeless', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad7 = [{'LEMMA': 'indifferent', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad8 = [{'LEMMA': 'lost', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad9 = [{'LEMMA': 'overwhelm', 'POS': 'VERB'}]
bad10 = [{'LEMMA': 'overwhelmed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad11 = [{'LEMMA': 'pressured', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad12 = [{'LEMMA': 'rushed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad13 = [{'LEMMA': 'sleepy', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad14 = [{'LEMMA': 'stressed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad15 = [{'LEMMA': 'stress'}]
bad16 = [{'LEMMA': 'tired', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
bad17 = [{'LEMMA': 'unfocused', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('bad', None, bad1, bad2, bad3, bad4, bad5, bad6, bad7, bad8, bad9, bad10, bad11, bad12, bad13,
                     bad14, bad15, bad16, bad17)

# calm
calm1 = [{'LEMMA': 'calm', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
calm2 = [{'LEMMA': {'IN': ['chilled', 'chill']}, 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
calm3 = [{'LEMMA': 'neutral', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
calm4 = [{'LEMMA': 'relaxed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
calm5 = [{'LEMMA': 'rested', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
calm6 = [{'LEMMA': 'safe', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
calm7 = [{'LEMMA': 'secure', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
calm8 = [{'LEMMA': 'at'}, {'LEMMA': 'ease'}]

emotions_matcher.add('calm', None, calm1, calm2, calm3, calm4, calm5, calm6, calm7, calm8)

# disgusted
disgusted1 = [{'LEMMA': 'appalled', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted2 = [{'LEMMA': 'awful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted3 = [{'LEMMA': 'detestable', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted4 = [{'LEMMA': 'disappointed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted5 = [{'LEMMA': 'disapproving', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted6 = [{'LEMMA': 'embarassed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted7 = [{'LEMMA': 'hesitant', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted8 = [{'LEMMA': 'horrified', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted9 = [{'LEMMA': 'judgmental', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted10 = [{'LEMMA': 'nauseated', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted11 = [{'LEMMA': 'nauseous', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted12 = [{'LEMMA': 'repelled', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
disgusted13 = [{'LEMMA': 'revolted', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('disgusted', None, disgusted1, disgusted2, disgusted3, disgusted4, disgusted5, disgusted6,
                     disgusted7, disgusted8, disgusted9, disgusted10, disgusted11, disgusted12, disgusted13)

# fearful
fearful1 = [{'LEMMA': 'anxiety', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful2 = [{'LEMMA': 'anxious', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful3 = [{'LEMMA': 'concern', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful4 = [{'LEMMA': 'concerned', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful5 = [{'LEMMA': 'anxiety', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful6 = [{'LEMMA': 'excluded', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful7 = [{'LEMMA': 'exposed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful8 = [{'LEMMA': 'fearful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful9 = [{'LEMMA': 'frightened', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful10 = [{'LEMMA': 'helpless', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful11 = [{'LEMMA': 'inadequate', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful12 = [{'LEMMA': 'inferior', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful13 = [{'LEMMA': 'insecure', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful14 = [{'LEMMA': 'insignificant', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful15 = [{'LEMMA': 'nervous', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful16 = [{'LEMMA': 'overwhelmed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful17 = [{'LEMMA': 'persecuted', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful18 = [{'LEMMA': 'rejected', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful19 = [{'LEMMA': 'scared', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful20 = [{'LEMMA': 'threatened', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful21 = [{'LEMMA': 'weak', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful22 = [{'LEMMA': 'worried', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
fearful23 = [{'LEMMA': 'worry', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV', 'VERB']}}]
fearful24 = [{'LEMMA': 'worthless', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('fearful', None, fearful1, fearful2, fearful3, fearful4, fearful5, fearful6, fearful7, fearful8,
                     fearful9, fearful10, fearful11, fearful12, fearful13, fearful14, fearful15, fearful16, fearful17,
                     fearful18, fearful19, fearful20, fearful21, fearful22, fearful23, fearful24)

# good
good1 = [{'LEMMA': 'alright', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
good2 = [{'LOWER': 'good', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
good3 = [{'LEMMA': 'ok', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
good4 = [{'LEMMA': 'okay', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('good', None, good1, good2, good3, good4)

# happy
happy1 = [{'LEMMA': 'accepted', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy2 = [{'LEMMA': 'amused', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy3 = [{'LEMMA': 'aroused', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy4 = [{'LEMMA': 'charmed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy5 = [{'LEMMA': 'cheeky', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy6 = [{'LEMMA': 'confident', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy7 = [{'LEMMA': 'content', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy8 = [{'LEMMA': 'courageous', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy9 = [{'LEMMA': 'creative', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy10 = [{'LEMMA': 'curious', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy11 = [{'LEMMA': 'delighted', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy12 = [{'LEMMA': 'eager', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy13 = [{'LEMMA': 'empowered', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy14 = [{'LEMMA': 'energetic', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy15 = [{'LEMMA': 'enthusiastic', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy16 = [{'LEMMA': 'free', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy17 = [{'LEMMA': 'glad', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy18 = [{'LEMMA': 'grateful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy19 = [{'LEMMA': 'happy', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy20 = [{'LEMMA': 'hopeful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy21 = [{'LEMMA': 'inquisitive', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy22 = [{'LEMMA': 'inspired', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy23 = [{'LEMMA': 'interested', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy24 = [{'LEMMA': 'intimate', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy25 = [{'LEMMA': 'joyful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy26 = [{'LEMMA': 'loving', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy27 = [{'LEMMA': 'optimistic', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy28 = [{'LEMMA': 'overjoyed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy29 = [{'LEMMA': 'optimistic', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy30 = [{'LEMMA': 'peaceful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy31 = [{'LEMMA': 'pleased', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy32 = [{'LEMMA': 'powerful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy33 = [{'LEMMA': 'proud', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy34 = [{'LEMMA': 'respected', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy35 = [{'LEMMA': 'sensitive', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy36 = [{'LEMMA': 'successful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy37 = [{'LEMMA': 'thankful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy38 = [{'LEMMA': 'trusting', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
happy39 = [{'LEMMA': 'valued', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('happy', None, happy1, happy2, happy3, happy4, happy5, happy6, happy7, happy8, happy9, happy10,
                     happy11, happy12, happy13, happy14, happy15, happy16, happy17, happy18, happy19, happy20, happy21,
                     happy22, happy23, happy24, happy25, happy26, happy27, happy28, happy29, happy30, happy31, happy32,
                     happy33, happy34, happy35, happy36, happy37, happy38, happy39)

# sad
sad1 = [{'LEMMA': 'abandoned', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad2 = [{'LEMMA': 'ashamed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad3 = [{'LEMMA': 'depression', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad4 = [{'LEMMA': 'depressed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad5 = [{'LEMMA': 'despair', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad6 = [{'LEMMA': 'disappointed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad7 = [{'LEMMA': 'embarassed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad8 = [{'LEMMA': 'empty', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad9 = [{'LEMMA': 'fragile', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad10 = [{'LEMMA': 'grief', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad11 = [{'LEMMA': 'guilty', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad12 = [{'LEMMA': 'hurt', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad13 = [{'LEMMA': 'inferior', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad14 = [{'LEMMA': 'isolated', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad15 = [{'LEMMA': 'lonely', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad16 = [{'LEMMA': 'powerless', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad17 = [{'LEMMA': 'remorseful', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad18 = [{'LEMMA': 'sad', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad19 = [{'LEMMA': 'victimised', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
sad20 = [{'LEMMA': 'vulnerable', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('sad', None, sad1, sad2, sad3, sad4, sad5, sad6, sad7, sad8, sad8, sad10, sad11, sad12, sad13,
                     sad14, sad15, sad16, sad17, sad18, sad19, sad20)

# surprised
surprised1 = [{'LEMMA': 'amazed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised2 = [{'LEMMA': 'atonished', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised3 = [{'LEMMA': 'awe', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised4 = [{'LEMMA': 'confused', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised5 = [{'LEMMA': 'disillusioned', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised6 = [{'LEMMA': 'dismayed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised7 = [{'LEMMA': 'excited', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised8 = [{'LEMMA': 'perplexed', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised9 = [{'LEMMA': 'shocked', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised10 = [{'LEMMA': 'startled', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]
surprised11 = [{'LEMMA': 'surprised', 'POS': {'IN': ['NOUN', 'ADJ', 'ADV']}}]

emotions_matcher.add('surprised', None, surprised1, surprised2, surprised3, surprised4, surprised5, surprised6,
                     surprised7, surprised8, surprised9, surprised10, surprised11)


def match(sentence):
    matches = emotions_matcher(sentence)
    return matches

