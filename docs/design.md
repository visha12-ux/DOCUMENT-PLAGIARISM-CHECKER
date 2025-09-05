# Design & Workflow

## Architecture
Input Document → Preprocessing → Similarity Calculation → Output Report

## Algorithms
- Tokenization (using NLTK)
- Cosine Similarity (using scikit-learn)
- N-gram based matching (optional)

## Workflow Example
1. User uploads 2 text files.
2. Preprocessing removes stopwords & punctuation.
3. Convert text into vector representation.
4. Calculate similarity score.
5. Display plagiarism percentage.
