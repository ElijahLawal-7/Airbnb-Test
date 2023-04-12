#!/usr/bin/env python3
""" Defines schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """ Lists school having a specific topic """
    top = {"topics": {"$elemMatch": {"$eq": topic,},},}
    return [i for i in mongo_collection.find(top)]
