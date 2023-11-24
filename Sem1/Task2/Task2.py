# Написать тест с использованием pytest и requests, в котором:
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# conftest.py содержит фикстуру авторизации
# по адресу https://test-stand.gb.ru/gateway/login
# с передачей параметров “username" и "password" и возвращающей токен авторизации
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя,
# для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером,
# содержащим токен авторизации в параметре "X-Auth-Token".
# Для отображения постов другого пользователя передается "owner": "notMe".
# http://restapi.adequateshop.com/api/authaccount/registration
# http://restapi.adequateshop.com/api/authaccount/login


import requests
import yaml

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)


# url_login = data["url_login"]
# login = data["login"]
# password = data["password"]
# url_posts = data["url_posts"]
# token = data["token"]

# result = requests.post(url=url_login, data={"username": login, "password": password})
# token = result.json()["token"]
# res_get = requests.get(url=url_posts, headers={"X-Auth-Token": token},
#                        params={"owner": "notMe"})
# print(token)
# print(res_get)
# print(res_get.json())


def test_step1(login):
    res_get = requests.get(data["url_posts"], params={"owner": "notMe"}, headers={"X-Auth-Token": login})
    content_var = [item["content"] for item in res_get.json()['data']]
    return content_var


def test_step2(login):
    result = requests.post(data["url_posts"], params={"title": data["title"], "description": data["description"],
                                                      "content": data["content"]},
                           headers={"X-Auth-Token": login})
    res = requests.get(data["url_posts"], params={"description": data["find_description"]},
                       headers={"X-Auth-Token": login})
    return result and res
