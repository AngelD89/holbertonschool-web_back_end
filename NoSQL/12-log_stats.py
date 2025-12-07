#!/usr/bin/env python3
"""Query MongoDB collection nginx in the logs DB and display stats."""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total logs
    total = collection.count_documents({})
    print(f"{total} logs")

    # Methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        count = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {count}"}
