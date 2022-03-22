import requests
from bs4 import BeautifulSoup


def parse_main_page():
    final_ret_data = []
    url = "https://freelance.habr.com/tasks"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    alltasks = soup.findAll('div', class_='task__title')
    for data in alltasks:
        task_title = data.text
        href = data.find('a')['href']
        link = f"https://freelance.habr.com{href}"
        task_id = int(href.replace("/tasks/", ""))
        final_ret_data.append((task_title, link, task_id))
    
    return final_ret_data

if __name__ == "__main__":
    print(parse_main_page())
