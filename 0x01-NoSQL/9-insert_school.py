#!/usr/bin/env python3
""" Defines insert_school """



def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs"""
    mon = mongo_collection.insert_one(kwargs)
    return mon.inserted_id
