from src.api.hh_api import HeadHunterAPI
from src.storage.json_storage import JSONSaver
from src.vacancy.vacancy import Vacancy
from src.utils.utils import filter_vacancies, get_by_salary, sort_vacancies, get_top, print_vacancies


def user_interaction():
    """Основная функция взаимодействия с пользователем."""
    keyword = input("Введите поисковый запрос: ")
    api = HeadHunterAPI()
    try:
        vacancies_data = api.get_vacancies(keyword)
    except Exception as e:
        print(f"Ошибка при получении вакансий: {e}")
        return

    if not vacancies_data:
        print("Вакансии не найдены.")
        return

    # Конвертируем в объекты Vacancy
    vacancies = Vacancy.cast_to_object_list(vacancies_data)

    # Сохраняем в JSON
    saver = JSONSaver()
    for vacancy_data in vacancies_data:  # Сохраняем оригинальные данные из API
        saver.add_vacancy(vacancy_data)

    # Фильтрация, сортировка, выбор топ-N
    filtered = filter_vacancies(vacancies, [keyword])
    sorted_vacancies = sort_vacancies(filtered)
    top_vacancies = get_top(sorted_vacancies, 5)

    # Вывод результатов
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
