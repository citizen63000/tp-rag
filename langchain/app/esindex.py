from elasticsearch import Elasticsearch
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_elasticsearch.vectorstores import ElasticsearchStore
from langchain_core.documents import Document

# Clean ElasticSearch DB
Elasticsearch("http://rag-elasticsearch:9200").options(ignore_status=[400,404]).indices.delete(index='rag')

# Initialize Vector store connection (ElasticSearch) with Embeddings generator (HuggingFaceEmbeddings)
// @todo

# Create Data
documents = [
    {"title": "Inception",                      "author": "Christopher Nolan", "genre": "Sci-Fi", "release_year": 2010},
    {"title": "The Shawshank Redemption",       "author": "", "genre": "Drama", "release_year": 1994},
    {"title": "The Godfather",                  "author": "", "genre": "Crime", "release_year": 1972},
    {"title": "Pulp Fiction",                   "author": "", "genre": "Crime", "release_year": 1994},
    {"title": "Forrest Gump",                   "author": "", "genre": "Drama", "release_year": 1994},
    {"title": "Le quantique c'est fantastique", "author": "Philippe lacomme", "genre": "Science", "release_year": 2013},
    {"title": "Les joies du Big Data",          "author": "Lionel", "genre": "Science", "release_year": 2020}
]

# @todo Index movies here
// @todo