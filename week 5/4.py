import requests
import sys

url=sys.argv[1]
response = requests.get(url, timeout=5)
        
if response.status_code == 200:
    print(f"The website at {url} is working.")
else:
    print(f"The website at {url} is not working.")


