# test_env.py
from dotenv import load_dotenv
import os

load_dotenv()

print("TOKEN :", os.getenv("AI_API_TOKEN"))
print("PRODUCT_ID :", os.getenv("AI_PRODUCT_ID"))
