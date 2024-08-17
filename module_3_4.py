def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        root_word_1 = root_word.upper()
        other_words_1 = i.upper()
        if other_words_1 in root_word_1 or root_word_1 in other_words_1:
            same_words.append(i)
    return same_words


result1 = single_root_words('Доми', 'До', 'ДоМисолька', 'РеДоМи', 'МиФа')
result2 = single_root_words('Осколок', 'КОЛ', 'скОл', 'Прикол', 'кусок')
print(result1)
print(result2)

