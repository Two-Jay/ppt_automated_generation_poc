from utils import read_file, write_file, inference, flush_create_directory
from typing import List
import os
import re
import pandas as pd

def parse_script(script_text: str) -> list:
  pattern = r'\[slide_(\d+)_start\]\nsubtitle: (.*?)\n(.*?)\[slide_\1_end\]'
  slides = re.findall(pattern, script_text, re.DOTALL)
  return [{"subtitle": subtitle.strip(), "content": content.strip()} for _, subtitle, content in slides]

def parse_subtopic_list(parameter : str, delimiter : str = "|") -> List[str]:
  return parameter.split(delimiter)

current_dir = os.path.dirname(__file__)

import configparser
config = configparser.ConfigParser()
config.read(f"{current_dir}/config.ini")
script_path = f"{current_dir}/scripts"
chapter_name = config["parameter"]["chapter_name"]

audience = read_file(f"{current_dir}/audience.md")
subtopic_list = parse_subtopic_list(config["parameter"]["subtopic_name_list"])

range_max = int(config["parameter"]["range_max"])

log_format = """
--------------------------------
result:
{result}
subtopic: {subtopic}
chapter: {chapter}
"""

# 각 파일에 대해 반복문을 실행합니다.
for i in range(1, range_max + 1):
    script_text = read_file(f"{script_path}/{chapter_name}/script_{chapter_name}_{i}.txt")
    parsed_slides = parse_script(script_text)

    prompt = read_file(f"{current_dir}/prompts/prompt.md")
    prompt = prompt.replace("{chapter_name}", chapter_name)
    prompt = prompt.replace("{audience_characteristics}", audience)

    def convert_ppt_content(prompt : str, script_text : str, subtopic : str) -> str:
      prompt = prompt.replace("{script_content}", script_text)
      prompt = prompt.replace("{subtopic_name}", subtopic)
      return inference(prompt)

    content_list = []
    for subtitle in parsed_slides:
        result = convert_ppt_content(prompt, subtitle["content"], subtitle["subtitle"])
        print(log_format.format(result=result, subtopic=subtitle["subtitle"], chapter=chapter_name))
        content_list.append({"Content": result, "Subtopic": subtitle["subtitle"], "Chapter": chapter_name})

    df = pd.DataFrame(content_list)
    df.to_excel(f"{current_dir}/content_list_{chapter_name}_{i}.xlsx", index=False)
