import os
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

def create_index(index_name: str, dimension: int):
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

def upsert_chunks(index_name: str, chunks: list[str]):
    index = pc.Index(index_name)
    embeddings = embed_model.encode(chunks, convert_to_tensor=False).tolist()
    vectors = [(f"chunk-{i}", emb, {"text": chunks[i]}) for i, emb in enumerate(embeddings)]
    index.upsert(vectors=vectors)
    return index

def search(index, query: str, top_k: int = 5):
    q_emb = embed_model.encode(query, convert_to_tensor=False).tolist()
    results = index.query(vector=q_emb, top_k=top_k, include_metadata=True)
    return [match["metadata"]["text"] for match in results["matches"]]
