import pandas as pd
from pymongo import MongoClient

def load_csv_to_mongodb(csv_file, db_name, collection_name):
    """
    Load data from a CSV file into a MongoDB collection.

    Args:
        csv_file (str): Path to the CSV file.
        db_name (str): Name of the MongoDB database.
        collection_name (str): Name of the MongoDB collection.
    """
    print("Loading CSV data into MongoDB...")  # Debug statement
    # Read the CSV data into a DataFrame
    try:
        df = pd.read_csv(csv_file)
        print(f"Successfully read {len(df)} rows from {csv_file}.")
    except FileNotFoundError as e:
        print(f"Error: File '{csv_file}' not found. Make sure the path is correct.")
        return

    # Connect to MongoDB
    client = MongoClient('localhost', 27017)  # Adjust host and port if needed
    db = client[db_name]
    collection = db[collection_name]

    # Insert data into the MongoDB collection
    collection.insert_many(df.to_dict(orient='records'))
    print(f"Data loaded into MongoDB collection '{collection_name}'.")