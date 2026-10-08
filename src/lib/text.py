import re 
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    Нормализуем строку 
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    '''
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    return " ".join(text.split())

def tokenize(text: str) -> list[str]:
    '''
        Ищу все норм слова 
        assert tokenize("привет, мир!") == ["привет", "мир"]
        assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
        assert tokenize("2025 год") == ["2025", "год"]
    
    '''
    return re.findall(r"\w+(?:-\w+)*", text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    '''
    Перебираем строку и создаем словарь со словами и их кол-вом 
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]
    '''
    dictionary = {}
    for item in tokens:
        if item not in dictionary:
            dictionary[item]=1
        else:
            dictionary[item]+=1
    return dictionary


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''
        Сортируем полученный список
        freq2 = count_freq(["bb","aa","bb","aa","cc"])
        assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    '''
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_freq[:n]



if __name__ == "__main__":
    # normalize
    print(normalize("ПрИвЕт\nМИр\t"))
    print(normalize("ёжик, Ёлка"))
    print(normalize("Hello\r\nWorld"))
    print(normalize("  двойные   пробелы  "))

    # tokenize
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))

    # count_freq + top_n
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    print(freq)
    print(top_n(freq, n=2))

    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    print(freq)
    print(top_n(freq, n=2))