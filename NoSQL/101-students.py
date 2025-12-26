#!/usr/bin/env python3
""" 101-students.py """


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    """
    return list(mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "topics": "$topics",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]))
