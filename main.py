from dotenv import load_dotenv
import os

def main(args=None):
    load_dotenv()

    print(os.getenv("TIME_INTERVAL"))

if __name__ == '__main__':
    main()
