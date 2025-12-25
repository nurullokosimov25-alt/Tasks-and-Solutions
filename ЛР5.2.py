#Проверить, является ли название модели палиндромом.
def is_palindrome(model_name):
    clean_name = "".join(model_name.split()).lower()
    return clean_name == clean_name[::-1]
model = "Aziza"
print(f"Является ли '{model}' палиндромом?:", is_palindrome(model))


