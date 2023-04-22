def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = [m] * 256
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip[ord(text[k])]

    return -1


def rabin_karp(text, pattern, d=256, q=101):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    h = pow(d, m-1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    for s in range(n-m+1):
        if p == t:
            if pattern == text[s:s+m]:
                return s
        if s < n-m:
            t = (t-h*ord(text[s])) % q
            t = (t*d + ord(text[s+m])) % q

    return -1

def kmp_search(pattern, text):
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - j + 1

    return -1


def finite_automaton_matcher(text, pattern):
   
    n = len(text)
    m = len(pattern)
    # создаем таблицу переходов
    transition_table = [[0 for _ in range(256)] for _ in range(m + 1)]
    for q in range(m):
        for a in range(256):
            k = min(m + 1, q + 2)
            while k > 0 and pattern[:k - 1] + chr(a) != pattern[:k]:
                k -= 1
            transition_table[q][a] = k
    # инициализируем переменные
    q = 0
    indices = []
    # обходим входную строку
    for i in range(n):
        q = transition_table[q][ord(text[i])]
        if q == m:
            indices.append(i - m + 1)
    if len(indices) == 1:
        return indices[0]
    else: return -1