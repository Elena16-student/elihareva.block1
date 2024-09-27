
class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        sp = ''
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punctuation:
                        line = line.replace(i, '')

                sp = sp + line
            all_words.update({self.file_names: sp.split()})
        return all_words

    def find(self, word):
        dict = {}
        for name, words in self.get_all_words().items():
            for i in words:
                if word.lower() in i:
                    index = words.index(i)
                    dict[self.file_names] = index + 1
                    break
        return dict

    def count(self, word):
        dict = {}
        count = 0
        for name, words in self.get_all_words().items():
            for j in words: # перебираем слова
                if word.lower() in j: #  и если искомое слово там есть, подсчитываем, сколько раз встретилось
                    count += 1
        dict[self.file_names] = count
        return dict


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())  # Все слова
print(finder1.find('captain'))  # cлово Капитан второе в тексте
print(finder1.count('captain'))

finder2 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('child'))# cлово Ребенок первое в тексте
print(finder2.count('child'))

finder3 = WordsFinder('Rudyard Kipling - If.txt')
print(finder3.get_all_words())  # Все слова
print(finder3.find('if')) # cлово Если первое в тексте
print(finder3.count('if'))
