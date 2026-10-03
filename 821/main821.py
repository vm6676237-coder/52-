# Дана строка s и символ c, встречающийся в ней s. Верните массив целых чисел, answer где answer.length == s.lengthи
# answer[i]— расстояние от индекса i до ближайшего вхождения символа c в строке s.
#
# Расстояние между двумя индексами iи jравно abs(i - j), где abs— функция абсолютного значения.

def shortestToChar(s, c):
    answer = [10001 for i in range(len(s))]
    index_simbol_c = []

    for i in range(len(s)):
        if s[i] == c: index_simbol_c.append(i)
    index_simbol_c = tuple(index_simbol_c)

    for i in range(len(s)):
        if i in index_simbol_c:
            answer[i] = 0
        else:
            for j in index_simbol_c:
                answer[i] = min(answer[i], abs(i-j))

    return answer

print(shortestToChar("aaab", "b"))