import argparse
import logging

import datasets
import sentence_transformers

import utils

logging.disable(logging.CRITICAL)

parser = argparse.ArgumentParser()
parser.add_argument("--query", type=str, required=True)
parser.add_argument("--k", type=int, default=5)
args = parser.parse_args()

model = sentence_transformers.SentenceTransformer(
    "dangvantuan/sentence-camembert-large", device="cuda"
)

dataset = datasets.load_dataset("json", data_files=["./data/dataset.json"], split="train")
dataset.load_faiss_index("embeddings", "index.faiss")

query_embedding = model.encode(args.query)
_, retrieved_examples = dataset.get_nearest_examples(
    "embeddings",
    query_embedding,
    k=args.k,
)


for text, start, end, title, url in zip(
    retrieved_examples["text"],
    retrieved_examples["start"],
    retrieved_examples["end"],
    retrieved_examples["title"],
    retrieved_examples["url"],
):
    start = start
    end = end
    print(f"title: {title}")
    print(f"transcript: [{str(start)+' ====> '+str(end)}] {text}")
    print(f"link: {url}")
    print("*" * 10)