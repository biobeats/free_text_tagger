import re


def is_adjective(token):
    if token.pos_ == 'ADJ':
        return True
    else:
        return False


def is_noun(token):
    if token.pos_ == 'NOUN':
        return True
    else:
        return False


def is_verb(token):
    if token.pos_ == 'VERB':
        return True
    else:
        return False


def is_auxiliary_verb(token):
    if token.pos_ == 'AUX':
        return True
    else:
        return False


def is_pronoun(token):
    if token.pos_ == 'PRON':
        return True
    else:
        return False


def check_for_phrasal_verbs(sentence):
    for token in sentence:
        if token.pos_ == 'ADP' and token.dep_ == 'prt' and token.head.pos_ == 'VERB':
            start = token.head.i
            end = token.i + 1
            return sentence[start:end]


def check_for_compound_nouns(sentence):
    for token in sentence:
        if token.pos_ == 'NOUN' and token.dep_ == 'compound':
            start = token.i
            end = token.head.i + 1
            return sentence[start:end]


def find_verbal_head_index(token):
    if token.head.pos_ == 'VERB':
        return token.head.i
    else:
        if token.head != token.head.head:
            return find_verbal_head_index(token.head)
        else:
            return None


def find_verbal_head(token):
    if token.head.pos_ == 'VERB' or token.head.pos_ == 'AUX':
        # gives back the position of the verb in the sentence
        return token.head
    else:
        if token.head != token.head.head:
            return find_verbal_head(token.head)
        else:
            return None


def check_for_activity_expression(sentence):
    activities = []
    for token in sentence:
        if is_verb(token):
            for el in token.children:
                if el.dep_ == 'dobj' or el.dep_ == 'pobj':
                    start = token.i
                    end = el.i + 1
                    activities.append(sentence[start:end])
        # if is_noun(token) and token.dep_ == 'pobj':
        #     start = find_verbal_head_index(token)
        #     end = token.i + 1
        #     if sentence[start:end] not in activities:
        #         activities.append(sentence[start:end])
    return activities


def check_for_noun_activity(sentence):
    activities = []
    for token in sentence:
        if token.pos_ == 'NOUN' and token.dep_ == 'pobj':
            if token.head.head.pos_ == 'NOUN' and token.head.head.dep_ == 'prep':
                start = token.head.head.i
                end = token.i + 1
                activities.append(sentence[start:end])
    return activities


def match_alone_expression(sentence):
    for token in sentence:
        if token.dep_ == 'pobj' and token.pos_ == 'ADJ' and token.lemma_ == 'own' and token.head.lemma_ == 'on':
            for el in token.lefts:
                if el.norm_ == 'my':
                    start = token.head.i
                    end = token.i + 1
                    return sentence[start:end]
        elif token.dep_ == 'pobj' and token.pos_ == 'PRON' and token.norm_ == 'myself' and token.head.lemma_ == 'by':
            start = token.head.i
            end = token.i + 1
            return sentence[start:end]


def check_negation(token):
    negatives = ['nothing', 'nobody', 'no']
    # TODO collapse collapsable things
    # NEGATION WITH ADJECTIVES
    if is_adjective(token):
        # nothing to be/feel upset about
        if is_verb(token.head) or is_auxiliary_verb(token.head):
            if is_pronoun(token.head.head) and token.head.head.lemma_ in negatives:
                return True
        # I am not busy
        for child in token.head.children:
            if child.dep_ == 'neg':
                return True
        # Not too bad
        for child in token.children:
            if child.dep_ == 'neg':
                return True
        # Not that happy
        if token.head.pos_ == 'amod' or token.head.pos_ == 'advmod':
            if token.head.head and token.head.head.pos_ == 'neg':
                return True

    # NEGATION WITH VERBS
    if is_verb(token):
        # I have nothing stressing me
        if is_pronoun(token.head) and token.head.lemma_ in negatives:
            return True
        # I have nobody stressing me
        for child in token.children:
            if is_pronoun(child) and child.lemma_ in negatives:
                return True
        # I have no one stressing me
        if is_noun(token.head):
            for child in token.head.children:
                if child.lemma_ in negatives:
                    return True
        # I'm not working
        for child in token.children:
            if child.dep_ == 'neg':
                return True

    # NEGATION WITH NOUNS
    if is_noun(token):
        # find the head of the noun
        verb = find_verbal_head(token)
        if verb:
            for child in verb.children:
                if child.dep_ == 'neg':
                    return True
        # expression like "no stress"
        for child in token.children:
            if child.lemma_ == 'no':
                return True
        # ?
        if token.head.pos_ == 'amod' or token.head.pos_ == 'advmod':
            if token.head.head and token.head.head.pos_ == 'neg':
                return True


def check_feeling(token):
    if is_verb(token) and token.lemma_ == 'feel':
        return True


def substitute_dash(sentence):
    sentence = re.sub(r' - ', '. ', sentence)
    return sentence