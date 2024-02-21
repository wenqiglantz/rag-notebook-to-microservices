This is a [LlamaIndex](https://www.llamaindex.ai/) project using [FastAPI](https://fastapi.tiangolo.com/) bootstrapped with [`create-llama`](https://github.com/run-llama/LlamaIndexTS/tree/main/packages/create-llama).

## Getting Started

First, setup the environment:

```
poetry install
poetry shell
```

By default, we use the OpenAI LLM (though you can customize). As a result you need to specify an `OPENAI_API_KEY` in an .env file in this directory.

Please add a `.env` file at the project root, you can copy content from `.env.example` and fill in the placeholder values, see a sample `.env.example` below:

```
# OpenAI
MODEL=gpt-3.5-turbo-0125
OPENAI_API_KEY=sk-###

# Milvus
MILVUS_API_KEY=###
MILVUS_URI="https://###.api.gcp-us-west1.zillizcloud.com"
MILVUS_COLLECTION="###"
MILVUS_DIMENSION=1536
```

Second, generate the embeddings of the documents in the `./data` directory (if this folder exists - otherwise, skip this step):

```
python app/engine/generate.py
```
or you can trigger a POST call to the endpoint `/api/ingestion` by navigating to the swagger UI of the API: [http://localhost:8000/docs](http://localhost:8000/docs).



The API allows CORS for all origins to simplify development. You can change this behavior by setting the `ENVIRONMENT` environment variable to `prod`:

```
ENVIRONMENT=prod uvicorn main:app
```

## Learn More

To learn more about LlamaIndex, take a look at the following resources:

- [LlamaIndex Documentation](https://docs.llamaindex.ai) - learn about LlamaIndex.

You can check out [the LlamaIndex GitHub repository](https://github.com/run-llama/llama_index) - your feedback and contributions are welcome!
