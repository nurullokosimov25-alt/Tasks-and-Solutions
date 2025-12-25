# Рекурсивно проверить, отсортирован ли список по возрастанию. Важно: без использования sorted().
def is_sorted_recursive(lst):
   
    if len(lst) <= 1:
        return True
   
    if lst[0] > lst[1]:
        return False
  
    return is_sorted_recursive(lst[1:])

list_a = [1, 2, 5, 8, 12]
list_b = [1, 2, 10, 5, 12]
print(f"Список {list_a} отсортирован? {is_sorted_recursive(list_a)}")
print(f"Список {list_b} отсортирован? {is_sorted_recursive(list_b)}")

