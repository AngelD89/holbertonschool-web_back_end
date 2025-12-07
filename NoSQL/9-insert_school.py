#!/usr/bin/env python3
""" Insert a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    
    Args:
        mongo_collection: pymongo collection object
        **kwargs: arbitrary keyword arguments to be inserted as a document
    
    Returns:
        The _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
