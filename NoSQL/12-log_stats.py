#!/usr/bin/env python3
""" 12-log_stats.py """
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Select the database and collection
    collection = client.logs.nginx

    # 1. Count total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Count by method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Count status check (method=GET, path=/status)
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
