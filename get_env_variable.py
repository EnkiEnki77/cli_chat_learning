# We can utilize the os package to access our environment variables
import os

api_key = os.getenv('API_KEY')
print(api_key)