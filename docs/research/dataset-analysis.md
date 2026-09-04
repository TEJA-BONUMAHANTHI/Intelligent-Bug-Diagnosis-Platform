# Historical Defect Dataset Analysis

## 1. Introduction

Historical defect datasets contain previously reported software bugs and their associated information.

These datasets are useful for building a knowledge base for an intelligent bug diagnosis platform.

Public defect datasets from software projects such as Mozilla, Apache, and Eclipse can be used as initial sources.

## 2. Dataset Sources

The proposed knowledge base can be seeded using publicly available defect data from:

- Mozilla
- Apache
- Eclipse

These projects contain large collections of real-world software defect reports.

## 3. Bug Report Structure

A typical bug report may contain:

- Bug ID
- Summary
- Description
- Product
- Component
- Version
- Priority
- Severity
- Reporter
- Assignee
- Status
- Comments
- Resolution
- Creation date
- Modification date

Not every dataset contains all fields.

## 4. Data Cleaning

Raw datasets may contain noisy information.

Cleaning activities include:

- Removing duplicate records
- Handling missing values
- Removing unnecessary HTML
- Normalizing text
- Removing irrelevant metadata
- Standardizing field names
- Handling special characters

## 5. Data Normalization

Different datasets may use different field names.

For example:

Mozilla:
bug_summary

Apache:
summary

Eclipse:
bug_summary

These can be mapped to a common field such as:

summary

A normalized schema makes it easier to process multiple datasets together.

## 6. Proposed Common Schema

The knowledge base can use fields such as:

- defect_id
- project
- product
- component
- summary
- description
- severity
- priority
- status
- resolution
- comments
- created_date
- updated_date

## 7. Text Construction

Relevant fields can be combined into a searchable document.

Example structure:

Project: Mozilla

Component: Browser

Summary:
Application crashes while opening a page.

Description:
The browser crashes when a specific page is loaded.

Resolution:
Fixed memory handling issue.

This combined text can be converted into an embedding.

## 8. Chunking

Large defect reports can be divided into smaller chunks.

Possible chunks include:

- Summary
- Description
- Comments
- Resolution

Chunking helps retrieve the most relevant information.

## 9. Metadata

Metadata should be stored along with each vector.

Useful metadata includes:

- Defect ID
- Project
- Product
- Component
- Severity
- Priority
- Resolution

Metadata allows filtering and better interpretation of search results.

## 10. Embedding Pipeline

The proposed pipeline is:

Dataset
→ Cleaning
→ Normalization
→ Text Construction
→ Chunking
→ Embedding Generation
→ Vector Indexing

## 11. Vector Store

Embeddings can be stored in:

- FAISS
- Chroma
- Qdrant
- Milvus

For an initial prototype, FAISS or Chroma can be used.

## 12. Retrieval Testing

The retrieval system should be tested using sample bug reports.

For each query:

1. Generate query embedding.
2. Search the vector index.
3. Retrieve Top-K defects.
4. Inspect relevance.
5. Record similarity scores.
6. Evaluate retrieval quality.

## 13. Data Quality Considerations

Important factors include:

- Dataset completeness
- Duplicate records
- Missing values
- Text quality
- Correct metadata
- Resolution information
- Class imbalance

Good-quality data improves semantic retrieval and diagnosis.

## 14. Knowledge Base Updates

The knowledge base can be updated periodically.

New defect records can follow:

New Bug
→ Cleaning
→ Chunking
→ Embedding
→ Vector Index Update

This allows the system to continuously expand its historical knowledge.

## 15. Conclusion

Historical defect datasets provide valuable real-world knowledge for the Intelligent Bug Diagnosis Platform. Cleaning, normalization, chunking, embedding, and vector indexing transform raw defect reports into a searchable knowledge base suitable for RAG-based diagnosis.