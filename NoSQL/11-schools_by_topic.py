#!/usr/bin/env python3
""" 11-schools_by_topic.py """

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        topic (str): The topic to search for.

    Returns:
        list: List of school documents containing the topic.
    """
    if mongo_collection is None or not topic:
        return []

    return list(mongo_collection.find({ "topics": topic }))
