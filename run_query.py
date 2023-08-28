import os
import sys

from google.cloud import bigquery

# Construct a BigQuery client object.

project = os.environ.get("PROJECT_ID")
folder = sys.argv[1]

client = bigquery.Client(project=project)

files = os.listdir(folder)

for file_name in files:
    with open(os.path.join(folder, file_name)) as f:
        query = f.read()
        query_job = client.query(query)  # Make an API request.

