#!/usr/bin/env python3
""" 10-update_topics.py """

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all documents in a collection matching the given school name.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        name (str): The name of the school to update.
        topics (list of str): List of topics to set in the document.

    Returns:
        dict: Result of the update operation.
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return None

    result = mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
    return result
