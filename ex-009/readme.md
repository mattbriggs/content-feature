# Pattern Compliance from Bobby (7.10.23)

C:\Users\mabrigg\Microsoft\Content coverage workgroup - General\Content Patterns - Data\pattern-compliance-2023_7\MicrosoftDocsazuredocspr.csv

| Column name         | Example                                              |
|---------------------|------------------------------------------------------|
| PartitionKey        | CODE_OF_CONDUCT_md                                   |
| RowKey              | 02A3176534AD7096890265CA7C2EF2AA                     |
| Timestamp           | 2023-07-07T01:04:09.8484474Z                         |
| RepoUrl             | https://github.com/MicrosoftDocs/azure-docs-pr       |
| RepoUrl@type        | String                                               |
| RepoPath            | D:/ClonedRepos/MicrosoftDocs/azure-docs-pr           |
| RepoPath@type       | String                                               |
| Path                | CODE_OF_CONDUCT.md                                   |
| Path@type           | String                                               |
| AuditFileId         | .learnlinter/globalRules/articleBuildValidations.yml |
| AuditFileId@type    | String                                               |
| AuditRuleTitle      | Alt text should be unique within file                |
| AuditRuleTitle@type | String                                               |
| Sha                 | 48e9741d3504b50900f02eb4359050f705f8249d             |
| Sha@type            | String                                               |
| MSService           |                                                      |
| MSService@type      | String                                               |
| MSProduct           |                                                      |
| MSProduct@type      | String                                               |
| MSTitle             |                                                      |
| MSTitle@type        | String                                               |
| MSDescription       |                                                      |
| MSDescription@type  | String                                               |
| MSTopic             |                                                      |
| MSTopic@type        | String                                               |
| MSDevLang           |                                                      |
| MSDevLang@type      | String                                               |
| MSTechnology        |                                                      |
| MSTechnology@type   | String                                               |
| MSSubService        |                                                      |
| MSSubService@type   | String                                               |
| MSAuthor            |                                                      |
| MSAuthor@type       | String                                               |
| Author              |                                                      |
| Author@type         | String                                               |
| Success             | TRUE                                                 |
| Success@type        | Boolean                                              |

## Requirements.txt

```text
anyio==3.7.1
argon2-cffi==21.3.0
argon2-cffi-bindings==21.2.0
arrow==1.2.3
asttokens==2.2.1
attrs==23.1.0
backcall==0.2.0
beautifulsoup4==4.12.2
bleach==6.0.0
cffi==1.15.1
click==8.1.3
colorama==0.4.6
comm==0.1.3
contourpy==1.0.7
cycler==0.11.0
debugpy==1.6.7
decorator==5.1.1
defusedxml==0.7.1
exceptiongroup==1.1.2
executing==1.2.0
fastjsonschema==2.17.1
fonttools==4.39.4
fqdn==1.5.1
fuzzywuzzy==0.18.0
gensim==4.3.1
idna==3.4
importlib-metadata==6.8.0
importlib-resources==5.12.0
ipykernel==6.24.0
ipython==8.14.0
ipython-genutils==0.2.0
isoduration==20.11.0
jedi==0.18.2
Jinja2==3.1.2
joblib==1.2.0
jsonpointer==2.4
jsonschema==4.18.0
jsonschema-specifications==2023.6.1
jupyter-events==0.6.3
jupyter_client==8.3.0
jupyter_core==5.3.1
jupyter_server==2.7.0
jupyter_server_terminals==0.4.4
jupyterlab-pygments==0.2.2
kiwisolver==1.4.4
Levenshtein==0.21.0
MarkupSafe==2.1.3
matplotlib==3.7.1
matplotlib-inline==0.1.6
mistune==3.0.1
nbclassic==1.0.0
nbclient==0.8.0
nbconvert==7.6.0
nbformat==5.9.1
nest-asyncio==1.5.6
nltk==3.8.1
notebook==6.5.4
notebook_shim==0.2.3
numpy==1.24.3
overrides==7.3.1
packaging==23.1
pandas==2.0.1
pandocfilters==1.5.0
parso==0.8.3
pickleshare==0.7.5
Pillow==9.5.0
platformdirs==3.8.1
plotly==5.14.1
prometheus-client==0.17.1
prompt-toolkit==3.0.39
psutil==5.9.5
pure-eval==0.2.2
pycparser==2.21
Pygments==2.15.1
pyparsing==3.0.9
python-dateutil==2.8.2
python-json-logger==2.0.7
python-Levenshtein==0.21.0
pytz==2023.3
pywin32==306
pywinpty==2.0.10
PyYAML==6.0
pyzmq==25.1.0
rapidfuzz==3.0.0
referencing==0.29.1
regex==2023.5.5
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rpds-py==0.8.10
scikit-learn==1.2.2
scipy==1.10.1
Send2Trash==1.8.2
six==1.16.0
smart-open==6.3.0
sniffio==1.3.0
soupsieve==2.4.1
stack-data==0.6.2
tenacity==8.2.2
terminado==0.17.1
threadpoolctl==3.1.0
tinycss2==1.2.1
tornado==6.3.2
tqdm==4.65.0
traitlets==5.9.0
typing_extensions==4.7.1
tzdata==2023.3
uri-template==1.3.0
wcwidth==0.2.6
webcolors==1.13
webencodings==0.5.1
websocket-client==1.6.1
zipp==3.15.0

```

Sure, here is a simple Python script that can perform these actions.

First, make sure that you have the pandas library installed. If not, you can install it using pip:

```python
!pip install pandas
```

Then, use the following script to load a CSV file, group by 'Path', calculate the total for 'Success', and save the result:

```python
# Import necessary libraries
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('your_file.csv')

# Group by 'Path' and calculate the total for 'Success'
grouped_df = df.groupby('Path')['Success'].sum().reset_index()

# Save the result as a new CSV file
grouped_df.to_csv('grouped_data.csv', index=False)
```

In this script, replace `'your_file.csv'` with the path to your actual file. Also, the result will be saved to a file named `'grouped_data.csv'` in the same directory where the script is running. You can change this to any path where you want the result to be saved.

Please note that this script assumes that the 'Success' column contains numeric values because it's performing a sum operation. If your 'Success' column does not contain numeric values, you'll need to use a different aggregation function or convert the data to numeric values first. 

If the 'Success' column contains boolean values (True/False), which might be the case judging by the column name, you might want to convert the boolean to integer (True=1 and False=0) before summing. Here is how you could do it:

```python
df['Success'] = df['Success'].astype(int)
```