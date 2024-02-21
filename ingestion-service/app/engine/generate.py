import logging, os
import pymilvus
from dotenv import load_dotenv
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext
)
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.core.node_parser import SentenceWindowNodeParser

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

model = os.getenv("MODEL", "gpt-3.5-turbo")
llm=OpenAI(model=model)
embed_model=OpenAIEmbedding(model="text-embedding-ada-002")

def generate_datasource():

    try:
        milvus_uri = os.getenv("MILVUS_URI")
        milvus_api_key = os.getenv("MILVUS_API_KEY")
        milvus_collection = os.getenv("MILVUS_COLLECTION")
        milvus_dimension = int(os.getenv("MILVUS_DIMENSION"))

        if not all([milvus_uri, milvus_api_key, milvus_collection, milvus_dimension]):
            raise ValueError("Missing required environment variables.")

        # Create MilvusVectorStore 
        vector_store = MilvusVectorStore(
            uri=milvus_uri,
            token=milvus_api_key,
            collection_name=milvus_collection,
            dim=milvus_dimension, # mandatory for new collection creation
            overwrite=True,  
        )

        # Create StorageContext 
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # create the sentence window node parser
        node_parser = SentenceWindowNodeParser.from_defaults(
            window_size=3,
            window_metadata_key="window",
            original_text_metadata_key="original_text",
        )

        documents = SimpleDirectoryReader("data").load_data()
        nodes = node_parser.get_nodes_from_documents(documents)
        index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=embed_model)

    except (KeyError, ValueError) as e:
        raise ValueError(f"Invalid environment variables: {e}")
    except ConnectionError as e:
        raise ConnectionError(f"Failed to connect to Milvus: {e}")


if __name__ == "__main__":
    generate_datasource()
