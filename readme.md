Here’s a README file explaining the steps to set up the environment, install requirements, run the application, and a brief description of the project files and their structure.

---

# MongoDB Query Generation and CSV Loader Application

This application allows you to load data from a CSV file into a MongoDB database, generate MongoDB queries using both a rule-based approach and an LLM (Language Learning Model), and save the query results into a CSV file.

## Project Structure

```
├── main.py               # Entry point for running the application
├── query_generation.py   # Handles rule-based and LLM-based query generation
├── load_data.py          # Loads CSV data into MongoDB
├── data_retrieval.py     # Executes MongoDB queries and saves results to CSV
├── requirements.txt      # Required Python packages
```

### Description of Files:

- **`main.py`**: This is the main script that orchestrates the CSV loading, query generation (both rule-based and LLM-based), and querying MongoDB. It also handles saving the results to a CSV file.
  
- **`query_generation.py`**: This script includes functions to generate MongoDB queries based on user input using both a rule-based approach and an LLM (GPT-Neo-1.3B). It also maps user-friendly field names to MongoDB fields.
  
- **`load_data.py`**: This script handles loading data from a CSV file into a MongoDB collection.

- **`data_retrieval.py`**: This script contains functions to query the MongoDB collection and save the query results into a CSV file.

## Steps to Set Up and Run the Application

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/samruddhibaviskar11/Aiqod_Assignment
```

### 2. Create a Virtual Environment

Navigate to the project directory and create a virtual environment to isolate your project dependencies.

```bash
cd your-repo-folder
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install the Required Dependencies

Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Install MongoDB

Ensure that MongoDB is installed and running on your machine. If not, follow the official guide to install MongoDB: [MongoDB Installation Guide](https://docs.mongodb.com/manual/installation/).

Once MongoDB is installed and running, verify the MongoDB connection.

### 5. Run the Application

Now you can run the application using the `main.py` script. 

```bash
python main.py
```

You will be prompted to:

- Enter the path to your CSV file (e.g., `sample_data.csv`).
- Provide a MongoDB query condition (e.g., `Find products with price greater than 50`).
  
The application will load the CSV data into MongoDB, generate a query using both rule-based and LLM approaches, and execute the query on the MongoDB collection. If there are results, you will have the option to save them to a CSV file.

### Sample Query to Run:
- Example Query 1: `Find products with price greater than 50`
- Example Query 2: `List products with a rating of 4.5 or higher in the Electronics category`

---

### 6. Save Results to CSV

After executing the query, if you wish to save the results to a CSV file, the application will prompt you to enter the output CSV file name.

---

## Sample File Structure:

1. **CSV File Example** (`sample_data.csv`):
   ```
   ProductID,ProductName,Category,Price,Rating,ReviewCount,Stock,Discount,Brand,LaunchDate
   101,Wireless Mouse,Electronics,25.99,4.5,200,150,10%,Logitech,15-01-2022
   102,Gaming Keyboard,Electronics,75.49,4.7,350,85,5%,Corsair,20-11-2021
   ```

2. **Generated Queries**:
   - Rule-based: `{ 'Price': { '$gt': 50 } }`
   - LLM-generated: `{ 'Rating': { '$gte': 4.5 } }`

---

## Requirements

- Python 3.7 or higher
- MongoDB installed locally or using MongoDB Atlas
- Internet access for LLM model

---

### Notes

1. **LLM Model**: The LLM used for query generation is `EleutherAI/gpt-neo-1.3B`, which requires an internet connection to download and use.

2. **MongoDB Connection**: Ensure that MongoDB is running locally or that you have set up your MongoDB Atlas account and connected to it. You may need to modify the MongoDB connection string in the `main.py` script if your MongoDB is hosted remotely.

3. **Eval Caution**: The `eval()` function is used to convert string representations of the generated queries into Python dictionaries. Be cautious when using `eval()` in production environments and consider replacing it with a safer alternative if necessary.

---


