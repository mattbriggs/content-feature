import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

# Set the URL of the HTML page containing the JSON-LD data
url = "https://learn.microsoft.com/en-us/licensing/vlsc-faqs-home-page"

# Send a GET request to the URL and extract the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the script tag containing the JSON-LD data
json_ld = soup.find("script", {"type": "application/ld+json"})

# Parse the JSON-LD data into a Python dictionary
json_ld_dict = json.loads(json_ld.string)

# Convert the JSON-LD data into a Pandas DataFrame
df = pd.json_normalize(json_ld_dict["mainEntity"])

# Save the DataFrame as a CSV file
df.to_csv("output.csv", index=False)