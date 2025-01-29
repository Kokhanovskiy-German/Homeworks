import csv 

filename = "programLanguages.csv"

lan1 = [
    "HTML - заголовки, перенос строк, виды текста, классы"
]

with open(filename, "w", newline="", encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writerow(lan1)

with open(filename, "a", newline="", encoding="UTF-8") as file:
    lan2 = ["CSS - цвет фона и текста, добавление картинок, позиции элемнетов"]
    writer = csv.writer(file)
    writer.writerow(lan2)

with open(filename, "a", newline="", encoding="UTF-8") as file:
    lan3 = ["JS - массивы, функции, циклы"]
    writer = csv.writer(file)
    writer.writerow(lan3)

with open(filename, "a", newline="", encoding="UTF-8") as file:
    lan4 = ["Python - способы сортировки, объекты, переменные, генераторы списков, функции, циклы"]
    writer = csv.writer(file)
    writer.writerow(lan4)