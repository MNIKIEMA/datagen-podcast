import gradio as gr
import os
import query_index
import datasets
import sentence_transformers

def query(text, k=5):
    model = sentence_transformers.SentenceTransformer(
    "dangvantuan/sentence-camembert-large", device="cpu")

    dataset = datasets.load_dataset("json", data_files=["./data/dataset.json"], split="train")
    dataset.load_faiss_index("embeddings", "index.faiss")

    query_embedding = model.encode(text)
    _, retrieved_examples = dataset.get_nearest_examples(
        "embeddings",
        query_embedding,
        k=k,
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

iface = gr.Interface(
  fn=query, 
  inputs='text',
  outputs='text',
  examples=[["Qu'est ce qui t'a fait le plus progresser?"]]
)

iface.launch()