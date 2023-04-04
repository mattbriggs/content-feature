# Python program to grab JSON-LD data from a URL and save as a CSV

This is a Python program that uses the requests and pandas libraries to grab JSON-LD data from a URL and save it as a CSV file.

## Explanation of the program

In this program, we first set the URL variable to the URL containing the JSON-LD data we want to extract. We then send a GET request to the URL using the requests library and extract the JSON-LD data from the response using the `json()` method.

Next, we convert the JSON-LD data into a Pandas DataFrame using the `json_normalize()` function, which converts nested JSON data into a flat table structure. We then save the DataFrame as a CSV file using the `to_csv()` method, specifying the output filename as output.csv and setting `index=False` to exclude the DataFrame index from the CSV file.

Note that this program assumes that the JSON-LD data is structured as a list of dictionaries, with each dictionary representing a single item. If the JSON-LD data is structured differently, you may need to adjust the `json_normalize()` function or use a different method to extract the data.

## Set up

```python
pip install -r requirements.txt
```
