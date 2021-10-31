from sentence_transformers import SentenceTransformer

model = SentenceTransformer("models/all-MiniLM-L12-v2")

vec = model.encode("I want to open an account.")

print(vec[:5])
