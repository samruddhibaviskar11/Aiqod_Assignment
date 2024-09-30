from load_data import load_csv_to_mongodb
from data_retrieval import query_mongodb, save_results_to_csv
from pymongo import MongoClient
from query_generation import setup_llm, generate_query_llm, generate_query_from_input
# Script execution starts here
print("main.py is being executed.")

# Step 1: Load CSV data into MongoDB
csv_file = input("Enter the path to your CSV file (e.g., 'sample_data.csv'): ")
db_name = "product_db_12"
collection_name = "products_1_2"

load_csv_to_mongodb(csv_file, db_name,collection_name)

# Step 2: Set up LLM
llm_pipeline = setup_llm(model_name="EleutherAI/gpt-neo-1.3B")
while(True):
    # Step 3: Get user input for query generation
    user_input = input("Enter your query condition (for exit enter exit) (e.g., 'Find products with price greater than 50'): ")
    #print("for exit enter exit")
    if user_input.lower() == "exit":
        print("Exiting the program.")
        break

    # Step 4: Generate queries
    rule_based_query = generate_query_from_input(user_input)
    print(f"Rule-based generated query: {rule_based_query}")

    # Step 5: Generate LLM query
    llm_generated_query = generate_query_llm(llm_pipeline, user_input)

    # Combine both queries
    final_query = llm_generated_query or rule_based_query

    # Step 6: Execute the generated MongoDB query
    if final_query == {}:
        print("No valid query generated.")
    else:
        try:
            print(f"Executing Query: {final_query}")
            client = MongoClient('localhost', 27017)  # MongoDB connection
            db = client[db_name]
            collection = db[collection_name]

            results = query_mongodb(collection, final_query)

            if results:
                print("Query Results:", results)
                save_option = input("Do you want to save the results to a CSV? (yes/no): ").strip().lower()
                if save_option == "yes":
                    output_file = input("Enter the output CSV file name: ")
                    save_results_to_csv(results, output_file)
                    print(f"Results saved to {output_file}")
            else:
                print("No results found for the generated query.")
        except Exception as e:
            print(f"Error executing query: {e}")






























































