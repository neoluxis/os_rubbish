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
    print(s)


def list_history():
    result = subprocess.run(
        ["ls", "-R", CODE_PATH],   # 命令及参数
        capture_output=True,  # 捕获 stdout/stderr
        text=True            # 返回字符串而不是 bytes
    )
    return result

def git(commit):
    os.system("git add .")
    os.system(f'git commit "{commit}"')
    os.system("git push")

history_default = [
    {"role": "system", "content": f"你是一个程序员，精通Python, Java, C++ 和 Rust 编程语言，并且非常熟悉算法。在本任务中，你写的代码保存在{CODE_PATH}，该文件夹结构为：{list_history()}，按照语言进行分类。"}
]
history = history_default

def task():
    global history
    history = history_default
    print(history)

    # output = chat(f"从leetcode随便挑选一道题目，给出解决方案，任选语言。当前已有{list_history()}，注意不要重复。以纯文本形式输出以下信息：1. 纯文本的文件保存位置；2. 纯文本格式的代码；3. 对于该代码的 git commit 信息，只需要commit信息。三者之间使用 --split-- 进行分割")
    output = """
./code/python/3_longest_substring_without_repeating_chars.py
--split--
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = set()

        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            max_len = max(max_len, right - left + 1)

        return max_len
--split--
add Python solution for LeetCode 3. Longest Substring Without Repeating Characters
"""
    path, code, commit = output.split('--split--')
    path = path.strip()
    code = code.strip()
    commit = commit.strip()
    print(path, code, commit)

    print(f"Code save to {path}")
    with open(path, 'w') as f: f.write(code)
    git(commit)
    # path = chat(f"从leetcode随便挑选一道题目，给出解决方案，任选语言。当前已有{list_history()}，注意不要重复。首先确定题目和文件保存位置。仅需纯文本输出保存位置即可")
    # print(f"File save to {path}")
    # time.sleep(5)
    # code = chat(f"现在给出该题目的解决方案。只需要纯文本的格式给出代码")
    # print(f"Code: \n{code}")
    # with open(path, 'w') as f: f.write(code)
    # time.sleep(5)
    # commit = chat(f"现在给出本次 git commit 的信息。只需要纯文本输出该信息")
    # print(commit)
    # git(commit)


def main(args=None):
    list_history()
    while True:
        task()
        log("Finish task")
        break
        # time.sleep(INTERVAL*60)

if __name__ == '__main__':
    main()

