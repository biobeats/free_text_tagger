# -*- coding: utf-8  -*-
# !/usr/bin/python

__author__ = "thepandascientist"


# THIS CLASS IS NEVER USED
# class Topic:
#     """ Class containing the general topic to be monitored
#
#     Attributes:
#         name (string): the name of the main topic
#         gazetteers ([Gazetteer])
#     """
#
#     def __init__(self, name, gazetteers):
#         self.name = name
#         self.gazetteers = gazetteers


class Gazetteer:
    """ Class containing a gazetteer

    Attributes:
        name (string): the name of the gazetteer
        tags (list): list of tags for the specific gazetteer
    """

    def __init__(self, name, tags):
        self.name = name
        self.tags = tags