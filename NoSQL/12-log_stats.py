#!/usr/bin/env python3
""" Nginx logs stats from MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    
    # Get total number of documents
    total_logs = logs_collection.count_documents({})
    print("{} logs".format(total_logs))
    
    # Display methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    
    # Get status check (method=GET and path=/status)
    status_check = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
