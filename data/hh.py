from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass

# Обновленный hh.py
import requests

class HH(Parser):
    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        self.file_worker = file_worker  # Предполагается, что file_worker реализует save/load

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
            self.save(self.vacancies)  # Сохранение после каждой итерации

    def save(self, data):
        self.file_worker.save(data)

    def load(self):
        return self.file_worker.load()
