import requests
import json
import matplotlib.pyplot as plt

def get_page_data(page=0, name=None):
    request = requests.get(f"https://www.codewars.com/api/v1/users/{name}/code-challenges/completed?page={page}")
    if request.status_code == 200:
        return request.json()
    else:
        return None


list_of_names = ["g964", "Jack777Sparrow", "ernest2006pro", "dmethan"]


# all_data = []
# # Получаем данные с первой страницы, чтобы узнать общее количество страниц
# for name in list_of_names:
#     first_page_data = get_page_data(name = name)
#     if first_page_data:
#         total_pages = first_page_data["totalPages"]
        
#         # Получаем данные со всех страниц
#         for i in range(1):

#             page_data = get_page_data(page=i, name = name)
#             if page_data:
#                 all_data.append({name:page_data["data"]})

# # Сохраняем все данные в файл
# with open("/Users/drake/Desktop/vscode/parsing/ex.json", "w") as file:
#     json.dump(all_data, file, indent=4)


with open("/Users/drake/Desktop/vscode/parsing/ex.json", 'r') as file2:
    infos = json.load(file2)


# year = int(input('write a year of completed chalange'))
languages =  ["python", "javascript"]


python = {}
js = {}
# languag = {"python":0,
#             "javascript":0}


def dict_of_users(): 
    U = {}
    for info in infos:
        
        k = 1
        j = 0
        # user_info[inf] = k
        for inf in info:
            languag = {inf:{"python":0,
                    "javascript":0}}
            
            for lis in info[inf]:
                
                python[inf] = k
                js[inf] = j
                
                if "2" in lis['completedAt']:
                    
                    # print(info[0][i]['completedAt'])
                    # print(f"ex - {info[0][i]["name"]}\n\tcompleted language --> {info[0][i]["completedLanguages"]}")

                    for name, i in languag.items():
                        
                        for lang, num in i.items():
                            if lang in lis["completedLanguages"]:


                                languag[name][lang] += 1
                                # print(languag)
                                # print(f"completed by {inf}\n")
                                # print('\t',lis['completedAt'])
                                # print(f"\tex - {lis["name"]}\n\tcompleted language --> {lis["completedLanguages"]}\n")
                    # elif "javascript" in lis["completedLanguages"]:
                    #     j +=1 
                        
                        
                        # print(f"completed by {inf}\n")
                        # print('\t',lis['completedAt'])
                        # print(f"\tex - {lis["name"]}\n\tcompleted language --> {lis["completedLanguages"]}\n")
            U.update(languag)
    return U
                


something = dict_of_users()
for some in something:
    print(some)
print(something)
def show_plt(language = "python"):
    usernames = list(something.keys())
    
    # lan = [value.values()["python"] for value in something]
    # list_of_kat = []
    # for value in something:
        
    #     list_of_kat.append(list(value.values())[0].get(language, 0))
    list_of_kat = [something[user].get(language, 0) for user in usernames]
    print(usernames)
    print(list_of_kat)
    # print(languages)
    plt.style.use("ggplot")
    

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.bar(usernames, list_of_kat, color='blue')
    plt.xlabel('Usernames')
    plt.ylabel('python accept kata')
    plt.title('Honor accept kata of Codewars Users')
    plt.xticks(rotation=90)
    plt.tight_layout()


    plt.show()

show_plt(language="python")


