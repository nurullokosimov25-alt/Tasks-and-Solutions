#Проверить, является ли название модели палиндромом.
def is_palindrome(model_name):
    clean_name = "".join(model_name.split()).lower()
    return clean_name == clean_name[::-1]
model = "Àçèçà"
print(f"ßâëÿåòñÿ ëè '{model}' ïàëèíäðîìîì?:", is_palindrome(model))

