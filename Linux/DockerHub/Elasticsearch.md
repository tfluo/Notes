# Elasticsearch
## confirm the lastest version
* [Elasticsearch docker-hub](https://hub.docker.com/_/elasticsearch)
## pull docker
* docker pull elasticsearch:7.6.1
## docker-compose.yaml
* vi docker-compose.yaml
```yaml
version: '2.2'
services:
  elasticsearch:
    image: elasticsearch:7.6.1
    container_name: es7_ti
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - bootstrap.memory_lock=true
      - TAKE_FILE_OWNERSHIP=true
      - node.name=es7_ti
    volumes:
      - [$LOCAL_ES_DATA_PATH]:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    networks:
      - es7net

volumes:
  es7data:
    driver: local

networks:
  es7net:
    driver: bridge
```
