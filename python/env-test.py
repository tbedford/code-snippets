from dotenv import load_dotenv
import os



load_dotenv()

print(os.getenv("MY_VAR"))
print(os.getenv("PATH"))
