from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import datetime
import pathlib
import subprocess

load_dotenv()

BASE_URL = os.getenv("OPENAI_BASE_URL", "")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-5")
API_KEY = os.getenv("OPENAI_API_KEY")
INTERVAL = int(os.getenv("TIME_INTERVAL", "300"))
CODE_PATH = os.getenv("CODE_PATH", "./code")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

if not API_KEY:
    raise Exception("API key cannot be empty!")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
pathlib.Path(CODE_PATH).mkdir(parents=True, exist_ok=True)


def chat(query):
    global history
    history.append({
        "role": "user",
        "content": query
    })
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=history,
        temperature=0.6,
    )
    result = completion.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": result
    })
    return result

def log(s):
    if DEBUG: print(str(s))


def list_history():
    result = subprocess.run(
        ["ls", "-R", CODE_PATH],
        capture_output=True,
        text=True
    )
    return result

def git(path, commit):
    add = subprocess.run(
        ['git', 'add', path],
        capture_output=True,
        text=True
    )
    log(add)
    commit = subprocess.run(
        ['git', 'commit', '-m', commit],
        capture_output=True,
        text=True
    )
    log(commit)
    push = subprocess.run(
        ['git', 'push'],
        capture_output=True,
        text=True
    )
    log(push)

history_default = [
    {"role": "system", "content": f"你是一个程序员，精通Python, Java, C++ 和 Rust 编程语言，并且非常熟悉算法。在本任务中，你写的代码保存在{CODE_PATH}，该文件夹结构为：{list_history()}，按照语言进行分类。"}
]
history = history_default

def task():
    global history
    history = history_default
    log(history)

    output = chat(f"从leetcode随便挑选一道题目，给出解决方案，任选语言。当前已有{list_history()}，注意不要重复。以纯文本形式输出以下信息：1. 纯文本的文件保存位置；2. 纯文本格式的代码；3. 对于该代码的 git commit 信息，只需要commit信息。三者之间使用 --split-- 进行分割")
    path, code, commit = output.split('--split--')
    path = path.strip()
    code = code.strip()
    commit = commit.strip()
    # print(path, code, commit)

    print(f"Code save to {path}")
    with open(path, 'w') as f: f.write(code)
    git(path, commit)



def main(args=None):
    # list_history()
    i=0
    while True:
        try:
            task()
            log(f"Finish task {i}")
            i+=1
            time.sleep(INTERVAL*60)
        except Exception as e:
            print(e)
            time.sleep(60) # wait for 1 min request rate

if __name__ == '__main__':
    main()

