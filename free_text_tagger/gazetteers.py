# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "thepandascientist"

import os
import codecs
from free_text_tagger.topics import Gazetteer


def load_gazetteers(path):
    files = os.listdir(path)
    gazetteers_dict = {}

    for f in files:
        file_path = os.path.join(path + '/' + f)
        with codecs.open(file_path, 'r', 'utf-8') as gazetteer_file:
            tags = []
            for line in gazetteer_file:
                line = line.strip()
                tags.append(line)
            name = (f.split('.'))[0]
            gazetteers_dict[name] = tags
    return gazetteers_dict


def build_topics_dict():
    root_path = os.path.abspath('gazetteers')
    topics_dirs = os.listdir(root_path)
    topic_dict = {}  # dictionary to save topics and gazetteers

    # for each main topic (eg EMOTIONS), associate a list of gazetteers objects
    for t in topics_dirs:
        gazetteers_list = []  # list to save gazetteer objects

        topic_path = os.path.join(root_path + '/' + t)
        gazetteers = load_gazetteers(topic_path)

        for name, tags in gazetteers.items():
            gazetteer = Gazetteer(name, tags)
            gazetteers_list.append(gazetteer)

        topic_dict[t] = gazetteers_list

    return topic_dict


build_topics_dict()