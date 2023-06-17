# Elasticsearch Sample Index: Comic Books

This script aims to create an Elasticsearch index for comic books using a CSV file containing the necessary data. The index will allow for demoing search and retrieval of comic book information based on various criteria.

## Usage

1. Build the Docker image:

```shell
make docker-build
```

2. Run the Docker container to index the comic books in Elasticsearch:

```shell
make docker-run
```

## Configuration

The following environment variables can be configured in the docker-run command:

- `ELASTICSEARCH_URL`: The URL of the Elasticsearch instance.
- `ELASTICSEARCH_USERNAME`: The username for Elasticsearch authentication. Default: empty.
- `ELASTICSEARCH_PASSWORD`: The password for Elasticsearch authentication. Default: empty.
- `NUMBER_OF_SHARDS`: The number of shards for index. Default: 1.
- `NUMBER_OF_REPLICAS`: The number of replicas for index. Default: 1.
- `INDEX_NAME`: The name of the Elasticsearch index to be created.
- `INDEX_RECREATE`: Whether to recreate the index if it already exists. Set to True to recreate the index; otherwise, set to False. Default: False.

## Sample Data

Here is an example of the CSV data format:

```csv
Title,Writer,Main Character,Publisher,Release Date,Description
The Dark Knight Returns,Frank Miller,Batman,DC Comics,1986-02-01,In a dystopian future; an aging Bruce Wayne dons the cape and cowl once again to save Gotham City from a new wave of crime. Frank Miller's gritty and dark portrayal of Batman revolutionized the character and became a defining moment in comic book history.
```
