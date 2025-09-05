def main():
    # Sample input documents
    doc1 = "This is a sample document. It contains some text."
    doc2 = "This document is just a sample. It has some text."

    # Preprocess
    text1 = clean_text(doc1)
    text2 = clean_text(doc2)

    # Calculate similarity
    score = calculate_similarity(text1, text2)

    print(f"Plagiarism detected: {score*100:.2f}% similarity")

if _name_ == "_main_":
    main()
