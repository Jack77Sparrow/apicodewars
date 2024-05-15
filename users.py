import requests
import pprint
from bs4 import BeautifulSoup


request = requests.get("https://www.codewars.com/users/leaderboard")
parse = BeautifulSoup(request.text, "html.parser")

main = parse.find("div", class_ = "leaderboard p-0")
users = main.find_all("tr")
all_users = []
for user in users:

    some1=user.find_all("a")

    for name in some1:
        all_users.append(name.text)
        # print(name.text)
    
# print(all_users)
        
count_of_users = 1
for use in all_users:
    # print(f"positions of {use} is {count_of_users}")
    count_of_users +=1
