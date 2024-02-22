# The Journey of RAG Development: From Notebook to Microservices

On a quest for enterprise production RAG, we explore how we craft RAG microservices from an RAG pipeline POC developed in a Colab notebook. Specifically, we touch on the topics of:
- `create-llama` command line tool, which bootstraps new microservices development.
- From a Colab notebook `sentence_window_node_parser_rag.ipynb`, we craft two microservices, `ingestion-service`, and `inference-service`, to cover the two main stages of RAG.
- GPU-accelerated Milvus vector database integration into our new microservices.
- Adding NeMo Guardrails to `inference-service` to add guardrails for user inputs, LLM outputs, topical moderation, and custom actions to integrate with LlamaIndex.
- more to come.

Refer to my blog [The Journey of RAG Development: From Notebook to Microservices](https://medium.com/towards-data-science/the-journey-of-rag-development-from-notebook-to-microservices-cc065d0210ef?sk=6644d8faadc5f9ef558f225510505fd6) for details on the implementation of both microservices.


