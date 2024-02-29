import os
from dotenv import load_dotenv
load_dotenv()

print("Hello!")

print("This is Hello project")

print("Please edit this file")

key = os.environ["SOMETHING_KEY"]

print(f"{key}")