#!/usr/bin/env python3
""" 8-all.py """

def list_all(mongo_collection):
    """
    Returns all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.

    Returns:
        list: List of documents in the collection, empty list if none.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
