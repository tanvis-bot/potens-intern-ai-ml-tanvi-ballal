import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("data/incidents.json", "r") as f:
    incidents = json.load(f)

incident_texts = [incident["issue"] for incident in incidents]
incident_embeddings = model.encode(incident_texts)

def search_similar_incidents(query: str):
    """
    Search similar historical incidents.
    """

    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        incident_embeddings
    )[0]

    best_match_index = np.argmax(similarities)

    return incidents[best_match_index]