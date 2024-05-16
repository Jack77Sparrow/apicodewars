import requests
import json
import pprint
from users import all_users
from tabulate import tabulate
import matplotlib.pyplot as plt
from tkinter import ttk




def users(username):
    request = requests.get(f"https://www.codewars.com/api/v1/users/{username}")

    if request.status_code == 200:
        return request.json()
    else:
        print("error")
        return None
# pprint.pprint(data)
    

user_info = []

for user in all_users[:3]:
    # print(user)
    link = users(user)
    
    if link:
        user_info.append(link)
def load_info(user_info):
    with open("/Users/drake/Desktop/vscode/parsing/data.json", 'w') as file:

        json.dump(user_info, file, indent=4)
        # json.loads(file)
    
load_info(user_info)
def json_info(name = None):
    with open("/Users/drake/Desktop/vscode/parsing/data.json", 'r') as file:
        
        info = json.load(file)
        
        return info
def get_info():
    info = json_info()
    
    for item in info:

        # print(f"{item["username"]} has a {item["ranks"]["overall"]["score"]} points")

        # print(f"\tHis leader position -> {item["leaderboardPosition"]}")
        # print(f"\tHis honor -> {item["honor"]}\n")
        languages = list(item["ranks"]["languages"].keys())

        for language in languages:

            try:
                
                # print(f"{language} {item["ranks"]["languages"]["python"]["score"]}")
                pass
            except KeyError:
                # print(f"{item["username"]} dont lear python")
                continue

# get_info()


def get_user_info(name):
    user_n = users(name)
    languages = user_n["ranks"]["languages"].keys()
    score = []
    for languag in languages:
        score.append(user_n["ranks"]["languages"][languag]["score"])
    

    return languages, score
    


    

print(get_user_info("g964"))


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
# print(tabulate(table_data, headers=headers, tablefmt="pretty"))


def plt_one_user(name):
    language_user = get_user_info(name)
    



    plt.style.use("ggplot")
    

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.bar(language_user[0], language_user[1], color='blue')
    plt.xlabel('Usernames')
    plt.ylabel('Honor Points')
    plt.title('Honor Points of Codewars Users')
    plt.xticks(rotation=90)
    plt.tight_layout()


    plt.show()


def plt_show(some):
    usernames = [user['username'] for user in user_info]
    honors = [user['honor'] for user in user_info]


    languages = [user["ranks"]["languages"][some]["score"] for user in user_info]
    # print(languages)
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


