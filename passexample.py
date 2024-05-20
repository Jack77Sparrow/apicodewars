import requests
import json



def get_page_data(page=0, name="g964"):
    request = requests.get(f"https://www.codewars.com/api/v1/users/{name}/code-challenges/completed?page={page}")
    if request.status_code == 200:
        return request.json()
    else:
        return None

all_data = []
# Получаем данные с первой страницы, чтобы узнать общее количество страниц
first_page_data = get_page_data()
if first_page_data:
    total_pages = first_page_data["totalPages"]
    
    # Получаем данные со всех страниц
    for i in range(total_pages):
        page_data = get_page_data(page=i)
        if page_data:
            all_data.append(page_data["data"])

# # Сохраняем все данные в файл
# with open("/Users/drake/Desktop/vscode/parsing/ex.json", "w") as file:
#     json.dump(all_data, file, indent=4)


with open("/Users/drake/Desktop/vscode/parsing/ex.json", 'r') as file2:
    info = json.load(file2)
j = 0
for i in range(len(info[0])):

    if "2022" in info[0][i]['completedAt']:
       
        # print(info[0][i]['completedAt'])
        # print(f"ex - {info[0][i]["name"]}\n\tcompleted language --> {info[0][i]["completedLanguages"]}")
        if "python" in info[0][i]["completedLanguages"] and len(info[0][i]["completedLanguages"]) == 1:
            j+=1
            print(info[0][i]['completedAt'])
            print(f"ex - {info[0][i]["name"]}\n\tcompleted language --> {info[0][i]["completedLanguages"]}")

    
        

print(j)




