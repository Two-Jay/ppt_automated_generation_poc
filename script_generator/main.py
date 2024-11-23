import pandas as pd
import re
import os
from concurrent.futures import ThreadPoolExecutor
from utils import read_file
# 주어진 텍스트 데이터
target_directory = input("Insert target directory : ")
if target_directory == "":
  raise Exception("Directory name cannot be empty")
target_directory = f"{os.path.dirname(__file__)}/toc/{target_directory}"
if not os.path.exists(target_directory):
  raise Exception("Directory does not exist")

inserted_file_name = input("Insert file name : ")

text_data_path = f"{target_directory}/{inserted_file_name}.md"
text_data = read_file(text_data_path)
file_name = text_data_path.split("/")[-1].split(".")[0]

# 데이터 파싱
chapters = re.split(r'- Chapter \d+: ', text_data)[1:]  # 각 챕터로 분리
data = {"Chapter": [], "Subtopic": [], "Description": []}

for chapter in chapters:
  lines = chapter.strip().split('\n')
  chapter_title = lines[0].strip()
  for line in lines[1:]:
      match = re.match(r'\d+\.\s*(.*?):\s*(.*)', line.strip())
      if match:
          subtopic, description = match.groups()
          data["Chapter"].append(chapter_title)
          data["Subtopic"].append(subtopic)
          data["Description"].append(description)

# 데이터프레임 생성
df = pd.DataFrame(data)
# 데이터프레임을 엑셀 파일로 저장
df.to_excel("cloud_services.xlsx", index=False)

def parse_chapter_contents(text_data : str):
  chapters = re.split(r'- Chapter \d+: ', text_data)[1:]
  chapter_list = []
  for chapter in chapters:
    lines = chapter.strip().split('\n')
    chapter_title = lines[0].strip()
    subtopics = [line.strip() for line in lines[1:] if line.strip()]
    chapter_list.append((chapter_title, subtopics))
  return chapter_list

def concat_chapter_contents(parsed_chapter : tuple[str, list[str]]):
  result = ""
  chapter_title, subtopics = parsed_chapter
  result += f"Chapter : {chapter_title}\n"
  for subtopic in subtopics:
    result += f"- {subtopic}\n"
  return result

from utils import write_file, read_file, parse_as_int_list, flush_create_directory, inference

chapter_list = parse_chapter_contents(text_data)
for i in chapter_list:
  print(concat_chapter_contents(i))



script_generation_prompt = read_file(f"{os.path.dirname(__file__)}/prompt/script_prompt.md")
audience = read_file(f"{os.path.dirname(__file__)}/prompt/audience.md")
script_generation_prompt = script_generation_prompt.replace("{audience}", audience)


import configparser
config = configparser.ConfigParser()
config.read("config.ini")

chapter_count = len(chapter_list)
duration_per_slide = config["parameter"]["duration"]
slide_amount_per_chapter = config["parameter"]["slide_amount"]
duration_list = [duration_per_slide] * chapter_count
slide_amount_list = [slide_amount_per_chapter] * chapter_count

# duration_list = parse_as_int_list(config["parameter"]["duration"])
# slide_amount_list = parse_as_int_list(config["parameter"]["slide_amount"])
assert len(duration_list) == len(slide_amount_list) == len(chapter_list), "The length of duration, slide_amount, and chapter_list must be the same"
result_path = f"{os.path.dirname(__file__)}/results"
# flush_create_directory(result_path)
output_path = f"{result_path}/script"

def generate_script_for_chapter(i):
  chapter_data = concat_chapter_contents(chapter_list[i])
  prompt = str(script_generation_prompt).replace("{chapter_content}", chapter_data)
  prompt = prompt.replace("{duration}", str(duration_list[i]))
  prompt = prompt.replace("{slide_amount}", str(slide_amount_list[i]))
  script = inference(prompt)
  write_file(output_path+f"_{file_name}_{i+1}.txt", script, mode="w")
  print(f"Generated script for chapter {i+1}")
  print(f"generated script :\n{script}")

slide_script_list = []

# 멀티스레딩을 사용하여 스크립트 생성
with ThreadPoolExecutor(max_workers=chapter_count) as executor:
  executor.map(generate_script_for_chapter, range(len(duration_list)))

"""
[slide_1_start]
안녕하세요, 오늘은 IT 인프라의 개요에 대해 알아보겠습니다. IT 인프라란 무엇일까요? 간단히 말해, IT 인프라는 기업의 IT 서비스를 지원하는 기반 시스템과 구조를 말합니다. 우리가 일상에서 사용하는 컴퓨터, 스마트폰, 인터넷 등이 모두 IT 인프라의 일부라고 할 수 있죠. 이러한 IT 인프라는 기업의 업무 수행에 필수적인 요소입니다. 예를 들어, 은행에서 ATM을 이용할 때, 그 뒤에는 복잡한 IT 인프라가 작동하고 있습니다.
[slide_1_end]

[slide_2_start]
IT 인프라의 구성요소에는 크게 세 가지가 있습니다: 하드웨어, 소프트웨어, 그리고 네트워크입니다. 하드웨어는 우리가 직접 볼 수 있고 만질 수 있는 물리적인 장비를 말합니다. 예를 들면, 컴퓨터, 서버, 스마트폰 등이 있죠. 소프트웨어는 이러한 하드웨어를 작동시키는 프로그램들을 말합니다. 우리가 흔히 사용하는 워드프로세서, 이메일 프로그램, 그리고 운영체제 등이 소프트웨어에 해당합니다. 마지막으로 네트워크는 이러한 하드웨어와 소프트웨어를 연결하는 통신 시스템을 의미합니다. 인터넷이 대표적인 네트워크의 예시입니다.
[slide_2_end]

[slide_3_start]
이러한 구성요소들은 서로 밀접하게 연관되어 있습니다. 예를 들어, 여러분이 스마트폰으로 이메일을 확인할 때를 생각해봅시다. 이때 스마트폰은 하드웨어, 이메일 앱은 소프트웨어, 그리고 데이터를 주고받는 인터넷 연결은 네트워크에 해당합니다. 이 세 가지 요소가 모두 제대로 작동해야만 우리는 원활하게 이메일을 확인할 수 있습니다. 이처럼 IT 인프라의 각 구성요소는 서로 유기적으로 연결되어 있어, 하나라도 문제가 생기면 전체 시스템에 영향을 미칠 수 있습니다.
[slide_3_end]

[slide_4_start]
IT 인프라는 크게 두 가지 유형으로 나눌 수 있습니다: 온프레미스와 클라우드입니다. 온프레미스는 기업이 자체적으로 IT 인프라를 구축하고 관리하는 방식을 말합니다. 쉽게 말해, 회사 내부에 서버실을 두고 직접 관리하는 것이죠. 반면, 클라우드는 인터넷을 통해 IT 인프라를 서비스로 제공받는 방식입니다. 우리가 흔히 사용하는 구글 드라이브나 아이클라우드가 클라우드 서비스의 예시입니다.
[slide_4_end]
"""