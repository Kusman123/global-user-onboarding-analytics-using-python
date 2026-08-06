# ------------------------------------------------------------
# SECTION 1: Importing Libraries
# ------------------------------------------------------------

# 'requests' allows our Python script to talk to websites/APIs via HTTP.
# 'json' helps us format and save the data properly.
# 'os' allows us to interact with the operating system (create folders, check paths).
# 'datetime' gives us timestamps so we don't overwrite old data.
# ------------------------------------------------------------

import requests
import json
import os
from datetime import datetime

# ------------------------------------------------------------
# SECTION 2: Configuration (Constants)
# ------------------------------------------------------------

# The URL of the API we are hitting.
API_URL = "https://randomuser.me/api/"


# The API documentation says the max per request is 5000, so we use that.
RESULTS_COUNT = 5000

# The folder where we will store raw data.

RAW_DATA_DIR = "data/raw"


# ------------------------------------------------------------
# SECTION 3: The Fetch Function
# ------------------------------------------------------------

def fetch_users(count):
  """
  Fetches users data from the Random user APi.

  Args:
  count(int): Number of users to fetch

  Returns:
  dict: The json response from the API as a python dictionary.
  """
  print(f" Fetching {count} users from the API....")

  try:
    response = requests.get(API_URL,params={'results':count})

    # A status code of 200 means "OK" - the request was successful.
    if response.status_code ==200:
      print(" API call successful!")
      
      # .json() converts the raw response text into a Python dictionary.

      return response.json()

    else:
      # If the API is down or we have an auth error, we raise an exception.
      print(f" API returned status code: {response.status_code}")
      response.raise_for_status()

  except requests.exceptions.ConnectionError:
    print(" Connection Error: Please check your internet connection.")
    raise # Re-raises the error so the script stops.
  except requests.exceptions.Timeout:
    print(" Timeout Error: The API took too long to respond.")
    raise
  except Exception as e:
    print(f" An unexpected error occurred: {e}")
    raise

# ------------------------------------------------------------
# SECTION 4: The Save Function
# ------------------------------------------------------------
# To avoid overwriting every time, we dont just save it as "data.json"
# We add the current date/time so we have a history of when we fetched it.
# ------------------------------------------------------------

def save_raw_json(data):
  """
    Saves the raw JSON data to the data/raw/ folder with a timestamp.
    
    Args:
        data (dict): The JSON data to save.
  """
  # 1. Generating a timestamp string:
  timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

  # 2. Creating the filename.
  filename = f"raw_users_{timestamp}.json"

  # 3. Combine the folder path and filename
  filepath = os.path.join(RAW_DATA_DIR, filename)

  os.makedirs(RAW_DATA_DIR, exist_ok=True)

  # 4. Opening the file in 'write' mode ('w') and save the JSON.
  with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data,f,indent=2, ensure_ascii=False)

  print(f" Raw data successfully saved to: {filepath}")


# ------------------------------------------------------------
# SECTION 5: The Main Execution Block
# ------------------------------------------------------------
# This 'if __name__ == "__main__":' block is standard in Python.
# It means: "Only run this code if I execute this script directly 
# (i.e., 'python src/fetch_data.py'), NOT if I import it into another script."
# This allows us to reuse the functions later without triggering a fetch.
# ------------------------------------------------------------

if __name__ == "__main__":
  print("Starting Data Ingestion Pipeline...")

  # Step 1: Fetch the data
  raw_data = fetch_users(RESULTS_COUNT)

  # Step 2: Save the data
  save_raw_json(raw_data)

  print(" Phase 2 Complete! Raw data is ready for cleaning.")