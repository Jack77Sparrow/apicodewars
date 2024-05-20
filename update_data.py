import json
import matplotlib.pyplot as plt

with open("/Users/drake/Desktop/vscode/parsing/data.json", 'r') as file:
    values = json.load(file)
    

all_data = {}
skills = {}
i = 0
for value in values:
    
    some = value["codeChallenges"]["totalCompleted"]
    someone = value["username"]
    all_data[someone] = some
    skill = value["skills"]
    for skil in skill:
        i+=1
        
    skills[someone] = i
    print(i)



print(skills)



def plot_skils():
    plt.style.use("ggplot")
    

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.bar(skills.keys(), skills.values(), color='blue')
    plt.xlabel('Usernames')
    plt.ylabel('Honor Points')
    plt.title('Honor Points of Codewars Users')
    plt.xticks(rotation=90)
    plt.tight_layout()


    plt.show()
# plot_skils()

def plot():
    plt.style.use("ggplot")
    

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.bar(all_data.keys(), all_data.values(), color='blue')
    plt.xlabel('Usernames')
    plt.ylabel('Honor Points')
    plt.title('Honor Points of Codewars Users')
    plt.xticks(rotation=90)
    plt.tight_layout()


    plt.show()

# plot()
