import requests
from bs4 import BeautifulSoup
import pandas as pd
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

outlist = [["Question", "Answer"]]
for i in json_ld_dict["mainEntity"]:
    outlist.append([i["name"], i["acceptedAnswer"]["text"]])

df = pd.DataFrame(outlist)
df.to_csv('output.csv', index=False, header=False)