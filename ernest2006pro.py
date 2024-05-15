import requests
import bs4



request = requests.get(f"https://www.codewars.com/api/v1/users/ernest2006pro")

print(request.json()["ranks"]["overall"])