import os
from dotenv import load_dotenv

# Reading .env and creating environment variables
load_dotenv()

# Reading environment variable
host = os.getenv("DB_HOST")

# Using environment variable
print(host)