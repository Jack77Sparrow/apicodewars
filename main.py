import requests
import json
import pprint
from users import all_users
from tabulate import tabulate
import matplotlib.pyplot as plt
def users(username):
    request = requests.get(f"https://www.codewars.com/api/v1/users/{username}")

    if request.status_code == 200:
        return request.json()
    else:
        print("error")
        return None
# pprint.pprint(data)
    

user_info = []

for user in all_users[:5]:
    # print(user)
    link = users(user)
    
    if link:
        user_info.append(link)
def load_info(user_info):
    with open("/Users/drake/Desktop/vscode/parsing/data.json", 'w') as file:

        json.dump(user_info, file, indent=4)
        # json.loads(file)
    
load_info(user_info)

def get_info():
    with open("/Users/drake/Desktop/vscode/parsing/data.json", 'r') as file:

        info = json.load(file)
    
    for item in info:

        print(f"{item["username"]} has a {item["ranks"]["overall"]["score"]} points")

        print(f"\tHis leader position -> {item["leaderboardPosition"]}")
        print(f"\tHis honor -> {item["honor"]}\n")
        languages = list(item["ranks"]["languages"].keys())

        for language in languages:

            print(f"{language} {item["ranks"]["languages"][language]["score"]}")

get_info()

table_data = []
for user in user_info:
    table_data.append([
        user['username'],
        user['honor'],
        user['clan'] if user['clan'] else "None",
        user['leaderboardPosition']
    ])
# print(table_data)
# Определяем заголовки столбцов
headers = ["Username", "Honor", "Clan", "Leaderboard Position"]

# Выводим таблицу
print(tabulate(table_data, headers=headers, tablefmt="pretty"))


usernames = [user['username'] for user in user_info]
honors = [user['honor'] for user in user_info]


languages = [user["ranks"]["languages"]["python"]["score"] for user in user_info]
print(languages)
plt.style.use("ggplot")

# Построение графика
plt.figure(figsize=(10, 5))
plt.bar(usernames, languages, color='blue')
plt.xlabel('Usernames')
plt.ylabel('Honor Points')
plt.title('Honor Points of Codewars Users')
plt.xticks(rotation=90)
plt.tight_layout()


plt.show()

