from datasets import load_dataset
import pandas as pd
from tqdm import tqdm

dataset = load_dataset("json", data_files=["Traditional_dolly_conv.jsonl"], split="train")

df = pd.DataFrame(columns=dataset.features)
for d in tqdm(dataset):
  df.loc[len(df)] = d
print(df)
df.to_csv("dolly-15k-CKIP.csv",index=False)