# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "biavarone"


import spacy

from free_text_tagger_v2 import analyzer
from free_text_tagger_v2 import activities_matcher
from free_text_tagger_v2 import emotions_matcher
from free_text_tagger_v2 import interactions_matcher
from free_text_tagger_v2 import places_matcher
import sys


nlp = spacy.load('en_core_web_lg')


def match_emotions(sentence):
    matches = emotions_matcher.match(sentence)

    for match_id, start, end in matches:
        if analyzer.check_negation(sentence[start]):
            pass
        else:
            # match_id is a number associated to the matched category, i.e. 9391526999249888540 == 'sad'
            rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'sad'
            span = sentence[start: end]  # get the matched slice of the sentence
            return rule_id, span  # decide if you want to return match_id or rule_id


def match_activities(sentence):
    matches = activities_matcher.match(sentence)

    for match_id, start, end in matches:
        # match_id is a number associated to the matched category, i.e. 5133706519360878345 == 'leisure'
        if analyzer.check_negation(sentence[start]):
            pass
        else:
            rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'leisure'
            span = sentence[start: end]  # get the matched slice of the sentence
            return rule_id, span  # decide if you want to return match_id or rule_id


def match_places(sentence):
    matches = places_matcher.match(sentence)

    for match_id, start, end in matches:
        # match_id is a number associated to the matched category, i.e. 12006852138382633966 == 'home'
        rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'home'
        span = sentence[start: end]  # get the matched slice of the sentence
        return rule_id, span  # decide if you want to return match_id or rule_id


def match_interactions(sentence):

    matches = interactions_matcher.match(sentence)

    for match_id, start, end in matches:
        # match_id is a number associated to the matched category, i.e. 18292453351080475948 == 'family'
        rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'family'
        span = sentence[start: end]  # get the matched slice of the sentence
        return rule_id, span  # decide if you want to return match_id or rule_id


if __name__ == "__main__":

    # sentence = "Here goes the sentence to be analyzed"
    sentence = sys.argv[1]
    # analyze sentence
    sentence = analyzer.substitute_dash(sentence)  # substitute dash with full stop for better parsing
    sentence = nlp(sentence)
    responses = []
    # return tags
    for sent in sentence.sents:
        sent = sent.as_doc()
        res = {}
        int_id, int_span = None, None if match_interactions(sent) is None else match_interactions(sent)
        pl_id, pl_span =  None, None if match_places(sent) is None else match_places(sent)
        emo_id, emo_span = None, None if match_emotions(sent) is None else match_emotions(sent)
        act_id, act_span = None, None if match_activities(sent) is None else match_activities(sent) 
        res['int_id'] = int_id        
        res['int_span'] = int_span        
        res['pl_id'] = pl_id        
        res['pl_span'] = pl_span        
        res['emo_id'] = emo_id        
        res['emo_span'] = emo_span        
        res['act_id'] = act_id        
        res['act_span'] = act_span
        responses.append(res)
    
    print(responses)

