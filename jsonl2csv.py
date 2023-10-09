from datasets import load_dataset
import pandas as pd
from tqdm import tqdm
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", help="輸入檔名(jsonl)", dest="input")
  parser.add_argument("-o", help="輸出檔名(csv)", dest="output")
  args = parser.parse_args()

  if args.input is None:
    parser.print_help()
    exit()

  if args.output is None:
    args.output = "output.csv"

  dataset = load_dataset("json", data_files=[args.input], split="train")

  df = pd.DataFrame(columns=dataset.features)
  for d in tqdm(dataset):
    df.loc[len(df)] = d

  print(df)
  df.to_csv(args.output,index=False)