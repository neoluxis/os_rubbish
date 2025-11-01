from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import datetime
import pathlib
import subprocess
import traceback
import logging

# 环境变量加载
load_dotenv()

BASE_URL = os.getenv("OPENAI_BASE_URL", "")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-5")
API_KEY = os.getenv("OPENAI_API_KEY")
INTERVAL = int(os.getenv("TIME_INTERVAL", "300"))  # 分钟
CODE_PATH = os.getenv("CODE_PATH", "./code")
DEBUG = os.getenv("DEBUG", "INFO").upper()  # 从 .env 获取日志级别

if not API_KEY:
    raise Exception("API key cannot be empty!")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
pathlib.Path(CODE_PATH).mkdir(parents=True, exist_ok=True)

# 配置日志等级
logging.basicConfig(
    level=getattr(logging, DEBUG, logging.INFO),  # 设置日志等级
    format='%(asctime)s [%(levelname)s] - %(message)s',
    handlers=[
        logging.StreamHandler(),  # 控制台输出
        logging.FileHandler('task.log', mode='a', encoding='utf-8')  # 文件输出
    ]
)


def list_history():
    """列出代码目录下所有文件，返回字符串"""
    try:
        result = subprocess.run(
            ["ls", "-R", CODE_PATH],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Error listing history: {e}")
        return ""


def git(path, commit_message):
    """执行 git add, commit, push 并打印输出"""
    try:
        for cmd in [['git', 'add', path], ['git', 'commit', '-m', commit_message], ['git', 'push']]:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.stdout:
                logging.info(result.stdout.strip())
            if result.stderr:
                logging.error(result.stderr.strip())
    except Exception as e:
        logging.error(f"Git operation failed: {e}")


history_default = [
    {
        "role": "system",
        "content": f"你是一个程序员，精通Python, Java, C++ 和 Rust 编程语言，并且非常熟悉算法。在本任务中，你写的代码保存在{CODE_PATH}，该文件夹结构为：{list_history()}，按照语言进行分类。"
    }
]
history = history_default.copy()


def chat(query):
    """向模型发送对话并返回响应"""
    global history
    history.append({"role": "user", "content": query})
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=history,
        temperature=0.6,
    )
    result = completion.choices[0].message.content
    history.append({"role": "assistant", "content": result})
    return result


def task():
    """执行一次任务：生成代码，保存文件，git 提交"""
    global history
    history = history_default.copy()
    logging.info("Starting new task...")

    try:
        output = chat(
            f"从leetcode随便挑选一道题目，给出解决方案，任选语言。"
            f"当前已有{list_history()}，注意不要重复。"
            f"以纯文本形式输出以下信息：1. 纯文本的文件保存位置；"
            f"2. 纯文本格式的代码；3. 对于该代码的 git commit 信息，只需要commit信息。"
            f"三者之间使用 --split-- 进行分割"
        )
        path, code, commit = [x.strip() for x in output.split('--split--')]
        full_path = os.path.join(CODE_PATH, path) if not os.path.isabs(path) else path

        # 保存代码
        pathlib.Path(os.path.dirname(full_path)).mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(code)
        logging.info(f"Code saved to {full_path}")

        # Git 提交
        git(full_path, commit)
        logging.info(f"Task finished with commit: {commit}")

    except Exception as e:
        logging.error(f"Task failed: {e}\n{traceback.format_exc()}")


def main():
    i = 0
    while True:
        try:
            task()
            i += 1
            logging.info(f"Sleeping for {INTERVAL} minutes before next task...")
            time.sleep(INTERVAL * 60)
        except Exception as e:
            logging.error(f"Main loop error: {e}\n{traceback.format_exc()}")
            time.sleep(60)  # 遇到异常等待 1 分钟


if __name__ == '__main__':
    main()
