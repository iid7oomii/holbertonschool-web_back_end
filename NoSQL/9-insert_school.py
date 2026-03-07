#!/usr/bin/env python3
""" 9-insert_school.py """

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        **kwargs: Key-value pairs to be inserted as document fields.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    if mongo_collection is None or not kwargs:
        return None

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
