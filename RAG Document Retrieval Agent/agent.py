import json
import numpy as np
from openai import OpenAI
from datetime import date
 
client = OpenAI()  # requires OPENAI_API_KEY
 
def embed(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(response.data[0].embedding)
 
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
 
def load_documents(path="documents.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()
 
def load_query(path="query.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 
def retrieve(docs, query, top_k=2):
    query_vec = embed(query)
    scored = []
 
    for d in docs:
        vec = embed(d)
        score = cosine_similarity(query_vec, vec)
        scored.append((d.strip(), score))
 
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k]
 
def save_outputs(results):
    payload = {
        "date": str(date.today()),
        "results": [
            {"document": r[0], "similarity": round(float(r[1]), 3)}
            for r in results
        ]
    }
 
    with open("retrieved_context.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
 
    with open("retrieved_context.txt", "w", encoding="utf-8") as f:
        f.write("Retrieved Context\n")
        f.write("=" * 40 + "\n\n")
        for r in payload["results"]:
            f.write(f"Score: {r['similarity']} — {r['document']}\n")
 
def main():
    docs = load_documents()
    query = load_query()
    results = retrieve(docs, query)
    save_outputs(results)
    print("RAG document retrieval completed.")
 
if __name__ == "__main__":
    main()