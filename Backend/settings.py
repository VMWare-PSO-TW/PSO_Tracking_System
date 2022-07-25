import os
from dotenv import load_dotenv
from urllib.parse import quote  

load_dotenv()

db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_pass = quote(os.environ.get("DB_PASS"))