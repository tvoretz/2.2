import chardet


def get_rus_list(filename):
        with open('clone/PY1_Lesson_2.3/' + filename, 'rb') as f:
            data = f.read()
            codepage = chardet.detect(data)
            result = data.decode(encoding=codepage['encoding'])
        return result.split(' ')


def print_top_10(file):
    # Получаем список слов в файле
    words_list = get_rus_list(file)

    # Оставляем только слова, где более 6 символов
    short_list = [s.lower() for s in words_list if len(s) >= 6]

    # Составляем словарь, где ключ - слово, значение - сколько раз оно встретилось
    frequency_dict = dict()
    for word in short_list:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1

    # Сортировка словаря, подсмотрено тут https://www.python.org/dev/peps/pep-0265/
    items = [(v, k) for k, v in frequency_dict.items()]
    items.sort()
    items.reverse()
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле {}:'.format(file))
    print(items[:10])

print_top_10('newsfr.txt')
print_top_10('newsit.txt')
print_top_10('newsafr.txt')
print_top_10('newscy.txt')
