import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def get_json_ld(url):
    ''' This function takes a URL as input and returns a Python dictionary
    containing the JSON-LD data.'''
    
    # Send a GET request to the URL and extract the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the script tag containing the JSON-LD data
    json_ld = soup.find("script", {"type": "application/ld+json"})

    # Parse the JSON-LD data into a Python dictionary
    json_ld_dict = json.loads(json_ld.string)

    return json_ld_dict

def compile(indict, urlfilepath, list):
    ''' This function takes a Python dictionary containing the JSON-LD data and
    returns a list of lists containing the question and answer.'''

    for i in indict["mainEntity"]:
        list.append([i["name"].strip(), i["acceptedAnswer"]["text"].strip(), urlfilepath])
    return list

def get_all_json_ld(urlfilepath, outputpath):
    ''' This function takes a file containing a list of URLs and returns a CSV.'''
    urls = []
    with open(urlfilepath, "r") as f:
        for line in f:
            urls.append(line.strip())
    size = len(urls)
    outlist = [["Question", "Answer", "URL"]]
    for inx, i in enumerate (urls):
        print("Record: {} of {}".format(inx, size))
        try:
            jsonld = get_json_ld(i)
            outlist = compile(jsonld, i, outlist)
        except Exception as e:
            print(e)
            continue
    df = pd.DataFrame(outlist)
    df.to_csv(outputpath, index=False, header=False)

def main():
    urlfilepath = input("Enter the path to the file containing the URLs: ")
    outputpath = input("Enter the path to the output file: ")
    get_all_json_ld(urlfilepath, outputpath)

if __name__ == "__main__":
    main()