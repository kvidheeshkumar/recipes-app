from sentence_transformers import SentenceTransformer
import json

# Load your recipe data
with open("bigger_sample.json") as f:
    data = json.load(f)

# Load a pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # ~384 dimensions

# Embed and store vector
for recipe in data:
    ingredients_text = recipe["embedding_ingredients"]
    embedding = model.encode(ingredients_text).tolist()
    recipe["embedding_vector"] = embedding

# Save new file
with open("bigger_sample_with_vectors.json", "w") as f:
    json.dump(data, f, indent=2)
