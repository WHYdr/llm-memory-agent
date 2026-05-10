from sentence_transformers import SentenceTransformer
from sentence_transformers import util


def get_embedding(text):

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    texts = ["I like pancakes", "I like waffles", "The weather is nice today"]

    embeddings = model.encode(texts)

    sim1 = util.cos_sim(embeddings[0], embeddings[1])
    sim2 = util.cos_sim(embeddings[0], embeddings[2])
    sim3 = util.cos_sim(embeddings[1], embeddings[2])

    print(sim1, sim2, sim3)