import datasets
import faiss
from sentence_transformers import SentenceTransformer
import torch

print(torch.cuda.is_available())

def get_embeddings(batch, model):
    embeddings = model.encode(batch["text"])
    return {"embeddings": embeddings}

model =  SentenceTransformer("dangvantuan/sentence-camembert-large",
                                                        device="cuda")
dataset = datasets.load_dataset("json", data_files=["./data/dataset.json"], split="train")
dataset = dataset.map(get_embeddings, batched=True, fn_kwargs={"model": model})
dataset = dataset.with_format(
    type="numpy", columns=["embeddings"], output_all_columns=True
)
dataset.add_faiss_index("embeddings", metric_type=faiss.METRIC_INNER_PRODUCT)
dataset.save_faiss_index("embeddings", "index.faiss")