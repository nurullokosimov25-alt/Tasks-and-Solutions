# «Обработка данных о студентах» 
# Дано: students = ["Ali_2004", "Zuhra_2003", "mansur_2005", "RUSTAM_2004"] Каждая строка содержит имя + год рождения. Что нужно сделать 
# 1. Разделить строку на имя и год (split("_")). 2. Имя привести к виду: первая буква заглавная, остальные маленькие. 
# 3. Год преобразовать в число. 4. Создать список строк формата: "Имя, возраст: ХХ" (возраст считать как 2025 – год рождения) 
# 5. Вывести список.
students = ["Ali_2004", "Zuhra_2003", "mansur_2005", "RUSTAM_2004"]
result = []
for student in students:
    name_raw, year_raw = student.split("_")
    name = name_raw.capitalize()
    year = int(year_raw)
    age = 2025 - year
    result.append(f"{name}, возраст: {age}")
print(result)

