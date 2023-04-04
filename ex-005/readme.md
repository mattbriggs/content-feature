# Python program to grab JSON-LD data from a URL and save as a CSV

This Python code extracts JSON-LD data from an HTML page, converts it into a Pandas DataFrame, and saves it as a CSV file.

## Explanation of the program

The requests library is used to send a GET request to the specified URL, and the HTML content of the response is extracted using the text attribute of the response object. This HTML content is stored in the html_content variable.

The BeautifulSoup library is used to parse the HTML content into a BeautifulSoup object called soup.

The `soup.find()` method is used to find the script tag containing the JSON-LD data, using the `{"type": "application/ld+json"}` attribute to filter the results to only those with the `application/ld+json` type. The JSON-LD data is stored in the `json_ld `variable.

The `json.loads()` function is used to parse the JSON-LD data from the `json_ld` variable into a Python dictionary called `json_ld_dict`.

The `pd.json_normalize()` function is used to convert the mainEntity object in the `json_ld_dict` dictionary into a Pandas DataFrame called `df`. The mainEntity object is assumed to contain an array of objects with the same properties.

Finally, the `df.to_csv() `method is used to save the DataFrame as a CSV file called o`utput.csv`. The `index=False `parameter is used to exclude the DataFrame index from the output file.

Note that the code assumes that the JSON-LD data is structured in a specific way, with the `mainEntity` object containing an array of objects with the same properties. If the JSON-LD data is structured differently, the `pd.json_normalize()` function may need to be modified to properly convert it into a Pandas DataFrame.

## Set up

```python
pip install -r requirements.txt
```
