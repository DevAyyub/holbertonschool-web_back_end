#!/usr/bin/env python3
""" 102-log_stats.py """
from pymongo import MongoClient


def log_stats():
    """
    Provides stats about Nginx logs stored in MongoDB, including top 10 IPs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # 1. Total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Status check
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    # 4. Top 10 IPs
    print("IPs:")
    top_ips = collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ])

    for ip_data in top_ips:
        ip = ip_data.get("_id")
        count = ip_data.get("count")
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    log_stats()
