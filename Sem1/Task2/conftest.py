import pytest
import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


# url_login = data["url_login"]
# login = data["login"]
# password = data["password"]
# url_posts = data["url_posts"]


@pytest.fixture()
def login():
    result = requests.post(data["url_login"], data={"username": data["login"], "password": data["password"]})
    return result.json()["token"]




