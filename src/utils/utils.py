from typing import List
from src.vacancy.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """Фильтрация вакансий по ключевым словам в описании."""
    return [v for v in vacancies if any(kw.lower() in v.description.lower() for kw in keywords)]


def get_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    """Фильтрация по зарплате (пример: '100-150')."""
    if '-' in salary_range:
        min_sal, max_sal = map(int, salary_range.split('-'))
        return [v for v in vacancies if v.salary_from >= min_sal and (v.salary_to or v.salary_from) <= max_sal]
    return vacancies


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка по зарплате (убывание)."""
    return sorted(vacancies, key=lambda v: v.salary_from, reverse=True)


def get_top(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Топ N вакансий."""
    return vacancies[:top_n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Вывод списка вакансий в консоль."""
    if not vacancies:
        print("Вакансии не найдены.")
        return
    for i, vacancy in enumerate(vacancies, 1):
        print(f"Вакансия {i}:")
        print(str(vacancy))
        print("-" * 50)
