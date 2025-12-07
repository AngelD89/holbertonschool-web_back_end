#!/usr/bin/env python3
""" Find schools by topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    
    Args:
        mongo_collection: pymongo collection object
        topic (string): the topic to search for
    
    Returns:
        A list of school docments that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
