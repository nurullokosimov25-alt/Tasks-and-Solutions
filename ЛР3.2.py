# “Динамический форматтер таблиц” (среднее) Функция: table(**kwargs) Функция должна:
# • определить максимальную длину ключа • красиво вывести таблицу вида: parameter value -------- ----- version 1.0 debug True
def table_mini(**kwargs):
    """Мини-версия форматтера."""
    if not kwargs:
        print("parameter value\n----- -----")
        print("None  None")
        return

    # 1. Находим максимальную длину ключа, минимум - 9 (длина 'parameter')
    w = max(len(str(k)) for k in kwargs.keys())
    w = max(w, len("parameter"))
    
    # 2. Вывод заголовков и разделителя
    print(f"{'parameter'.ljust(w)} value")
    print(f"{'-' * w} -----")
    
    # 3. Вывод данных
    for key, value in kwargs.items():
        print(f"{str(key).ljust(w)} {str(value)}")

