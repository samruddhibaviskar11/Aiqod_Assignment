import csv

def query_mongodb(collection, query):
    """
    Execute a MongoDB query and return the results.

    Args:
        collection: The MongoDB collection to query.
        query (dict): The MongoDB query to execute.

    Returns:
        list: List of documents matching the query.
    """
    try:
        results = list(collection.find(query))
        if results:
            print(f"Found {len(results)} matching documents.")
        else:
            print("No matching documents found.")
        return results
    except Exception as e:
        print(f"Error executing MongoDB query: {e}")
        return []

def save_results_to_csv(results, output_file):
    """
    Save MongoDB query results to a CSV file.

    Args:
        results (list): List of documents (results) from MongoDB.
        output_file (str): Path to the output CSV file.
    """
    if not results:
        print("No data available to save.")
        return
    
    # Extract the keys (fields) for the CSV header
    keys = results[0].keys()
    
    # Write the results to the CSV file
    try:
        with open(output_file, 'w', newline='') as csvfile:
            dict_writer = csv.DictWriter(csvfile, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(results)
        print(f"Results successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving results to CSV: {e}")
