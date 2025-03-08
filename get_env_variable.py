# We can utilize the os and dotenv packages to access our environment variables
import os
from dotenv import load_dotenv

# By default load_dotenv assumes .env is in the same directory as the script, but you can configure
# that with load_dotenv('/custom/path/.env')
load_dotenv()

api_key = os.environ.get("open_ai_api_key")
print(api_key)