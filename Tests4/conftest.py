from uuid import uuid4
import pytest
import requests

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

@pytest.fixture
def token():
    token = 'Ваш токен от yandex диска'
    if not token:
        pytest.fail("Ya-token не установлен в переменных")
    return token

@pytest.fixture()
def headers(token):
    return {
        'Authorization': f'OAuth {token}'
    }

@pytest.fixture
def temp_folder():
    return f"test-folder-{uuid4()}"

@pytest.fixture
def create_and_cleanup_folder(headers, temp_folder):
    """ создаем папку  и удаляем """
    folder_path = f"disk:/{temp_folder}"
    """ Создаем """
    response = requests.put(BASE_URL, headers=headers, params={'path': folder_path})
    assert response.status_code in [201, 409], f"Ошибка при создании {response.status_code, response.text}"
    # 201 - создано успешно
    # 409 - папка уже существует
    yield temp_folder # передает управление в тест

    """ Удаление """
    delete_response = requests.delete(BASE_URL, headers=headers, params={'path': folder_path})
    if delete_response.status_code != 204:
        print(f"Не удалось удалить папку: {delete_response.status_code} {delete_response.text}")

