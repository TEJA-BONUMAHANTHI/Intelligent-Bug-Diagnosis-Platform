# Semantic Similarity Techniques

## 1. Introduction

Semantic similarity measures how closely two pieces of text are related in meaning.

In an intelligent bug diagnosis platform, semantic similarity is used to identify historical bug reports that are conceptually similar to a newly submitted bug.

## 2. Keyword Matching Limitation

Traditional search methods mainly depend on matching exact words.

For example:

Bug A:
"Application crashes while opening a large file."

Bug B:
"Program terminates unexpectedly when processing huge files."

Although the wording is different, both bugs describe a similar problem.

Keyword-based search may not identify this relationship effectively.

## 3. Text Embeddings

Text embeddings convert text into numerical vectors.

For example:

Bug Report
→ Embedding Model
→ Numerical Vector

The vector captures important semantic information from the text.

## 4. Semantic Similarity

Two bug reports can be compared using their embedding vectors.

If two vectors are close to each other, the corresponding bug reports are likely to have similar meanings.

## 5. Cosine Similarity

Cosine similarity is commonly used to measure similarity between embedding vectors.

The formula is:

Cosine Similarity =
(A · B) / (||A|| × ||B||)

Where:

- A = First text embedding
- B = Second text embedding
- A · B = Dot product
- ||A|| = Magnitude of vector A
- ||B|| = Magnitude of vector B

The value generally ranges from -1 to 1.

For normalized text embeddings, higher values indicate greater similarity.

## 6. Example

Suppose a new bug report is:

"Null pointer exception occurs while loading user profile."

The historical knowledge base may contain:

1. "Null pointer error while opening customer profile."
2. "Database connection timeout during login."
3. "User profile page displays incorrect information."

Semantic search can identify the first report as the most relevant result.

## 7. Top-K Retrieval

Instead of retrieving only one result, the system can retrieve the Top-K similar records.

For example:

K = 5

The system retrieves the five most similar historical defects.

These records are then passed to the RAG pipeline.

## 8. Duplicate Detection

Semantic similarity can help detect duplicate bug reports.

Two reports with different wording but similar meaning can receive a high similarity score.

This can help developers identify whether an issue has already been reported.

## 9. Root Cause Analysis

Similarity search can also retrieve historical bugs that experienced similar root causes.

Historical resolution information can provide useful evidence for diagnosis.

## 10. Embedding Model Selection

The embedding model should provide good semantic representations for software-related text.

Possible approaches include:

- Sentence Transformers
- General-purpose embedding models
- Domain-specific embedding models

For the prototype, Sentence Transformer models can be evaluated because they are easy to integrate and can run locally.

## 11. Similarity Search Pipeline

The complete process is:

Bug Report
→ Text Preprocessing
→ Embedding Generation
→ Vector Similarity Search
→ Top-K Historical Defects
→ RAG Context
→ AI Diagnosis

## 12. Evaluation

Semantic retrieval quality can be evaluated using:

- Precision
- Recall
- Top-K accuracy
- Mean Reciprocal Rank
- Similarity score analysis
- Manual relevance evaluation

## 13. Benefits

Semantic similarity provides:

- Meaning-based search
- Better duplicate detection
- Relevant historical defect retrieval
- Improved RAG context
- Better diagnosis support

## 14. Conclusion

Semantic similarity is an important component of the Intelligent Bug Diagnosis Platform because it enables the system to find historically relevant defects even when the wording of the current bug differs from previous reports.