# NoSQL (MongoDB + Python)

This directory contains practical NoSQL exercises built around MongoDB operations using two approaches:

- MongoDB shell scripts for core CRUD/database commands.
- Python helper modules (with PyMongo) for reusable collection operations and analytics.

The project is designed to build confidence with document-based data modeling, filtering, updates, and basic log statistics.

## Learning Objectives

By completing these tasks, you practice how to:

- List and select MongoDB databases.
- Insert, query, count, update, and delete documents in a collection.
- Build Python helper functions that wrap collection operations.
- Query documents by array membership (topics).
- Generate simple operational metrics from a logs collection.

## Project Structure

### Mongo Shell Scripts

- `0-list_databases`: lists all available databases (`show dbs`).
- `1-use_or_create_database`: switches to (or creates) `my_db`.
- `2-insert`: inserts `{ name: "Holberton school" }` into `school` collection.
- `3-all`: lists all documents in `school` collection.
- `4-match`: lists documents where `name` is `Holberton school`.
- `5-count`: counts documents in `school` collection.
- `6-update`: updates matching schools with `address: "972 Mission street"`.
- `7-delete`: deletes documents where `name` is `Holberton school`.

### Python Modules (PyMongo)

- `8-all.py`: returns all documents from a collection.
- `9-insert_school.py`: inserts a school document using keyword arguments.
- `10-update_topics.py`: updates `topics` for schools matching a given name.
- `11-schools_by_topic.py`: returns schools that contain a specific topic.
- `12-log_stats.py`: prints analytics for `logs.nginx` (total logs, methods count, and `GET /status`).

## Requirements

- MongoDB server running locally (default: `mongodb://127.0.0.1:27017`)
- Python 3.8+
- `pymongo`

## Setup

Install Python dependency:

```bash
pip install pymongo
```

## How To Run

### Run Mongo Shell Scripts

From this directory:

```bash
cat 0-list_databases | mongo
cat 1-use_or_create_database | mongo
cat 2-insert | mongo my_db
cat 3-all | mongo my_db
cat 4-match | mongo my_db
cat 5-count | mongo my_db
cat 6-update | mongo my_db
cat 7-delete | mongo my_db
```

### Run Python Scripts

```bash
python3 12-log_stats.py
```

For `8` to `11`, import functions in your own test script or Python shell and pass a valid PyMongo collection.

## Notes

- The shell scripts are intentionally minimal to focus on MongoDB command syntax.
- Python helpers in `8` to `11` are reusable and can be integrated into larger applications.
- `12-log_stats.py` assumes the database `logs` and collection `nginx` already contain documents.

## Author

Holberton School - Web Back End track exercises.
