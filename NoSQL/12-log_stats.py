#!/usr/bin/env python3
"""
12-log_stats.py: Displays stats about Nginx logs stored in MongoDB.
Database: logs
Collection: nginx
"""

from pymongo import MongoClient

def main():
    """
    Connect to MongoDB, count logs, count by method, and count GET /status.
    """
    client = MongoClient()  # default connection localhost:27017
    db = client.logs
    collection = db.nginx

    # total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # count by HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # count GET /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()
