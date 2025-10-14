from src.api.hh_api import HeadHunterAPI
from src.vacancy.vacancy import Vacancy
from src.storage.json_storage import JSONSaver
from src.utils.utils import filter_vacancies, get_by_salary, sort_vacancies, get_top, print_vacancies

def user_interaction():
    api = HeadHunterAPI()
    saver = JSONSaver()

    query = input("Поисковый запрос: ")
    vacancies_data = api.get_vacancies(query)
    vacancies = Vacancy.cast_to_object_list(vacancies_data)

    for d in vacancies_data:
        saver.add_vacancy(d)

    n = int(input("Топ N: "))
    words = input("Ключевые слова (пробел): ").split()
    range_str = input("Диапазон зарплат (min-max): ")

    filtered = filter_vacancies(vacancies, words)
    ranged = get_by_salary(filtered, range_str)
    sorted_v = sort_vacancies(ranged)
    top = get_top(sorted_v, n)
    print_vacancies(top)

    if vacancies_data:
        saver.delete_vacancy(vacancies_data[0])
        print("Удалена первая вакансия.")

if __name__ == "__main__":
    user_interaction()
