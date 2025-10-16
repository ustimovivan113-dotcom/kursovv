import pytest
from src.api.hh_api import HeadHunterAPI
import requests


@pytest.fixture
def api():
    return HeadHunterAPI()


def test_connect_error(monkeypatch, api):
    def mock_get(*args, **kwargs):
        raise requests.RequestException("Connection error")

    monkeypatch.setattr(requests, 'get', mock_get)
    with pytest.raises(ConnectionError):
        api.connect()


def test_get_vacancies_error(monkeypatch, api):
    def mock_get(*args, **kwargs):
        raise requests.RequestException("API error")

    monkeypatch.setattr(requests, 'get', mock_get)
    with pytest.raises(ConnectionError):  # Изменяем на ConnectionError
        api.get_vacancies("test")


def test_get_vacancies_mock(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
                self.text = '{"items": [{"id": "1", "name": "Test Job", "alternate_url": "http://hh.ru/1", "salary": {"from": 100000}, "snippet": {"requirement": "req", "responsibility": "resp"}, "employer": {"name": "Test Employer"}}]}'

            def json(self):
                return eval(self.text)  # Используем eval для простоты в тесте

        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    api = HeadHunterAPI()
    data = api.get_vacancies("test", 1)
    assert len(data) == 1
    assert data[0]["name"] == "Test Job"
