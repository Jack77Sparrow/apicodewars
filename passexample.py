import requests
import json
import matplotlib.pyplot as plt

def get_page_data(page=0, name=None):
    request = requests.get(f"https://www.codewars.com/api/v1/users/{name}/code-challenges/completed?page={page}")
    if request.status_code == 200:
        return request.json()
    else:
        return None


list_of_names = ["g964", "Jack777Sparrow", "ernest2006pro"]

all_data = []
# Получаем данные с первой страницы, чтобы узнать общее количество страниц
for name in list_of_names:
    first_page_data = get_page_data(name = name)
    if first_page_data:
        total_pages = first_page_data["totalPages"]
        
        # Получаем данные со всех страниц
        for i in range(1):

            page_data = get_page_data(page=i, name = name)
            if page_data:
                all_data.append({name:page_data["data"]})

# # Сохраняем все данные в файл
# with open("/Users/drake/Desktop/vscode/parsing/ex.json", "w") as file:
#     json.dump(all_data, file, indent=4)


with open("/Users/drake/Desktop/vscode/parsing/ex.json", 'r') as file2:
    infos = json.load(file2)
j = 0
# year = int(input('write a year of completed chalange'))
user_info = {}
for info in infos:
    
    k = 1
    # user_info[inf] = k
    for inf in info:
        
        for lis in info[inf]:
            
            user_info[inf] = k
                
            if "2" in lis['completedAt']:
                
                # print(info[0][i]['completedAt'])
                # print(f"ex - {info[0][i]["name"]}\n\tcompleted language --> {info[0][i]["completedLanguages"]}")
                if "python" in lis["completedLanguages"]:
                    k+=1
                    j+=1
                    print(f"completed by {inf}\n")
                    print('\t',lis['completedAt'])
                    print(f"\tex - {lis["name"]}\n\tcompleted language --> {lis["completedLanguages"]}\n")

            

print(user_info)
print(j)

def show_plt():
    
    # print(languages)
    plt.style.use("ggplot")
    

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.bar(user_info.keys(), user_info.values(), color='blue')
    plt.xlabel('Usernames')
    plt.ylabel('python accept kata')
    plt.title('Honor accept kata of Codewars Users')
    plt.xticks(rotation=90)
    plt.tight_layout()


    plt.show()

show_plt()


