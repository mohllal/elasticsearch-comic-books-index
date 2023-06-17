.PHONY: docker-build
docker-build:
	docker build -t mohllal/elasticsearch-comic-books-index .

.PHONY: docker-run
docker-run:
	docker run --rm --network host \
		--env ELASTICSEARCH_URL=http://localhost:9200 \
		--env ELASTICSEARCH_USERNAME='' \
		--env ELASTICSEARCH_PASSWORD='' \
		--env INDEX_NAME='comic-books' \
		--env INDEX_RECREATE='True' \
		--name elasticsearch-comic-books-index \
		mohllal/elasticsearch-comic-books-index
