## TODOs / challenges

1. Load your own markdown notes (or any text), chunk them into overlapping pieces (fixed size + overlap is fine to start).
2. Embed the chunks with an open-source sentence-transformers model. Manually verify: normalize two embeddings and compute their dot product yourself with NumPy — confirm it matches what `cosine_similarity` from a library gives you. This is the "prove you understand the math" step.
3. Stand up a local Qdrant instance (Docker, or the in-memory client to start) and upsert your embedded chunks with metadata (source file, text).
4. Write a `search(query, top_k)` function: embed the query the same way, query Qdrant, return ranked chunks with scores.
5. Challenge: swap in a second embedding model and compare result quality on the same queries — write down what you notice.