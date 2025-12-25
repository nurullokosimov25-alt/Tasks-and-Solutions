# Найти расстояние между повторениями символа (позиции i и j) Например: s = "abcaab" повтор "a" на позициях 0, 3, 4 → расстояния: 3, 1
# Использовать словарь-аккумулятор: last_seen[ch] = позиция 
﻿def distances_between_repeats(s):
    last_seen = {}      
    distances = []       

    for i, ch in enumerate(s):
        if ch in last_seen:                  
            distances.append(i - last_seen[ch])
        last_seen[ch] = i                  

    return distances
print(distances_between_repeats("abcaab"))

