from langchain_elasticsearch.vectorstores import ElasticsearchStore
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from langchain_core.documents import Document

# Initialize Vector store connection (ElasticSearch) with Embeddings generator (HuggingFaceEmbeddings)
// @todo

# Connect to Ollama
// @todo

# Initialize prompt
system_prompt = (
    "Use the given context to answer the question. "
    "If you don't know the answer, say you don't know. "
    "Use three sentence maximum and keep the answer concise. "
    "Context: {context}"
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Define state for application
class State(TypedDict):
    input: str
    context: List[Document]
    answer: str

# Define application steps
def retrieve(state: State):
    // @todo

def generate(state: State):
    // @todo

# Create execution graph
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

# chat
// @todo