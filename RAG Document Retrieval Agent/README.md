# RAG Document Retrieval Agent

Uses AI embeddings to find the most relevant documents for a query.

## Quick Start (5 Minutes)

### Step 1: Create Project Folder

```bash
mkdir rag-document-retrieval-agent
cd rag-document-retrieval-agent
touch documents.txt query.txt agent.py
```

### Step 2: Install Dependencies

```bash
pip install openai numpy
```

### Step 3: Set API Key

```bash
export OPENAI_API_KEY="your-api-key"
```
(Get key from [platform.openai.com](https://platform.openai.com))

### Step 4: Add Documents (documents.txt)

One document per line:

```
Doc1: AI agents automate tasks using decision logic and tools.
Doc2: Retrieval-Augmented Generation improves accuracy by grounding LLMs in documents.
Doc3: Prompt engineering affects output quality significantly.
```

### Step 5: Add Query (query.txt)

```
How does RAG improve LLM reliability?
```

### Step 6: Copy Code (agent.py)

Copy the entire code from the original script into `agent.py`.

### Step 7: Run

```bash
python agent.py
```

You get two files:
- `retrieved_context.json` — structured results
- `retrieved_context.txt` — readable report

## What It Does

- Reads documents and a search query
- Converts both to embeddings (numerical representation)
- Calculates similarity between query and each document
- Returns most relevant documents
- Outputs results with similarity scores

## Input Format

### documents.txt

One document per line:

```
Document 1 text here
Document 2 text here
Document 3 text here
```

Can be:
- Single sentences
- Full paragraphs
- Wikipedia entries
- Product descriptions
- Help articles
- API documentation

### query.txt

Single line with your search question:

```
Your search question or topic here
```

## Output Example

### retrieved_context.json
```json
{
  "date": "2024-06-01",
  "results": [
    {
      "document": "Retrieval-Augmented Generation improves accuracy by grounding LLMs in documents.",
      "similarity": 0.876
    },
    {
      "document": "AI agents automate tasks using decision logic and tools.",
      "similarity": 0.642
    }
  ]
}
```

### retrieved_context.txt
```
Retrieved Context
========================================

Score: 0.876 — Retrieval-Augmented Generation improves accuracy by grounding LLMs in documents.
Score: 0.642 — AI agents automate tasks using decision logic and tools.
```

## How It Works

1. **Embed documents** — Convert each document to a 1536-dimension vector
2. **Embed query** — Convert your query to the same vector space
3. **Calculate similarity** — Use cosine similarity (0-1 scale)
4. **Rank results** — Sort by highest similarity
5. **Return top K** — Return 2 most relevant (default)

Similarity score:
- **0.9+** — Highly relevant
- **0.7-0.9** — Relevant
- **0.5-0.7** — Somewhat relevant
- **<0.5** — Not relevant

## Input Examples

**Example 1 — Product Documentation:**
```
documents.txt:
The API endpoint accepts GET and POST requests.
Authentication requires a valid API key in headers.
Rate limits are 1000 requests per hour.
Error codes are documented in the error handling section.

query.txt:
How do I authenticate with the API?
```

**Example 2 — Knowledge Base:**
```
documents.txt:
Python is a high-level programming language.
Machine learning uses algorithms to learn from data.
Neural networks are inspired by the human brain.
Deep learning uses multiple layers of neural networks.

query.txt:
What are neural networks used for?
```

**Example 3 — Customer Support:**
```
documents.txt:
To reset your password, click the forgot password link on login page.
Account deletion is permanent and cannot be undone.
Payment methods can be updated in account settings.
Two-factor authentication enhances security.

query.txt:
How do I change my payment method?
```

## Customize

**Get more results (top 5 instead of 2):**
```python
results = retrieve(docs, query, top_k=5)
```

**Change embedding model:**
```python
response = client.embeddings.create(
    model="text-embedding-3-large",  # Use larger model for better accuracy
    input=text
)
```

**Filter by score threshold:**
```python
# Only return documents with score > 0.7
results = [r for r in scored if r[1] > 0.7][:top_k]
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `FileNotFoundError` | Create documents.txt and query.txt in same folder |
| `ModuleNotFoundError` | Run `pip install openai numpy` |
| Low similarity scores | Add more detailed documents |
| Wrong documents retrieved | Rephrase query more specifically |

## Tips

- Use specific, detailed documents for better matching
- Ask clear, focused questions in query.txt
- Review similarity scores to assess confidence
- Add more documents for better coverage
- Use for knowledge base search, documentation lookup, Q&A systems

## Multiple Queries

Search with different questions:

```python
queries = [
    "How does RAG work?",
    "What is prompt engineering?",
    "How do AI agents make decisions?"
]

for q in queries:
    with open("query.txt", "w") as f:
        f.write(q)
    
    docs = load_documents()
    query_text = load_query()
    results = retrieve(docs, query_text)
    save_outputs(results)
    print(f"✓ Retrieved context for: {q[:30]}...")
```

## Large Document Sets

For many documents, consider pre-caching embeddings:

```python
# Pre-compute once, reuse for multiple queries
embeddings_cache = {}
for i, doc in enumerate(docs):
    if i not in embeddings_cache:
        embeddings_cache[i] = embed(doc)

# Now reuse cache for faster retrieval
def retrieve_cached(docs, query, top_k=2):
    query_vec = embed(query)
    scored = []
    for i, d in enumerate(docs):
        vec = embeddings_cache[i]
        score = cosine_similarity(query_vec, vec)
        scored.append((d.strip(), score))
    
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k]
```

## Expected Behavior

**Input:**
```
documents.txt:
The capital of France is Paris.
Berlin is the capital of Germany.
London is the capital of England.

query.txt:
What is the capital of France?
```

**Output:**
```
Score: 0.952 — The capital of France is Paris.
Score: 0.421 — London is the capital of England.
```

(Top document has very high score because it directly answers the query)

## Cost

- Small model: ~$0.02 per 1M tokens
- Large model: ~$0.13 per 1M tokens
- Example: 100 documents + 100 queries = ~$0.10