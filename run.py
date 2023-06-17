import csv
import json
import os
import logging

from requests import Session
from requests.exceptions import HTTPError

elasticsearch_url = os.environ.get("ELASTICSEARCH_URL")
elasticsearch_username = os.environ.get("ELASTICSEARCH_USERNAME")
elasticsearch_password = os.environ.get("ELASTICSEARCH_PASSWORD")

s = Session()
s.auth = (elasticsearch_username, elasticsearch_password)
s.headers.update({"content-type": "application/json"})

index_name = os.environ.get("INDEX_NAME")
index_recreate = os.environ.get("INDEX_RECREATE", False)

number_of_shards = os.environ.get("NUMBER_OF_SHARDS", 1)
number_of_replicas = os.environ.get("NUMBER_OF_REPLICAS", 1)

logging.basicConfig(level=logging.INFO)


def csv_to_json(csv_file_path: str) -> str:
    """
    read a csv file and convert it to json string
    """

    data = []

    # read csv file
    with open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # convert each csv row into python dict
        for row in csv_reader:
            data.append(row)

    return json.dumps(data)


def index_exists() -> bool:
    """
    check if an elasticsearch index exists
    """

    url = f"{elasticsearch_url}/{index_name}"
    try:
        logging.info(f"Trying to check index '{index_name}' existence...")

        r = s.head(url)
        r.raise_for_status()
        return True
    except HTTPError as e:
        logging.error(f"Error in checking index '{index_name} existence': {str(e)}")
        return False


def delete_index():
    """
    delete an elasticsearch index
    """

    url = f"{elasticsearch_url}/{index_name}"
    try:
        logging.info(f"Trying to delete index '{index_name}'...")

        r = s.delete(url)
        r.raise_for_status()

        logging.info(f"Deleting index '{index_name}' done successfully!")
    except HTTPError as e:
        logging.error(f"Error in deleting index '{index_name}': {str(e)}")


def create_index():
    """
    create an elasticsearch index
    """

    schema = {
        "settings": {
            "number_of_shards": number_of_shards,
            "number_of_replicas": number_of_replicas,
        }
    }

    url = f"{elasticsearch_url}/{index_name}"
    try:
        logging.info(f"Trying to create index '{index_name}'...")

        r = s.put(url, data=json.dumps(schema))
        r.raise_for_status()

        logging.info(f"Creating index '{index_name}' done successfully!")
    except HTTPError as e:
        logging.error(f"Error in creating index '{index_name}': {str(e)}")


if __name__ == "__main__":
    data = csv_to_json("comic_books.csv")

    # delete index if it exists
    if index_recreate and index_exists():
        delete_index()

    # create index if it doesn't exist
    if not index_exists():
        create_index()
