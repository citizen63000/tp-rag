# RAG

Ce TP consiste à créer un RAG avec Llama3, Langchain et ElasticSearch.
Llama tournera en local avec un serveur Ollama.

# Container Ollama

Se connecter au container:

```
./docker-connect-ollama.sh
```

Lancer Llama3.2 : 
```
ollama run llama3.2
```

# Container langchain (rag-langchain)
## Préparation de l'environnement

Se connecter au container langchain:

```
./docker-connect-langchain.sh
```
Initialiser l'environnement de développement:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Indexation des documents dans ElasticSearch
Complétez le fichier esindex.py avec le code approprié et lancez le fichier :
```
python3 esindex.py
```

## Chatbot
Complétez le code de main.py et lancez le chatbot :
```
python3 main.py
```