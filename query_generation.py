import re
from transformers import pipeline

# Setup the LLM (GPT-Neo-1.3B)
def setup_llm(model_name="EleutherAI/gpt-neo-1.3B"):
    llm_pipeline = pipeline("text-generation", model=model_name)
    return llm_pipeline

# Generate query with LLM
def generate_query_llm(llm_pipeline, user_input):
    """
    Use LLM to generate a MongoDB query from the user input.
    """
    prompt = (
        f"Generate a valid MongoDB query in dictionary format based on the following condition:\n"
        f"{user_input}\n\n"
        "Return **only** the MongoDB query as a valid dictionary. The dictionary should be in the following formats:\n"
        "{ 'field_name': { '$operator': value } }\n"
        "{ '$and': [ { 'field_name1': { '$operator1': value1 } }, { 'field_name2': { '$operator2': value2 } } ] }\n"
        "Ensure the dictionary is properly formatted and uses single quotes around keys and values. No explanations, no extra text."
    )
    
    print(f"Prompt to LLM:\n{prompt}")
    
    # Generate the response
    result = llm_pipeline(prompt, max_new_tokens=100, do_sample=False, temperature=0.7)
    raw_query = result[0]['generated_text'].strip()
    
    # Debug: Print the raw output before cleaning
    print(f"Raw LLM Output: {raw_query}")
    
    # Attempt to extract valid dictionary using regex
    try:
        match = re.search(r'(\{(?:[^{}]|(?R))*\})', raw_query, re.DOTALL)
        if match:
            cleaned_query = match.group(0).replace('"', "'")  # Ensure single quotes
            print(f"Extracted Query: {cleaned_query}")
            return eval(cleaned_query)  # Convert string representation to dict
        else:
            print("No valid dictionary structure found in the response.")
    except Exception as e:
        print(f"Error decoding extracted query: {e}")
    
    return {}  # Fallback if no valid query is generated

# Rule-based query generation (simplified for common conditions)
def generate_query_from_input(user_input):
    query_conditions = []
    
    conditions = re.findall(r'(\w+) (greater than|below|equals) (\d+(\.\d+)?)', user_input, re.IGNORECASE)
    
    for condition in conditions:
        field_name, operator, value = condition[0], condition[1], condition[2]
        field_name_mapped = map_field(field_name)

        # Map operators to MongoDB
        if operator.lower() == "greater than":
            query_conditions.append(f"{{ '{field_name_mapped}': {{ '$gt': {value} }} }}")
        elif operator.lower() == "below":
            query_conditions.append(f"{{ '{field_name_mapped}': {{ '$lt': {value} }} }}")
        elif operator.lower() == "equals":
            query_conditions.append(f"{{ '{field_name_mapped}': {{ '$eq': {value} }} }}")
    
    # Combine multiple conditions using $and if needed
    if len(query_conditions) > 1:
        final_query = "{ '$and': [" + ", ".join(query_conditions) + "] }"
    else:
        final_query = query_conditions[0] if query_conditions else "{}"
    
    return eval(final_query)  # Convert string representation to dict

# Map user-friendly names to MongoDB fields
def map_field(field_name):
    field_map = {
        "price": "Price",
        "rating": "Rating",
        "review count": "ReviewCount",
        "category": "Category",
        "brand": "Brand",
        "launch date": "LaunchDate"
    }
    return field_map.get(field_name.lower(), field_name)
