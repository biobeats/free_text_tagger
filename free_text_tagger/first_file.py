# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "thepandascientist"

import json
import spacy

from free_text_tagger import gazetteers
from free_text_tagger import analyzer
nlp = spacy.load('en_core_web_lg')


def match_emotions(sentence, emotions):
    results = {}
    # TODO this should be done better
    for type_of_emotion in emotions:
        results[type_of_emotion.name] = []

    # match nouns, adjectives and verbs with emotions
    for token in sentence:
        # with something like "feel good" I want to match the whole expression
        if analyzer.check_feeling(token) and not analyzer.check_negation(token):
            for child in token.children:
                for type_of_emotion in emotions:
                    for tag in type_of_emotion.tags:
                        if (tag == child.norm_ or tag == child.lemma_ or tag == child.text) and token.dep_ != 'amod':
                            start = token.i
                            end = child.i + 1
                            resulting_tag = type_of_emotion.name
                            to_highlight = sentence[start:end]
                            results[resulting_tag].append(to_highlight)

        if analyzer.is_adjective(token) or analyzer.is_verb(token) or analyzer.is_noun(token):
            if analyzer.check_negation(token):  # do nothing if there is a negation before
                pass
            else:
                for type_of_emotion in emotions:
                    for tag in type_of_emotion.tags:
                        if tag == token.lemma_:
                            resulting_tag = type_of_emotion.name
                            to_highlight = token
                            results[resulting_tag].append(to_highlight)

    return results


def match_activities(sentence, activities):
    results = {}
    # TODO this should be done better
    for type_of_activity in activities:
        results[type_of_activity.name] = []

    # match phrasal verbs and highlight its span
    verb = analyzer.check_for_phrasal_verbs(sentence)
    if verb:
        verb = verb.as_doc()
        for type_of_activity in activities:
            for tag in type_of_activity.tags:
                for token in verb:
                    if tag == token.lemma_ or tag == token.norm_ or tag == token.text:
                        resulting_tag = type_of_activity.name
                        to_highlight = verb
                        results[resulting_tag].append(to_highlight)

    activities_expressions = analyzer.check_for_activity_expression(sentence)
    for activity_expression in activities_expressions:
        if activity_expression:
            activity_expression = activity_expression.as_doc()
            for type_of_activity in activities:
                for tag in type_of_activity.tags:
                    for token in activity_expression:
                        if tag == token.lemma_ or tag == token.norm_ or tag == token.text:
                            resulting_tag = type_of_activity.name
                            to_highlight = activity_expression
                            results[resulting_tag].append(to_highlight)

    noun_activities = analyzer.check_for_noun_activity(sentence)
    for noun_activity in noun_activities:
        if noun_activity:
            noun_activity = noun_activity.as_doc()
            for type_of_activity in activities:
                for tag in type_of_activity.tags:
                    for token in noun_activity:
                        if tag == token.lemma_ or tag == token.norm_ or tag == token.text:
                            resulting_tag = type_of_activity.name
                            to_highlight = noun_activity
                            results[resulting_tag].append(to_highlight)

    # match single verb with activity
    for token in sentence:
        if analyzer.is_verb(token):
            for type_of_activity in activities:
                for tag in type_of_activity.tags:
                    if tag == token.norm_ or tag == token.lemma_:
                        resulting_tag = type_of_activity.name
                        to_highlight = token
                        results[resulting_tag].append(to_highlight)

    return results


def match_places(sentence, places):
    results = {}
    # TODO this should be done better
    for type_of_place in places:
        results[type_of_place.name] = []

    # match compounds with places
    # TODO negations not handled with compounds
    compound = analyzer.check_for_compound_nouns(sentence)
    if compound:
        compound = compound.as_doc()
        to_match = []
        for noun in compound:
            to_match.append(str(noun.lemma_))
        for type_of_place in places:
            for tag in type_of_place.tags:
                if tag in to_match:
                    resulting_tag = type_of_place.name
                    to_highlight = compound
                    results[resulting_tag].append(to_highlight)

    # match nouns with places
    for token in sentence:
        if analyzer.is_noun(token) or analyzer:
            # TODO check this (negation) actually works fine
            # do not accept expressions like "I'm not at home"
            if analyzer.check_negation(token):
                pass
            else:
                for type_of_place in places:
                    for tag in type_of_place.tags:
                        if tag == token.norm_ and tag == token.lemma_:
                            resulting_tag = type_of_place.name
                            to_highlight = token
                            results[resulting_tag].append(to_highlight)
        else:
            # TODO check this
            # match mis-parsed elements (not classified as objects/nouns)
            for type_of_place in places:
                for tag in type_of_place.tags:
                    if tag == token.norm_ and tag == token.lemma_:
                        resulting_tag = type_of_place.name
                        to_highlight = token
                        results[resulting_tag].append(to_highlight)

    return results


def match_interactions(sentence, interactions):
    results = {}
    # TODO this should be done better
    color_patterns = [nlp(text) for text in ('red', 'green', 'yellow')]

    for type_of_interaction in interactions:
        results[type_of_interaction.name] = []

    # handle on my own and by myself
    alone = analyzer.match_alone_expression(sentence)
    if alone:
        resulting_tag = 'alone'
        to_highlight = alone
        results[resulting_tag].append(to_highlight)

    # match compounds with interactions
    compound = analyzer.check_for_compound_nouns(sentence)
    if compound:
        compound = compound.as_doc()
        to_match = []
        for noun in compound:
            to_match.append(str(noun.lemma_))
        for type_of_interaction in interactions:
            for tag in type_of_interaction.tags:
                if tag in to_match:
                    resulting_tag = type_of_interaction.name
                    to_highlight = compound
                    results[resulting_tag].append(to_highlight)

    # match nouns (or adjectives -for alone) with interactions
    for token in sentence:
        if analyzer.is_noun(token):
            for type_of_interaction in interactions:
                for tag in type_of_interaction.tags:
                    if tag == token.norm_ or tag == token.lemma_:
                        resulting_tag = type_of_interaction.name
                        to_highlight = token
                        results[resulting_tag].append(to_highlight)
        elif analyzer.is_adjective(token):
            for type_of_interaction in interactions:
                for tag in type_of_interaction.tags:
                    if tag == token.norm_ or tag == token.lemma_:
                        resulting_tag = type_of_interaction.name
                        to_highlight = token
                        results[resulting_tag].append(to_highlight)
        else:
            # match mis-parsed elements
            for type_of_interaction in interactions:
                for tag in type_of_interaction.tags:
                    if tag == token.norm_ or tag == token.lemma_:
                        resulting_tag = type_of_interaction.name
                        to_highlight = token
                        results[resulting_tag].append(to_highlight)

    return results


def read_sentences(dataset):
    # Reads input data and return a list of sentences
    sentences_list = []
    for el in dataset['documents']:
        sentences_list.append(el['text'])
    return sentences_list


if __name__ == "__main__":
    with open('/home/benedetta/PycharmProjects/BioBeats/topic_free_text/baseline2.json', 'r') as baseline_data:
        baseline_data = baseline_data.read()
        baseline_data = json.loads(baseline_data)
        sentences = read_sentences(baseline_data)

        # Dictionary where {keys: broad category name,
        # value: list of Gazetteers objects (name=category name, tags=tags to match}
        topics = gazetteers.build_topics_dict()

        for sentence in sentences:
            print(sentence)
            sentence = analyzer.substitute_dash(sentence)
            sentence = nlp(sentence)
            for sent in sentence.sents:
                sent = sent.as_doc()
                print(sent)
                interactions = match_interactions(sent, topics['interactions'])
                places = match_places(sent, topics['places'])
                emotions = match_emotions(sent, topics['emotions'])
                activities = match_activities(sent, topics['activities'])

                print('ACTIVITIES')
                for key, value in activities.items():
                    if value:
                        print(key, value)

                print('INTERACTIONS')
                for key, value in interactions.items():
                    if value:
                        print(key, value)

                print('PLACES')
                for key, value in places.items():
                    if value:
                        print(key, value)

                print('EMOTIONS')
                for key, value in emotions.items():
                    if value:
                        print(key, value)
                print()

    # sentence = "I'm not at home yet"
    # topics = gazetteers.build_topics_dict()
    #
    # sentence = nlp(sentence)
    # print(sentence)
    # for sent in sentence.sents:
    #     sent = sent.as_doc()
    #     print(sent)
    #     interactions = match_interactions(sent, topics['interactions'])
    #     places = match_places(sent, topics['places'])
    #     emotions = match_emotions(sent, topics['emotions'])
    #     activities = match_activities(sent, topics['activities'])
    #     print('ACTIVITIES')
    #     for key, value in activities.items():
    #         if value:
    #             print(key, value)
    #     print('INTERACTIONS')
    #     for key, value in interactions.items():
    #         if value:
    #             print(key, value)
    #     print('PLACES')
    #     for key, value in places.items():
    #         if value:
    #             print(key, value)
    #     print('EMOTIONS')
    #     for key, value in emotions.items():
    #         if value:
    #             print(key, value)
    #     print()
