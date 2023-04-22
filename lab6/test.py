from main import *

text = "The quick brown fox jumps over the lazy dog"
pattern1 = "fox"
pattern2 = "cat"

print("– Бойера-Мура")
boyer = boyer_moore(text, pattern1)
if boyer == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {boyer}")
boyer = boyer_moore(text, pattern2)
if boyer == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {boyer}")

print("\n– Рабина-Карпа")
rabin = rabin_karp(text, pattern1)
if rabin == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {rabin}")
rabin = rabin_karp(text, pattern2)
if rabin == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {rabin}")

print("\n- Кнута-Морриса-Пратта")
kmp = kmp_search(pattern1, text)
if kmp == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {kmp}")
kmp = kmp_search(pattern2, text)
if kmp == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {kmp}")

print("\n– с помощью конечного автомата")
auto = finite_automaton_matcher(text, pattern1)
if auto == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {auto}")
auto = finite_automaton_matcher(text, pattern2)
if auto == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {auto}")