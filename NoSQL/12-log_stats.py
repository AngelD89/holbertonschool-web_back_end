#!/usr/bin/env python3
""" Nginx logs stats from MongoDB """
from pymongo import MongoClient


def main():
    """
    Displays stats about Nginx logs in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    
    # Get total number of documents
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Display methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Get status check (method=GET and path=/status)
    status_check = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    main()
