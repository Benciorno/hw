# import requests
# class color:
#    CYAN = '\033[96m'
#    RED = '\033[91m'
#    BOLD = '\033[1m'
#    END = '\033[0m'
# ВТОРОЕ ЗАДАНИЕ
# print(f"{color.BOLD + color.RED}\t\t\t  Студия Гибли\n{color.END}"
#       f"{color.BOLD}Гибли{color.END} — это японская студия анимационных фильмов,"
#       f"\nсоучредителями которой являются:\n"
#       f"Исао Такахата, Хаяо Миядзаки, Тошио Сузуки и Ясуёси Токума.\n"
#       f"Компания начала свою деятельность в июне 1985 года")
# BASE_URL = "https://ghibliapi.herokuapp.com/films/"
# main_data = requests.get(BASE_URL).json()
# title = input(color.BOLD + color.CYAN + "* Напишите название аниме и мы дадим информацию о ней: " + color.END)
#
# release_date = [x["release_date"] for x in main_data if x["title"] == title][0]
# description = [x["description"] for x in main_data if x["title"] == title][0]
# producer = [x["producer"] for x in main_data if x["title"] == title][0]
# original_title = [x["original_title_romanised"] for x in main_data if x["title"] == title][0]
#
# print(f"\t\t\t{color.BOLD}Информация об {title}"
#       f"\nОригинальное название {color.RED + color.BOLD}'{original_title}'{color.END}\n"
#       f"Дата создания - {release_date} году, продюсерам/и {color.BOLD}{producer}{color.END}\n"
#       f"{color.RED + color.BOLD}Описание:{color.END} \n{description}")

# ПЕРВОЕ ЗАДАНИЕ


# from countryinfo import CountryInfo
#
#
# country = CountryInfo(input(f"{color.BOLD + color.CYAN}Напишите название страны и мы дадим информацию о ней: {color.END}"))
# print(f"\t\t{color.BOLD + color.RED}{(country.name()).title()}{color.END}"
#       f"\n{color.BOLD}Плошадь{color.END} - {country.area()}км"
#       f"\n{color.BOLD}Столица страны{color.END} - {country.capital()}"
#       f"\n{color.BOLD}Население страны{color.END} - {country.population()}"
#       f"\n{color.BOLD}Код номера {color.END}- +{country.calling_codes()[0]}"
#       f"\n{color.BOLD}Часовой пояс{color.END} - {country.timezones()[0]}"
#       f"\n{color.BOLD}Материк{color.END} - {country.region()}"
#       f"\n{color.BOLD}Валюта{color.END} - {country.currencies()[0]}")