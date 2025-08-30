import numpy as np
import string

# Array of sample documents
documents = [
    "The sun rises in the east and sets in the west every day.",
    "Python is a popular programming language used for data science and web development.",
    "Mountains are beautiful natural formations that attract many hikers and tourists.",
    "Healthy eating and regular exercise are essential for maintaining a good lifestyle.",
    "Space exploration has advanced significantly with the development of new technologies."
]

filenames = [f"doc{i+1}.txt" for i in range(len(documents))]

def clean_text(text):
    # Convert to lowercase and remove punctuation
    return text.lower().translate(str.maketrans('', '', string.punctuation))

# Clean the documents
documents = [clean_text(doc) for doc in documents]

#  User enters a query
query = clean_text(input("Enter your query: "))
query_words = query.split()

# Convert each document into a vector based on query words
def text_to_vector(text, words):
    vec = np.zeros(len(words))
    
    text_words = text.split()
    for i, word in enumerate(words):
        vec[i] = text_words.count(word)
    
    return vec

query_vector = np.ones(len(query_words))  # TF in the query: 1 for each word
doc_vectors = np.array([text_to_vector(doc, query_words) for doc in documents])

#  Calculate cosine similarity
def cosine_similarity(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v) + 1e-10)

similarities = np.array([cosine_similarity(query_vector, doc_vec) for doc_vec in doc_vectors])

# Display results
sorted_indices = similarities.argsort()[::-1]

print("Documents most similar to your query:")
found = False
for idx in sorted_indices[:5]:
    if similarities[idx] > 0:
        print(f"{filenames[idx]} - similarity: {similarities[idx]:.3f}")
        found = True

if not found:
    print("No documents match your query.")
