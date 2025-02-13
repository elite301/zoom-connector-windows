import asyncio
import os

from dotenv import load_dotenv
load_dotenv()

from ablyUtil import Ably

if __name__ == "__main__":
    asyncio.run(Ably(os.getenv('API_KEY'), os.getenv('CHANNEL')))
