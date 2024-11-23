
def read_file(file_path : str, encoding : str = "utf-8", mode : str = "r") -> str:
  with open(file_path, mode, encoding=encoding) as file:
    return file.read()

def write_file(file_path : str, content : str, encoding : str = "utf-8", mode : str = "w"):
  with open(file_path, mode, encoding=encoding) as file:
    file.write(content)
        
import pandas as pd

def convert_pandas_to_excel(df : pd.DataFrame, file_path : str):
  with pd.ExcelWriter(file_path) as writer:
    df.to_excel(writer, index=False)
    
import anthropic, dotenv, os

dotenv.load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Client(api_key=api_key)
def inference(prompt: str):
  response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    max_tokens=4096,
  )
  return response.content[0].text

import shutil
def flush_create_directory(path: str):
  if os.path.exists(path):
    shutil.rmtree(path)
  os.makedirs(path)

def parse_as_int_list(text: str) -> list[int]:
    return [int(x) for x in text.strip().split()]
