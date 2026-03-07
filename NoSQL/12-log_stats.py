#!/usr/bin/env python3
""" 12-log_stats.py
Display some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def main():
    """Connect to MongoDB and display Nginx log stats."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # Total number of logs
    total_logs = nginx.count_documents({})
    print("{} logs".format(total_logs))

    # Count for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Count of GET /status
    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))


if __name__ == "__main__":
    main()
